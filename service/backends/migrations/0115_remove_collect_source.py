# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restful', '0114_auto_20160910_1726'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collect',
            name='source',
        ),
    ]
