# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restful', '0094_auto_20160813_2236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='firstprize',
            name='prizegoods',
            field=models.IntegerField(null=True, verbose_name='\u5bf9\u5e94\u5956\u54c1ID', blank=True),
        ),
        migrations.AlterField(
            model_name='trade',
            name='price',
            field=models.DecimalField(default=0.0, help_text='\u8be5\u5546\u54c1\u7684\u4f18\u60e0\u4ef7\u683c promotion_price \u5b57\u6bb5', verbose_name='\u5355\u54c1\u4ef7\u683c', max_digits=10, decimal_places=2),
        ),
    ]
