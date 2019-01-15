# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restful', '0013_auto_20160519_1013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trade',
            name='number',
            field=models.IntegerField(default=0, null=True, verbose_name='\u968f\u673a\u53f7\u7801', blank=True),
        ),
    ]
