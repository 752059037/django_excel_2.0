from django.shortcuts import render, redirect
from threading import Thread
import datetime
from django import views
import xlrd
from xlrd import xldate_as_tuple
from excel_import import models
from django.db import transaction
from excel_import import forms
import logging
import xlwt
from django.conf import settings

logging.basicConfig(level=logging.ERROR,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt=' %Y-%m-%d %H:%M:%S',
                    filename='bug.log', filemode='a',
                    )

# Create your views here.




SHEET_TO_TABLE = settings.SHEET_TO_TABLE
HEADER_LINE = settings.HEADER_LINE
START_LINE = settings.START_LINE
EXCEL_EXPORT_PATH = settings.EXCEL_EXPORT_PATH
UNIQUE = settings.UNIQUE
SHEET_BLACKLIST = settings.SHEET_BLACKLIST


class Read_sheet(views.View):
    def get(self, request):
        return render(request, 'import_excel.html')
    
    def post(self, request):
        try:
            global xlsx_obj
            xlsx = request.FILES.get('xlsx')
            if xlsx:
                file_formats = xlsx.name.split('.')[-1]
                if file_formats == 'xlsx':
                    content = xlsx.read()  # 取到句柄
                    xlsx_obj = Operation_xlsx(content)  # 实例化xlsx对象
                    sheet_list = xlsx_obj.read_sheet()  # 取到所有sheet名
                    ret = {'code': 1, 'msg': sheet_list}
                else:
                    ret = {'code': 0, 'msg': [{'文件错误': ['请传入正确文件']}], 'last_url': '/import_excel'}
            else:
                ret = {'code': 0, 'msg': [{'文件错误': ['文件为空']}], 'last_url': '/import_excel'}
            return render(request, 'import_excel.html', {'ret': ret})
        except Exception as e:
            logging.error(e)
            return render(request, 'import_excel.html',
                          {'ret': {'code': 0, 'msg': [{'服务器错误': ['服务器发生了未知的错误']}]}, 'last_url': '/import_excel'})


class Save_xlsx(views.View):
    
    def get(self, request):
        redirect('/')
    
    def post(self, request):
        error_msg = []
        try:
            sheet_name = request.POST.getlist('sheet_name')  # 取到要保存的sheet名
            t_list = []
            for i in sheet_name:
                xlsx_iter = xlsx_obj.read_data(i)
                ret = xlsx_obj.verity_save_xlsx(xlsx_iter,)
                if ret['code'] == 0:
                    error_msg.append(ret)
            return render(request, 'save_excel.html', {'error_msg': error_msg})
        except Exception as e:
            logging.error(e)
            return render(request, 'save_excel.html', {'error_msg': error_msg})

