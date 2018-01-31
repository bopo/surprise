# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restful', '0113_auto_20160909_2210'),
    ]

    operations = [
        migrations.AddField(
            model_name='collect',
            name='source',
            field=models.CharField(max_length=255, null=True, verbose_name='\u6765\u6e90', blank=True),
        ),
        migrations.AlterField(
            model_name='collect',
            name='from_name',
            field=models.CharField(max_length=255, null=True, verbose_name='\u6765\u6e90\u6807\u9898', blank=True),
        ),
    ]
