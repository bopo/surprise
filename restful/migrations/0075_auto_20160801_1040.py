# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restful', '0074_preselection_num_iid'),
    ]

    operations = [
        migrations.AddField(
            model_name='preselection',
            name='category',
            field=models.CharField(max_length=255, null=True, verbose_name='\u5206\u7c7b', blank=True),
        ),
        migrations.AlterField(
            model_name='preselection',
            name='cid',
            field=models.IntegerField(null=True, verbose_name='\u91c7\u96c6\u5206\u7c7bID', blank=True),
        ),
    ]
