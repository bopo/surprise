# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restful', '0012_trade_rebate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trade',
            name='open_iid',
            field=models.CharField(default='', help_text='\u6dd8\u5b9d\u5f00\u653e\u5e73\u53f0\u7684 open_iid', max_length=200, verbose_name='\u6dd8\u5b9d\u5546\u54c1ID'),
        ),
        migrations.AlterField(
            model_name='trade',
            name='rebate',
            field=models.FloatField(help_text='\u533a\u5206\u662f\u968f\u673a\u6570,\u8fd8\u662f\u6298\u6263\u5546\u54c1, \u6570\u503c\u4e3a\u6298\u6263\u7684\u6bd4\u4f8b,\u4f8b\u5982: 0.9 \u4ee3\u8868\u4e5d\u6298, \u7a7a\u5219\u4e3a\u968f\u673a\u6570\u5546\u54c1', null=True, verbose_name='\u56de\u6263\u7387', blank=True),
        ),
    ]
