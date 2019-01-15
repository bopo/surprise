# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restful', '0057_auto_20160710_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodscategory',
            name='ordering',
            field=models.PositiveIntegerField(default=999, verbose_name='\u6392\u5e8f', editable=False),
        ),
    ]
