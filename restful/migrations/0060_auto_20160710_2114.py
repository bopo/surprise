# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restful', '0059_auto_20160710_2107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbkcategory',
            name='cid',
            field=models.BigIntegerField(null=True, verbose_name='ID', blank=True),
        ),
    ]
