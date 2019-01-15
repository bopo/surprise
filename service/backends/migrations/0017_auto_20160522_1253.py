# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('restful', '0016_trade_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='cover',
            field=imagekit.models.fields.ProcessedImageField(help_text='\u56fe\u7247\u5c3a\u5bf8\u6700\u597d\u4e3a720x240', upload_to='banner', null=True, verbose_name='\u56fe\u7247'),
        ),
    ]
