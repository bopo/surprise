# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restful', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trade',
            old_name='num',
            new_name='nums',
        ),
    ]
