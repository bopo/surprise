# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consumer', '0009_customuser_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='slug',
            field=models.UUIDField(verbose_name='slug', null=True, auto_created=True, blank=True),
        ),
    ]
