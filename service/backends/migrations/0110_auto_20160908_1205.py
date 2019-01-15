# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restful', '0109_affairs_shared_rule'),
    ]

    operations = [
        migrations.AlterField(
            model_name='affairs',
            name='shared_rule',
            field=models.CharField(max_length=20, null=True, verbose_name='\u5206\u4eab\u7c7b\u578b', blank=True),
        ),
    ]
