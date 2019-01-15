# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restful', '0077_auto_20160801_1105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preselection',
            name='subcategory_id',
            field=models.IntegerField(null=True, verbose_name='\u91c7\u96c6\u5b50\u5206\u7c7bID', blank=True),
        ),
    ]
