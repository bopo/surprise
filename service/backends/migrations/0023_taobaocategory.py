# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restful', '0022_auto_20160530_1616'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaobaoCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cid', models.IntegerField(default=1, verbose_name='\u6dd8\u5b9d\u5206\u7c7bID')),
                ('pid', models.IntegerField(default=1, verbose_name='\u5206\u7c7b\u7236\u7ea7')),
                ('name', models.CharField(max_length=100, null=True, verbose_name='\u5206\u7c7b\u540d\u79f0', blank=True)),
                ('type', models.CharField(max_length=100, null=True, verbose_name='\u5206\u7c7b\u7c7b\u578b', blank=True)),
                ('flag', models.CharField(max_length=100, null=True, verbose_name='\u5206\u7c7b\u6807\u793a', blank=True)),
                ('level', models.IntegerField(default=1, verbose_name='\u5206\u7c7b\u5c42\u7ea7')),
                ('is_parent', models.BooleanField(default=False, verbose_name='\u5206\u7c7b\u5c42\u7ea7')),
            ],
        ),
    ]
