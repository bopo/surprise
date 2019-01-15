# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restful', '0072_auto_20160726_2030'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='preselection',
            name='item_location',
        ),
        migrations.RemoveField(
            model_name='preselection',
            name='seller_credit_score',
        ),
        migrations.RemoveField(
            model_name='preselection',
            name='seller_id',
        ),
        migrations.AddField(
            model_name='preselection',
            name='delist_time',
            field=models.DateTimeField(null=True, verbose_name='\u4e0b\u67b6\u65f6\u95f4', blank=True),
        ),
    ]
