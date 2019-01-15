# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restful', '0075_auto_20160801_1040'),
    ]

    operations = [
        migrations.RenameField(
            model_name='preselection',
            old_name='cid',
            new_name='subcategory_id',
        ),
        migrations.RemoveField(
            model_name='preselection',
            name='category',
        ),
        migrations.AddField(
            model_name='preselection',
            name='subcategory',
            field=models.CharField(max_length=255, null=True, verbose_name='\u91c7\u96c6\u5b50\u5206\u7c7b', blank=True),
        ),
    ]
