# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restful', '0061_auto_20160710_2226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodscategory',
            name='slug',
            field=models.SlugField(default='', blank=True, null=True, verbose_name='Slug'),
        ),
    ]
