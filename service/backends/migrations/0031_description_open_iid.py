# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restful', '0030_auto_20160602_1048'),
    ]

    operations = [
        migrations.AddField(
            model_name='description',
            name='open_iid',
            field=models.CharField(max_length=100, null=True, verbose_name='\u6dd8\u5b9dID', blank=True),
        ),
    ]
