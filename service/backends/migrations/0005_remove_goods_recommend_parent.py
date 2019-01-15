# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restful', '0004_goods_recommend_parent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goods',
            name='recommend_parent',
        ),
    ]
