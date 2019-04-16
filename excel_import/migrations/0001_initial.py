# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-04-16 06:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BxContrast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('station_id', models.IntegerField()),
                ('contrast_id', models.IntegerField()),
                ('contrast_name', models.CharField(max_length=255)),
                ('insert_tms', models.DateTimeField(auto_now_add=True)),
                ('update_tms', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'bx_contrast',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='BxDevice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('station_id', models.IntegerField()),
                ('device_id', models.IntegerField()),
                ('device_name', models.CharField(max_length=255)),
                ('insert_tms', models.DateTimeField(auto_now_add=True)),
                ('update_tms', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'bx_device',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='BxEverydayContrastData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_id', models.IntegerField()),
                ('parent_id', models.IntegerField()),
                ('grade', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('n_coverage', models.FloatField()),
                ('n_entry', models.FloatField()),
                ('n_stay', models.FloatField()),
                ('negotiate_entry', models.FloatField()),
                ('entry_rate', models.FloatField()),
                ('stay_rate', models.FloatField()),
                ('month_id', models.CharField(max_length=250)),
                ('insert_tms', models.DateTimeField(auto_now_add=True)),
                ('update_tms', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'bx_everyday_contrast_data',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='BxEverydayData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('station_id', models.IntegerField()),
                ('date', models.DateField()),
                ('n_coverage', models.IntegerField()),
                ('n_entry', models.IntegerField()),
                ('n_stay', models.IntegerField()),
                ('negotiate_entry', models.IntegerField(blank=True, null=True)),
                ('conclusion', models.CharField(blank=True, max_length=255, null=True)),
                ('hotmap_url_1', models.CharField(blank=True, max_length=255, null=True)),
                ('hotmap_url_2', models.CharField(blank=True, max_length=255, null=True)),
                ('insert_tms', models.DateTimeField(auto_now_add=True)),
                ('update_tms', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'bx_everyday_data',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='BxLiveUrl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('station_id', models.IntegerField()),
                ('cam_name', models.CharField(max_length=255)),
                ('live_url', models.CharField(max_length=255)),
                ('insert_tms', models.DateTimeField(auto_now_add=True)),
                ('update_tms', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'bx_live_url',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='BxPerformArrange',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('station_id', models.IntegerField()),
                ('station_name', models.CharField(blank=True, max_length=255, null=True)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('pic_time_gap', models.IntegerField()),
                ('pic_count', models.IntegerField()),
                ('insert_tms', models.DateTimeField(auto_now_add=True)),
                ('update_tms', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'bx_perform_arrange',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='BxRoiTraffic',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('station_id', models.IntegerField()),
                ('roi_id', models.IntegerField()),
                ('car_model_type', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('n_entry', models.IntegerField()),
                ('ratio', models.FloatField()),
                ('insert_tms', models.DateTimeField(auto_now_add=True)),
                ('update_tms', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'bx_roi_traffic',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='BxStationDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('outer_station_id', models.IntegerField(blank=True, null=True)),
                ('station_id', models.IntegerField()),
                ('station_name', models.CharField(max_length=255)),
                ('brand_name', models.CharField(max_length=255)),
                ('brand_id', models.IntegerField()),
                ('region', models.CharField(max_length=255)),
                ('province', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('station_type', models.IntegerField()),
                ('grade_name', models.CharField(max_length=255)),
                ('station_address', models.CharField(max_length=255)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('pic_time_gap', models.IntegerField(blank=True, null=True)),
                ('hotmap_url_1', models.CharField(blank=True, max_length=255, null=True)),
                ('hotmap_url_2', models.CharField(blank=True, max_length=255, null=True)),
                ('contrast_id', models.CharField(blank=True, max_length=255, null=True)),
                ('insert_tms', models.DateTimeField(auto_now_add=True)),
                ('update_tms', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'bx_station_detail',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='BxText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_id', models.IntegerField()),
                ('dashboard_id', models.IntegerField()),
                ('block_name', models.CharField(max_length=255)),
                ('data', models.CharField(max_length=255)),
                ('seq', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'bx_text',
                'managed': True,
            },
        ),
    ]