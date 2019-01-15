# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restful', '0080_auto_20160804_1951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preselectioncategory',
            name='source',
            field=models.CharField(default=None, max_length=100, verbose_name='\u91c7\u96c6\u70b9', blank=True, choices=[('nanyibang', '\u7537\u8863\u90a6'), ('liwushuo', '\u793c\u7269\u8bf4')]),
        ),
    ]
