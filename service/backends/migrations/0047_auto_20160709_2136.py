# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('restful', '0046_trend'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trend',
            name='exchange',
            field=models.DateField(default=datetime.datetime(2016, 7, 9, 21, 36, 29, 695957), verbose_name='\u5151\u5956\u65f6\u95f4', unique=True, auto_created=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
