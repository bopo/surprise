# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restful', '0040_auto_20160616_1339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='queryrule',
            name='end_commission_num',
            field=models.CharField(help_text='\uff08\u4e0e\u8fd4\u56de\u6570\u636e\u4e2d\u7684commission_num\u5b57\u6bb5\u5bf9\u5e94\uff09\u4e0a\u9650.', max_length=100, null=True, verbose_name='\u6700\u9ad830\u5929\u7d2f\u8ba1\u63a8\u5e7f\u91cf', blank=True),
        ),
        migrations.AlterField(
            model_name='queryrule',
            name='end_commission_rate',
            field=models.CharField(help_text='\u5982\uff1a2345\u8868\u793a23.45%\u3002\u6ce8\uff1astart_commissionRate\u548cend_commissionRate\u4e00\u8d77\u8bbe\u7f6e\u624d\u6709\u6548\u3002', max_length=100, null=True, verbose_name='\u6700\u9ad8\u4f63\u91d1\u6bd4\u7387', blank=True),
        ),
        migrations.AlterField(
            model_name='queryrule',
            name='end_credit',
            field=models.CharField(choices=[('1heart', '\u4e00\u5fc3'), ('2heart', '\u4e24\u5fc3'), ('3heart', '\u4e09\u5fc3'), ('4heart', '\u56db\u5fc3'), ('5heart', '\u4e94\u5fc3'), ('1diamond', '\u4e00\u94bb'), ('2diamond', '\u4e24\u94bb'), ('3diamond', '\u4e09\u94bb'), ('4diamond', '\u56db\u94bb'), ('5diamond', '\u4e94\u94bb'), ('1crown', '\u4e00\u51a0'), ('2crown', '\u4e24\u51a0'), ('3crown', '\u4e09\u51a0'), ('4crown', '\u56db\u51a0'), ('5crown', '\u4e94\u51a0'), ('1goldencrown', '\u4e00\u9ec4\u51a0'), ('2goldencrown', '\u4e8c\u9ec4\u51a0'), ('3goldencrown', '\u4e09\u9ec4\u51a0'), ('4goldencrown', '\u56db\u9ec4\u51a0'), ('5goldencrown', '\u4e94\u9ec4\u51a0')], max_length=100, blank=True, help_text='\u53ef\u9009\u503c\u548cstart_credit\u4e00\u6837.start_credit\u7684\u503c\u4e00\u5b9a\u8981\u5c0f\u4e8e\u6216\u7b49\u4e8eend_credit\u7684\u503c\u3002\u6ce8\uff1aend_credit\u4e0estart_credit\u4e00\u8d77\u4f7f\u7528\u624d\u751f\u6548', null=True, verbose_name='\u6700\u9ad8\u5356\u5bb6\u4fe1\u7528'),
        ),
        migrations.AlterField(
            model_name='queryrule',
            name='start_commission_num',
            field=models.CharField(help_text='\uff08\u4e0e\u8fd4\u56de\u6570\u636e\u4e2d\u7684commission_num\u5b57\u6bb5\u5bf9\u5e94\uff09\u4e0b\u9650.\u6ce8\uff1a\u8be5\u5b57\u6bb5\u8981\u4e0eend_commissionNum\u4e00\u8d77\u4f7f\u7528\u624d\u751f\u6548', max_length=100, null=True, verbose_name='\u6700\u4f4e30\u5929\u7d2f\u8ba1\u63a8\u5e7f\u91cf'),
        ),
        migrations.AlterField(
            model_name='queryrule',
            name='start_commission_rate',
            field=models.CharField(help_text='\u5982\uff1a1234\u8868\u793a12.34%', max_length=100, null=True, verbose_name='\u6700\u4f4e\u4f63\u91d1\u6bd4\u7387', blank=True),
        ),
        migrations.AlterField(
            model_name='queryrule',
            name='start_credit',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='\u6700\u4f4e\u5356\u5bb6\u4fe1\u7528', choices=[('1heart', '\u4e00\u5fc3'), ('2heart', '\u4e24\u5fc3'), ('3heart', '\u4e09\u5fc3'), ('4heart', '\u56db\u5fc3'), ('5heart', '\u4e94\u5fc3'), ('1diamond', '\u4e00\u94bb'), ('2diamond', '\u4e24\u94bb'), ('3diamond', '\u4e09\u94bb'), ('4diamond', '\u56db\u94bb'), ('5diamond', '\u4e94\u94bb'), ('1crown', '\u4e00\u51a0'), ('2crown', '\u4e24\u51a0'), ('3crown', '\u4e09\u51a0'), ('4crown', '\u56db\u51a0'), ('5crown', '\u4e94\u51a0'), ('1goldencrown', '\u4e00\u9ec4\u51a0'), ('2goldencrown', '\u4e8c\u9ec4\u51a0'), ('3goldencrown', '\u4e09\u9ec4\u51a0'), ('4goldencrown', '\u56db\u9ec4\u51a0'), ('5goldencrown', '\u4e94\u9ec4\u51a0')]),
        ),
    ]
