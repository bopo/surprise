# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restful', '0081_auto_20160805_1419'),
    ]

    operations = [
        migrations.AddField(
            model_name='preselectioncategory',
            name='ordering',
            field=models.PositiveIntegerField(default=999, verbose_name='\u6392\u5e8f', editable=False),
        ),
    ]
