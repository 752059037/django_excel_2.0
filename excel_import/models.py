# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class BxContrast(models.Model):
    station_id = models.IntegerField()
    contrast_id = models.IntegerField()
    contrast_name = models.CharField(max_length=255, blank=True, null=True)
    insert_time = models.DateTimeField(auto_now_add=True)
    update_tms = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'bx_contrast'
        verbose_name = '竞品关联表'


class BxDevice(models.Model):
    station_id = models.IntegerField()
    device_id = models.IntegerField()
    device_name = models.CharField(max_length=255)
    device_type = models.CharField(max_length=255)
    insert_time = models.DateTimeField(auto_now_add=True)
    update_tms = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'bx_device'
        verbose_name = '站点设备信息表'


class BxEverydayContrastData(models.Model):
    filter_name = models.CharField(max_length=255)
    filter_date = models.CharField(max_length=250)
    column_name = models.CharField(max_length=255)
    remark = models.CharField(max_length=255, blank=True, null=True)
    table_id = models.IntegerField()
    parent_id = models.IntegerField()
    n_coverage = models.FloatField()
    n_entry = models.FloatField()
    n_stay = models.FloatField()
    negotiate_entry = models.FloatField(blank=True, null=True)
    entry_rate = models.FloatField()
    stay_rate = models.FloatField()
    negotiate_entry_rate = models.FloatField(blank=True, null=True)
    insert_tms = models.DateTimeField(auto_now_add=True)
    update_tms = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'bx_everyday_contrast_data'
        verbose_name = '环比数据表'
        


class BxEverydayData(models.Model):
    station_id = models.IntegerField()
    date = models.DateField()
    n_coverage = models.IntegerField(blank=True, null=True)
    n_entry = models.IntegerField(blank=True, null=True)
    n_stay = models.IntegerField(blank=True, null=True)
    negotiate_entry = models.IntegerField(blank=True, null=True)
    conclusion = models.CharField(max_length=255, blank=True, null=True)
    hotmap_url_1 = models.CharField(max_length=255, blank=True, null=True)
    hotmap_url_2 = models.CharField(max_length=255, blank=True, null=True)
    insert_tms = models.DateTimeField(auto_now_add=True)
    update_tms = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'bx_everyday_data'
        verbose_name = '站点数据表'


class BxLiveUrl(models.Model):
    station_id = models.IntegerField()
    cam_name = models.CharField(max_length=255)
    live_url = models.CharField(max_length=255)
    insert_tms = models.DateTimeField(auto_now_add=True)
    update_tms = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'bx_live_url'
        verbose_name = '直播配置'



class BxPerformArrange(models.Model):
    station_id = models.IntegerField()
    station_name = models.CharField(max_length=255, blank=True, null=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    pic_time_gap = models.IntegerField()
    pic_count = models.IntegerField()
    status = models.IntegerField()
    insert_tms = models.DateTimeField(auto_now_add=True)
    update_tms = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'bx_perform_arrange'
        verbose_name = '演艺时间'


class BxRoiTraffic(models.Model):
    station_id = models.IntegerField()
    roi_id = models.IntegerField()
    car_model_type = models.CharField(max_length=255)
    date = models.DateField()
    n_entry = models.IntegerField(blank=True, null=True)
    ratio = models.FloatField()
    insert_tms = models.DateTimeField(auto_now_add=True)
    update_tms = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'bx_roi_traffic'
        verbose_name = '车型热度表'


class BxStationDetail(models.Model):
    outer_station_id = models.IntegerField(blank=True, null=True)
    station_id = models.IntegerField()
    station_name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    brand_id = models.IntegerField()
    region = models.CharField(max_length=255)
    province = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    station_type = models.IntegerField()
    grade = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    grade_id = models.IntegerField()
    pic_time_gap = models.IntegerField(blank=True, null=True)
    hotmap_url_1 = models.CharField(max_length=255, blank=True, null=True)
    hotmap_url_2 = models.CharField(max_length=255, blank=True, null=True)
    station_address = models.CharField(max_length=255)
    contrast_id = models.CharField(max_length=255, blank=True, null=True)
    insert_tms = models.DateTimeField(auto_now_add=True)
    update_tms = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'bx_station_detail'
        verbose_name = '站点信息表'


class BxText(models.Model):
    brand_id = models.IntegerField()
    dashboard_id = models.IntegerField()
    dashboard_name = models.CharField(max_length=255)
    data = models.CharField(max_length=255)
    seq = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bx_text'
        verbose_name = '文本'

