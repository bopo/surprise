# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restful', '0100_tmc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='first',
            name='coordinate',
            field=models.CharField(max_length=200, verbose_name='\u4f4d\u7f6e\u5750\u6807', blank=True),
        ),
        migrations.AlterField(
            model_name='first',
            name='location',
            field=models.CharField(max_length=200, verbose_name='\u5730\u5740\u4fe1\u606f', blank=True),
        ),
        migrations.AlterField(
            model_name='first',
            name='screensize',
            field=models.CharField(max_length=200, verbose_name='\u5c4f\u5e55\u5c3a\u5bf8', blank=True),
        ),
    ]
