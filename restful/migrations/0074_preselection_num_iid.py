# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restful', '0073_auto_20160726_2036'),
    ]

    operations = [
        migrations.AddField(
            model_name='preselection',
            name='num_iid',
            field=models.BigIntegerField(null=True, verbose_name='\u6dd8\u5b9d\u771f\u5b9eID', blank=True),
        ),
    ]
