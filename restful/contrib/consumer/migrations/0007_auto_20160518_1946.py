# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consumer', '0006_customuser_uuid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='uuid',
        ),
        migrations.AddField(
            model_name='customuser',
            name='slug',
            field=models.UUIDField(default=uuid.uuid1().hex, verbose_name='slug'),
        ),
    ]
