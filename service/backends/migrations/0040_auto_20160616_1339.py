# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restful', '0039_auto_20160616_1326'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='queryrule',
            name='area',
        ),
        migrations.RemoveField(
            model_name='queryrule',
            name='auto_send',
        ),
        migrations.RemoveField(
            model_name='queryrule',
            name='cash_coupon',
        ),
        migrations.RemoveField(
            model_name='queryrule',
            name='onemonth_repair',
        ),
        migrations.RemoveField(
            model_name='queryrule',
            name='overseas_item',
        ),
        migrations.RemoveField(
            model_name='queryrule',
            name='real_describe',
        ),
        migrations.RemoveField(
            model_name='queryrule',
            name='sevendays_return',
        ),
        migrations.RemoveField(
            model_name='queryrule',
            name='support_cod',
        ),
        migrations.RemoveField(
            model_name='queryrule',
            name='vip_card',
        ),
    ]
