# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-04-16 07:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('excel_import', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bxeverydaycontrastdata',
            name='negotiate_entry_rate',
            field=models.FloatField(default=0.5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bxperformarrange',
            name='status',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
