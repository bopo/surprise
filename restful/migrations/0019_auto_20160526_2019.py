# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restful', '0018_auto_20160526_1159'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='firstprize',
            name='prizegoods',
        ),
        # migrations.AddField(
        #     model_name='firstprize',
        #     name='prizegoods',
        #     field=models.ForeignKey(default=1, verbose_name='\u5bf9\u5e94\u5956\u54c1', to='restful.Goods'),
        #     preserve_default=False,
        # ),
    ]
