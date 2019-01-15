# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restful', '0071_preselection'),
    ]

    operations = [
        migrations.AddField(
            model_name='preselection',
            name='cid',
            field=models.IntegerField(null=True, verbose_name='\u6dd8\u5b9d\u5206\u7c7bID', blank=True),
        ),
        migrations.AddField(
            model_name='preselection',
            name='commission',
            field=models.CharField(max_length=255, null=True, verbose_name='\u6dd8\u5b9d\u5ba2\u4f63\u91d1', blank=True),
        ),
        migrations.AddField(
            model_name='preselection',
            name='commission_num',
            field=models.CharField(max_length=255, null=True, verbose_name='\u7d2f\u8ba1\u6210\u4ea4\u91cf', blank=True),
        ),
        migrations.AddField(
            model_name='preselection',
            name='commission_rate',
            field=models.CharField(max_length=255, null=True, verbose_name='\u6dd8\u5b9d\u5ba2\u4f63\u91d1\u6bd4\u7387', blank=True),
        ),
        migrations.AddField(
            model_name='preselection',
            name='commission_volume',
            field=models.CharField(max_length=255, null=True, verbose_name='\u7d2f\u8ba1\u603b\u652f\u51fa\u4f63\u91d1\u91cf', blank=True),
        ),
        migrations.AddField(
            model_name='preselection',
            name='item_location',
            field=models.CharField(max_length=100, null=True, verbose_name='\u5546\u54c1\u6240\u5728\u5730', blank=True),
        ),
        migrations.AddField(
            model_name='preselection',
            name='nick',
            field=models.CharField(max_length=100, null=True, verbose_name='\u5356\u5bb6\u6635\u79f0', blank=True),
        ),
        migrations.AddField(
            model_name='preselection',
            name='pic_url',
            field=models.URLField(max_length=255, null=True, verbose_name='\u56fe\u7247url', blank=True),
        ),
        migrations.AddField(
            model_name='preselection',
            name='price',
            field=models.DecimalField(null=True, verbose_name='\u4ef7\u683c', max_digits=10, decimal_places=2, blank=True),
        ),
        migrations.AddField(
            model_name='preselection',
            name='promotion_price',
            field=models.CharField(max_length=255, null=True, verbose_name='\u4fc3\u9500\u4ef7\u683c', blank=True),
        ),
        migrations.AddField(
            model_name='preselection',
            name='seller_credit_score',
            field=models.IntegerField(null=True, verbose_name='\u5356\u5bb6\u4fe1\u7528\u7b49\u7ea7', blank=True),
        ),
        migrations.AddField(
            model_name='preselection',
            name='seller_id',
            field=models.IntegerField(null=True, verbose_name='\u5356\u5bb6ID', blank=True),
        ),
        migrations.AddField(
            model_name='preselection',
            name='shop_type',
            field=models.CharField(default='C', max_length=2, null=True, verbose_name='\u5e97\u94fa\u7c7b\u578b:B(\u5546\u57ce),C(\u96c6\u5e02)', blank=True),
        ),
        migrations.AddField(
            model_name='preselection',
            name='source',
            field=models.CharField(default=None, max_length=100, null=True, verbose_name='\u91c7\u96c6\u70b9', blank=True),
        ),
        migrations.AddField(
            model_name='preselection',
            name='title',
            field=models.CharField(max_length=255, null=True, verbose_name='\u6807\u9898', blank=True),
        ),
        migrations.AddField(
            model_name='preselection',
            name='volume',
            field=models.CharField(max_length=255, null=True, verbose_name='30\u5929\u5185\u4ea4\u6613\u91cf', blank=True),
        ),
    ]
