# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restful', '0036_auto_20160613_1115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='firstprize',
            name='coordinate',
            field=models.CharField(max_length=200, null=True, verbose_name='\u4f4d\u7f6e\u5750\u6807', blank=True),
        ),
        migrations.AlterField(
            model_name='firstprize',
            name='location',
            field=models.CharField(max_length=200, null=True, verbose_name='\u5730\u5740\u4fe1\u606f', blank=True),
        ),
    ]
