# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restful', '0034_auto_20160602_1605'),
    ]

    operations = [
        migrations.AddField(
            model_name='notice',
            name='registration',
            field=models.BooleanField(default=False, verbose_name='\u6ce8\u518c\u63a8\u9001\u6d88\u606f'),
        ),
    ]
