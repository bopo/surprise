# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('restful', '0053_tbkcategory_channel'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbkcategory',
            name='lft',
            field=models.PositiveIntegerField(default=1, editable=False, db_index=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tbkcategory',
            name='rght',
            field=models.PositiveIntegerField(default=0, editable=False, db_index=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tbkcategory',
            name='tree_id',
            field=models.PositiveIntegerField(default=0, editable=False, db_index=True),
            preserve_default=False,
        ),
    ]
