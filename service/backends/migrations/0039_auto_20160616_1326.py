# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restful', '0038_goods_category_recommend'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='queryrule',
            name='cid',
        ),
        migrations.RemoveField(
            model_name='queryrule',
            name='keyword',
        ),
        migrations.RemoveField(
            model_name='queryrule',
            name='page_no',
        ),
        migrations.RemoveField(
            model_name='queryrule',
            name='page_size',
        ),
    ]
