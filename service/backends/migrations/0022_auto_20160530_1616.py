# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restful', '0021_goods_delist_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='delist_time',
            field=models.DateTimeField(null=True, verbose_name='\u4e0b\u67b6\u65f6\u95f4', blank=True),
        ),
    ]
