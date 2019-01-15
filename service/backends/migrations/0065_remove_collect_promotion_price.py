# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restful', '0064_collect'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collect',
            name='promotion_price',
        ),
    ]
