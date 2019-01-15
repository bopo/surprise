# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('restful', '0056_auto_20160710_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbkcategory',
            name='parent',
            field=mptt.fields.TreeForeignKey(related_name='children', blank=True, to='restful.TBKCategory', null=True),
        ),
    ]
