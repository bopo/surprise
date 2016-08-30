# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restful', '0092_auto_20160812_2327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trade',
            name='pic_url',
            field=models.URLField(default='', null=True, verbose_name='\u56fe\u7247\u7f51\u5740', blank=True),
        ),
    ]
