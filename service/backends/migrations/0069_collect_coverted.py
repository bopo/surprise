# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restful', '0068_auto_20160720_1524'),
    ]

    operations = [
        migrations.AddField(
            model_name='collect',
            name='coverted',
            field=models.BooleanField(default=0, verbose_name='\u8f6c\u6362'),
        ),
    ]
