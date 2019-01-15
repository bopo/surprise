# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restful', '0101_auto_20160816_1612'),
    ]

    operations = [
        migrations.AddField(
            model_name='trade',
            name='extra',
            field=models.CharField(default='', max_length=100, null=True, verbose_name='\u6dd8\u5b9d\u8ba2\u5355\u989d\u5916\u6d88\u606f', blank=True),
        ),
        migrations.AddField(
            model_name='trade',
            name='order_status',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='\u6dd8\u5b9d\u8ba2\u5355\u72b6\u6001', choices=[('2', '\u4ed8\u6b3e\u6210\u529f'), ('7', '\u4e0b\u5355\u672a\u4ed8\u6b3e'), ('6', '\u786e\u8ba4\u6536\u8d27\u540e'), ('4', '\u9000\u6b3e\u540e\u4ea4\u6613\u5173\u95ed'), ('8', '\u521b\u5efa\u8ba2\u5355\u540e\u4ea4\u6613\u5173\u95ed')]),
        ),
    ]
