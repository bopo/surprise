# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restful', '0011_auto_20160518_2205'),
    ]

    operations = [
        migrations.AddField(
            model_name='trade',
            name='rebate',
            field=models.FloatField(null=True, verbose_name='\u56de\u6263\u7387', blank=True),
        ),
    ]
