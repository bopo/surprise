# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restful', '0115_remove_collect_source'),
    ]

    operations = [
        migrations.AddField(
            model_name='shared',
            name='effective',
            field=models.BooleanField(default=False, verbose_name='\u5df2\u7ecf\u6fc0\u6d3b'),
        ),
    ]
