# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restful', '0095_auto_20160814_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='firstprize',
            name='prizegoods',
            field=models.CharField(max_length=100, null=True, verbose_name='\u5bf9\u5e94\u5956\u54c1ID', blank=True),
        ),
    ]
