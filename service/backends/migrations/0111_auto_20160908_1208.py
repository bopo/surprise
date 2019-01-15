# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restful', '0110_auto_20160908_1205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='affairs',
            name='orderid',
            field=models.CharField(default='', max_length=100, null=True, verbose_name='\u6dd8\u5b9d\u8ba2\u5355', blank=True),
        ),
    ]
