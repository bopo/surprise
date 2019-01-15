# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('restful', '0055_tbkcategory_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbkcategory',
            name='parent',
            field=mptt.fields.TreeForeignKey(related_name='child', blank=True, to='restful.TBKCategory', null=True),
        ),
    ]
