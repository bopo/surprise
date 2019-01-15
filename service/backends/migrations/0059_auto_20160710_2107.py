# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restful', '0058_auto_20160710_1849'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbkcategory',
            name='cid',
            field=models.BigIntegerField(default=0, verbose_name='ID', blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tbkcategory',
            name='id',
            field=models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True),
        ),
    ]
