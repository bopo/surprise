# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restful', '0031_description_open_iid'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='item_imgs',
            field=models.CharField(max_length=255, null=True, verbose_name='\u591a\u5f20\u56fe\u7247', blank=True),
        ),
    ]
