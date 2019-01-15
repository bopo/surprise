# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restful', '0082_preselectioncategory_ordering'),
    ]

    operations = [
        migrations.AddField(
            model_name='preselectioncategory',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='preselectioncategory',
            name='ordering',
            field=models.IntegerField(default=999, verbose_name='\u6392\u5e8f', editable=False),
        ),
    ]
