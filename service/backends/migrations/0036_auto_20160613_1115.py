# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('restful', '0035_notice_registration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='owner',
            field=models.ForeignKey(verbose_name='\u63a8\u9001\u7ed9\u7528\u6237', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='notice',
            name='registration',
            field=models.BooleanField(default=False, help_text='\u6ce8\u518c\u6210\u529f\u540e\u53d1\u9001\u7684\u6d88\u606f,\u53ea\u80fd\u6709\u4e00\u6761. \u7528\u6237\u8bbe\u7f6e\u4e3a\u7a7a, \u5fc5\u987b\u4e3a\u7f6e\u9876', verbose_name='\u6ce8\u518c\u6210\u529f\u63a8\u9001\u7684\u6d88\u606f'),
        ),
    ]
