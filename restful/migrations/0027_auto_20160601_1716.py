# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restful', '0026_auto_20160531_2125'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goodscategory',
            name='taobao',
        ),
        migrations.AddField(
            model_name='goodscategory',
            name='catids',
            field=models.CharField(help_text='\u591a\u4e2a\u7528,\u5206\u5272', max_length=100, null=True, verbose_name='\u5206\u7c7bIDs', blank=True),
        ),
        migrations.AddField(
            model_name='goodscategory',
            name='keyword',
            field=models.CharField(max_length=100, null=True, verbose_name='\u5206\u7c7b\u5173\u952e\u5b57', blank=True),
        ),
        migrations.DeleteModel(
            name='TaobaoCategory',
        ),
    ]
