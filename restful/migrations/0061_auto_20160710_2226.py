# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restful', '0060_auto_20160710_2114'),
    ]

    operations = [
        migrations.AddField(
            model_name='goodscategory',
            name='channel',
            field=models.CharField(max_length=100, null=True, verbose_name='\u9891\u9053', blank=True),
        ),
        migrations.AlterField(
            model_name='goodscategory',
            name='catids',
            field=models.BigIntegerField(null=True, verbose_name='\u6dd8\u5b9d\u5206\u7c7b', blank=True),
        ),
    ]
