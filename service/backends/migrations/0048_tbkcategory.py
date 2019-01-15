# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restful', '0047_auto_20160709_2136'),
    ]

    operations = [
        migrations.CreateModel(
            name='TBKCategory',
            fields=[
                ('id', models.BigIntegerField(serialize=False, verbose_name='ID', primary_key=True, blank=True)),
                ('name', models.CharField(max_length=100, verbose_name='\u540d\u79f0')),
                ('type', models.CharField(max_length=100, verbose_name='\u7c7b\u578b', blank=True)),
                ('flag', models.CharField(max_length=100, verbose_name='\u6807\u793a', blank=True)),
                ('level', models.IntegerField(verbose_name='\u5c42\u7ea7', blank=True)),
                ('count', models.IntegerField(verbose_name='count', blank=True)),
                ('subIds', models.IntegerField(verbose_name='\u5b50\u7c7b', blank=True)),
            ],
        ),
    ]
