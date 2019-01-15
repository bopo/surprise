# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('restful', '0066_auto_20160716_0005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodscategory',
            name='cover',
            field=imagekit.models.fields.ProcessedImageField(upload_to='category', null=True, verbose_name='\u5206\u7c7b\u56fe\u7247'),
        ),
    ]
