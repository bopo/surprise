# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restful', '0032_goods_item_imgs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='item_imgs',
            field=models.TextField(max_length=255, null=True, verbose_name='\u591a\u5f20\u56fe\u7247', blank=True),
        ),
    ]
