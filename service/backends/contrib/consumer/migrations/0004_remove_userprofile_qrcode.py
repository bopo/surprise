# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consumer', '0003_auto_20160517_1940'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='qrcode',
        ),
    ]
