# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restful', '0084_auto_20160805_1448'),
    ]

    operations = [
        migrations.AddField(
            model_name='preselectioncategory',
            name='subcategory_id',
            field=models.IntegerField(default=0, verbose_name='\u91c7\u96c6\u5206\u7c7b'),
        ),
    ]
