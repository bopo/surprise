# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consumer', '0010_auto_20160519_1409'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='slug',
        ),
    ]
