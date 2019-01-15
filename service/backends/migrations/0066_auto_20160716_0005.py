# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('restful', '0065_remove_collect_promotion_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='collect',
            old_name='title',
            new_name='from_name',
        ),
        migrations.RemoveField(
            model_name='collect',
            name='category',
        ),
        migrations.RemoveField(
            model_name='collect',
            name='created',
        ),
        migrations.RemoveField(
            model_name='collect',
            name='id',
        ),
        migrations.RemoveField(
            model_name='collect',
            name='modified',
        ),
        migrations.RemoveField(
            model_name='collect',
            name='pic_url',
        ),
        migrations.RemoveField(
            model_name='collect',
            name='price',
        ),
        migrations.RemoveField(
            model_name='collect',
            name='status',
        ),
        migrations.RemoveField(
            model_name='collect',
            name='status_changed',
        ),
        migrations.AddField(
            model_name='collect',
            name='goods_ptr',
            field=models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, default=None, serialize=False, to='restful.Goods'),
            preserve_default=False,
        ),
    ]
