# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restful', '0107_auto_20160907_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sharedrule',
            name='every',
            field=models.CharField(default=None, choices=[('monthly', '\u6bcf\u6708'), ('weekly', '\u6bcf\u5468'), ('day', '\u6bcf\u5929')], max_length=100, blank=True, help_text='\u8bbe\u7f6e\u8be5\u9879,\u5f00\u59cb\u65f6\u95f4\u8fc7\u671f\u65f6\u95f4\u4e0d\u8d77\u4f5c\u7528', null=True, verbose_name='\u5206\u4eab\u5468\u671f'),
        ),
        migrations.AlterField(
            model_name='sharedrule',
            name='price',
            field=models.FloatField(default='0.00', help_text='\u6bcf\u6b21\u5956\u52b1\u91d1\u989d', verbose_name='\u5956\u52b1\u91d1\u989d'),
        ),
    ]
