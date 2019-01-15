# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restful', '0088_remove_firstprize_prizegoods'),
    ]

    operations = [
        migrations.AddField(
            model_name='firstprize',
            name='prizegoods',
            field=models.ForeignKey(verbose_name='\u5bf9\u5e94\u5956\u54c1', blank=True, to='restful.Goods', null=True),
        ),
    ]
