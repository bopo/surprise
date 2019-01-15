# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restful', '0096_auto_20160814_1539'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='noticetemplate',
            options={'verbose_name': '\u6d88\u606f\u6a21\u677f', 'verbose_name_plural': '\u6d88\u606f\u6a21\u677f'},
        ),
        migrations.RemoveField(
            model_name='noticetemplate',
            name='slug',
        ),
        migrations.AddField(
            model_name='noticetemplate',
            name='category',
            field=models.CharField(default='', max_length=255, verbose_name='\u6d88\u606f\u6a21\u677f\u5206\u7c7b'),
        ),
    ]
