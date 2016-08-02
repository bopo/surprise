# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restful', '0002_auto_20160511_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trade',
            name='nums',
            field=models.IntegerField(default=1, verbose_name='\u8d2d\u4e70\u6570\u91cf', blank=True),
        ),
        migrations.AlterField(
            model_name='trade',
            name='open_iid',
            field=models.CharField(default='', max_length=200, verbose_name='\u5546\u54c1OPEN_ID'),
        ),
        migrations.AlterField(
            model_name='trade',
            name='price',
            field=models.DecimalField(default=0.0, verbose_name='\u5355\u54c1\u4ef7\u683c', max_digits=10, decimal_places=2),
        ),
    ]
