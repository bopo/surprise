# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restful', '0108_auto_20160907_1730'),
    ]

    operations = [
        migrations.AddField(
            model_name='affairs',
            name='shared_rule',
            field=models.CharField(max_length=20, null=True, verbose_name='\u5206\u4eab\u89c4\u5219', blank=True),
        ),
    ]
