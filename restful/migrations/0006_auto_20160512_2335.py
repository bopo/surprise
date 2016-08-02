# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restful', '0005_remove_goods_recommend_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='cover',
            field=models.ImageField(upload_to='banner', verbose_name='\u56fe\u7247', blank=True),
        ),
        migrations.AlterField(
            model_name='goodscategory',
            name='cover',
            field=models.ImageField(upload_to='category', max_length=200, verbose_name='\u5206\u7c7b\u56fe\u7247', blank=True),
        ),
    ]
