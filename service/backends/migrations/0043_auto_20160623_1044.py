# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restful', '0042_queryhistory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='coordinate',
            field=models.CharField(default='', max_length=200, verbose_name='\u4f4d\u7f6e\u5750\u6807'),
        ),
    ]
