# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restful', '0083_auto_20160805_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preselectioncategory',
            name='ordering',
            field=models.IntegerField(default=999, verbose_name='\u6392\u5e8f'),
        ),
    ]
