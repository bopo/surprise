# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('restful', '0078_auto_20160801_1128'),
    ]

    operations = [
        migrations.CreateModel(
            name='PreselectionCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64, verbose_name='\u5206\u7c7b\u540d\u79f0')),
                ('source', models.CharField(default=None, max_length=100, null=True, verbose_name='\u91c7\u96c6\u70b9', blank=True)),
                ('lft', models.PositiveIntegerField(editable=False, db_index=True)),
                ('rght', models.PositiveIntegerField(editable=False, db_index=True)),
                ('tree_id', models.PositiveIntegerField(editable=False, db_index=True)),
                ('level', models.PositiveIntegerField(editable=False, db_index=True)),
                ('parent', mptt.fields.TreeForeignKey(related_name='children', blank=True, to='restful.PreselectionCategory', null=True)),
            ],
            options={
                'verbose_name': '\u91c7\u96c6\u7c7b\u522b',
                'verbose_name_plural': '\u91c7\u96c6\u7c7b\u522b',
            },
        ),
    ]
