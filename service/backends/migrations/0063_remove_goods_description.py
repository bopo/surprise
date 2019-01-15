# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restful', '0062_auto_20160711_0021'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goods',
            name='description',
        ),
    ]
