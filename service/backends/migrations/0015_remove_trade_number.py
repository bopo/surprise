# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restful', '0014_auto_20160519_1131'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trade',
            name='number',
        ),
    ]