class Operation_xlsx:
    """
    操作excel表格的类
    传入excel表格的路径
    
    excel数据类型对照表:
        0: empty
        1: string(text)
        2: number
        3: date
        4: boolean
        5: error
        6: blank
    """
    
    def __init__(self, content):
        content = content
        self.data = xlrd.open_workbook(file_contents=content)  # 读excel太慢
    
    def read_data(self, table_name):
        """
        :return: 返回生成器,包含{'sheet_name':sheet名,'line_num':行数,'content':内容}
        """
        sheet = self.data.sheet_by_name(table_name)
        nrows = sheet.nrows
        
        for i in range(START_LINE - 1 - 1, nrows):
            row_type = sheet.row_types(i)
            data = sheet.row_values(i)
            for index, cell_type_num in enumerate(row_type, 0):
                if cell_type_num == 3:  # 将Excel时间类型转化为datetime类型
                    data[index] = datetime.datetime(*xldate_as_tuple(sheet.row_values(i)[index], 0))
            yield_data = {'sheet_name': sheet.name, 'line_num': i + 1, 'content': data}
            yield yield_data
    
    def read_sheet(self):
        """
        :return: 返回含有sheet名的列表,隐藏sheet视为没有
        """
        sheet_list = []
        for sheet in self.data.sheets():
            if sheet.name in SHEET_BLACKLIST: # 不导入的表就不展示
                continue
            if sheet.visibility == 0:
                sheet_list.append(sheet.name)
        return sheet_list
    
    def __get_dic(self, header, content):
        """
        :return: 返回一个字段名与数据对应的字典,用于校验数据
        """
        dic = {}
        for title in header:
            index = header.index(title)  # 根据表头标题取到对应的数据
            dic[title] = content[index]  # 构建成字典{'brand_id':88,'brand_name','雪佛兰'}
        return dic
    
    def __model_to_unique(self, model_name, clean_data):
        """
        此函数传入model名,返回唯一字段,用于确定字段的更新or创建
        :param model_name:
        :return:
        """
        unique_dic = {}
        unique_field = UNIQUE[model_name]
        for i in unique_field:
            unique_clean_data = clean_data.get(i)
            unique_dic.setdefault(i, unique_clean_data)
        return unique_dic
    
    def verity_save_xlsx(self, xlsx_iter):
        """
        :param xlsx_iter: 生成器对象或可迭代对象
        :return: 返回错误信息
        """
        global sheet_name
        ret = {'code': 1, 'msg': []}
        try:
            with transaction.atomic():  # 开启事务 如果出错则全部不保存
                header = []
                for line in xlsx_iter:  # 循环得到excel里的每行数据
                    sheet_name = line['sheet_name']
                    line_num = line['line_num']
                    content = line['content']
                    if line_num == HEADER_LINE:  # 如果是行数==表头行,则取到表头
                        header = line['content']
                    
                    elif line_num > HEADER_LINE:
                        dic = self.__get_dic(header, content)
                        form_name = SHEET_TO_TABLE[sheet_name][1]
                        form_obj = getattr(forms, form_name)(dic)  # 通过反射取到form对象
                        
                        if form_obj.is_valid():  # 如果数据正确,按照唯一字段,有则更新 无则创建
                            model_name = SHEET_TO_TABLE[sheet_name][0]
                            clean_data = form_obj.cleaned_data
                            unique_field = self.__model_to_unique(model_name, clean_data, )  # 构建唯一字段对应的字典
                            reflect_model = getattr(models, model_name)  # 反射取到对应的model类
                            reflect_model.objects.update_or_create(
                                **unique_field,
                                defaults=clean_data
                            )
                            
                        else:
                            error_data, error_msg = list(form_obj.errors.items())[0]
                            
                            ret['msg'].append({'{}页 第{}行,{}'.format(sheet_name, line_num, error_data, ): error_msg})
                if ret['msg']:
                    ret['code'] = 0
                    raise ValueError('表格出现异常,执行回滚')
        except ValueError as ve:
            logging.info(ve)
        except KeyError as ke:
            ret['msg'].append({sheet_name: ['此页无对应的数据表', ]})
            logging.info(ke)
        except Exception as e:
            ret['msg'].append({sheet_name: ['表格格式错误', ]})
            logging.error(e)
            # raise e
        
        return ret


class Excel_export(views.View):
    
    def get(self, request):
        ret = {'code': None, 'sheet_name_list': []}
        try:
            sheet_name = request.GET.get('sheet_name')
            if not sheet_name:
                for i in dir(models):
                    if i.startswith('Bx'):
                        model = getattr(models, i)
                        obj = model.objects.first()
                        if obj:
                            ret['sheet_name_list'].append(obj._meta.verbose_name)
                            ret['last_url'] = '/'
            else:
                workbook = xlwt.Workbook(encoding='utf-8')
                sheet = workbook.add_sheet(sheet_name, cell_overwrite_ok=True)
                model_name = SHEET_TO_TABLE[sheet_name][0]
                model = getattr(models, model_name)

                field = model.objects.first()
                if field:
                    field = field._meta.fields  # 取到模型的所有字段
                
                # 构建要保存的数据格式,第一个为所有字段组成的列表,作为excel的表头
                DATA = [[i.name for i in field], ]
                
                query_set = model.objects.values_list(
                )
                style = xlwt.XFStyle()
                for i in query_set:
                    DATA.append(i)
                for i, row in enumerate(DATA):
                    for j, col in enumerate(row):
                        if isinstance(col, datetime.datetime):  # 转换datetime格式
                            style.num_format_str = 'YY/MM/DD h:mm:ss'
                            col = col.replace(tzinfo=None)
                            sheet.write(i, j, col, style)
                        elif isinstance(col, datetime.date):  # 转换date格式
                            style.num_format_str = 'YY/MM/DD '
                            sheet.write(i, j, col, style)
                        else:
                            sheet.write(i, j, col, )
                workbook.save('{}/{}.xls'.format(EXCEL_EXPORT_PATH, sheet_name))
                ret['code'] = 1
        except Exception as e:
            ret['code'] = 0
            logging.error(e)
        return render(request, 'export_excel.html', {'ret': ret})


class Index(views.View):
    def get(self, request):
        return render(request, 'index.html')
