# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restful', '0015_remove_trade_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='trade',
            name='number',
            field=models.CharField(default=0, max_length=10, null=True, verbose_name='\u968f\u673a\u53f7\u7801', blank=True),
        ),
    ]
