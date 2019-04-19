from __future__ import unicode_literals

from django.db import models


class BxContrast(models.Model):
    station_id = models.IntegerField()
    contrast_id = models.IntegerField()
    contrast_name = models.CharField(max_length=255)
    insert_tms = models.DateTimeField(auto_now_add=True)
    update_tms = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'bx_contrast'
        verbose_name = '竞品关联表'


class BxDevice(models.Model):
    station_id = models.IntegerField()
    device_id = models.IntegerField()
    device_name = models.CharField(max_length=255)
    insert_tms = models.DateTimeField(auto_now_add=True)
    update_tms = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'bx_device'
        verbose_name = '站点设备信息表'


class BxEverydayContrastData(models.Model):
    brand_id = models.IntegerField()
    parent_id = models.IntegerField()
    grade = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    n_coverage = models.FloatField()
    n_entry = models.FloatField()
    n_stay = models.FloatField()
    negotiate_entry = models.FloatField()
    negotiate_entry_rate = models.FloatField()
    entry_rate = models.FloatField()
    stay_rate = models.FloatField()
    month_id = models.CharField(max_length=250)
    insert_tms = models.DateTimeField(auto_now_add=True)
    update_tms = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'bx_everyday_contrast_data'
        verbose_name = '环比数据表'


class BxEverydayData(models.Model):
    station_id = models.IntegerField()
    date = models.DateField()
    n_coverage = models.IntegerField()
    n_entry = models.IntegerField()
    n_stay = models.IntegerField()
    negotiate_entry = models.IntegerField(blank=True, null=True)
    conclusion = models.CharField(max_length=255, blank=True, null=True)
    hotmap_url_1 = models.CharField(max_length=255, blank=True, null=True)
    hotmap_url_2 = models.CharField(max_length=255, blank=True, null=True)
    insert_tms = models.DateTimeField(auto_now_add=True)
    update_tms = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'bx_everyday_data'
        verbose_name = '站点数据表'


class BxLiveUrl(models.Model):
    station_id = models.IntegerField()
    cam_name = models.CharField(max_length=255)
    live_url = models.CharField(max_length=255)
    insert_tms = models.DateTimeField(auto_now_add=True)
    update_tms = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
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
        managed = True
        db_table = 'bx_perform_arrange'
        verbose_name = '演艺时间'


class BxRoiTraffic(models.Model):
    id = models.IntegerField(primary_key=True)
    station_id = models.IntegerField()
    roi_id = models.IntegerField()
    car_model_type = models.CharField(max_length=255)
    date = models.DateField()
    n_entry = models.IntegerField()
    ratio = models.FloatField()
    insert_tms = models.DateTimeField(auto_now_add=True)
    update_tms = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'bx_roi_traffic'
        verbose_name = '车型热度表'


class BxStationDetail(models.Model):
    outer_station_id = models.IntegerField(blank=True, null=True)
    station_id = models.IntegerField()
    station_name = models.CharField(max_length=255)
    brand_name = models.CharField(max_length=255)
    brand_id = models.IntegerField()
    region = models.CharField(max_length=255)
    province = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    station_type = models.IntegerField()
    grade_name = models.CharField(max_length=255)
    station_address = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    # grade_id = models.IntegerField()
    pic_time_gap = models.IntegerField(blank=True, null=True)
    hotmap_url_1 = models.CharField(max_length=255, blank=True, null=True)
    hotmap_url_2 = models.CharField(max_length=255, blank=True, null=True)
    contrast_id = models.CharField(max_length=255, blank=True, null=True)
    insert_tms = models.DateTimeField(auto_now_add=True)
    update_tms = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'bx_station_detail'
        verbose_name = '站点信息表'


class BxText(models.Model):
    brand_id = models.IntegerField()
    dashboard_id = models.IntegerField()
    block_name = models.CharField(max_length=255)
    data = models.CharField(max_length=255)
    # station_id = models.IntegerField(blank=True, null=True)
    seq = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'bx_text'
        verbose_name = '文本'