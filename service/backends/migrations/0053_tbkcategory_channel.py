# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restful', '0052_auto_20160710_1205'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbkcategory',
            name='channel',
            field=models.CharField(max_length=100, null=True, verbose_name='\u9891\u9053', blank=True),
        ),
    ]
