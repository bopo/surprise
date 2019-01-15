# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restful', '0103_auto_20160902_1352'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notice',
            name='template',
        ),
        migrations.AlterField(
            model_name='noticetemplate',
            name='category',
            field=models.CharField(default='', max_length=255, verbose_name='\u6d88\u606f\u6a21\u677f\u5206\u7c7b', choices=[('shared', '\u5206\u4eab\u5956\u52b1'), ('reward', '\u4e2d\u5956\u6d88\u606f'), ('signup', '\u6ce8\u518c\u6d88\u606f'), ('system', '\u7cfb\u7edf\u6d88\u606f'), ('payment', '\u652f\u4ed8\u6d88\u606f'), ('confirm', '\u5546\u54c1\u786e\u8ba4')]),
        ),
    ]
