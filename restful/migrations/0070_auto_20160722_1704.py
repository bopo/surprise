# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restful', '0069_collect_coverted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shared',
            name='open_iid',
            field=models.CharField(default='', help_text='\u975e\u5fc5\u987b,\u53ef\u4ee5\u4e3a\u7a7a', max_length=100, verbose_name='\u5546\u54c1\u5f00\u653eID'),
        ),
        migrations.AlterField(
            model_name='shared',
            name='title',
            field=models.CharField(help_text='\u975e\u5fc5\u987b,\u53ef\u4ee5\u4e3a\u7a7a', max_length=200, verbose_name='\u5546\u54c1\u6807\u9898', blank=True),
        ),
    ]
