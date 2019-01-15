# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consumer', '0014_auto_20160529_2338'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='jpush_registration_id',
            field=models.CharField(max_length=200, null=True, verbose_name='jpush_registration_id', blank=True),
        ),
    ]
