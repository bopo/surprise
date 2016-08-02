# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restful', '0067_auto_20160720_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodscategory',
            name='cover',
            field=models.ImageField(default='', upload_to='category', max_length=200, verbose_name='\u5206\u7c7b\u56fe\u7247', blank=True),
            preserve_default=False,
        ),
    ]
