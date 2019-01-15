# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restful', '0008_auto_20160517_2234'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='firstprize',
            options={'verbose_name': '\u9996\u767b\u5956\u54c1', 'verbose_name_plural': '\u9996\u767b\u5956\u54c1'},
        ),
        migrations.AlterField(
            model_name='firstprize',
            name='prizegoods',
            field=models.ForeignKey(verbose_name='\u5bf9\u5e94\u5956\u54c1', to='restful.Goods'),
        ),
    ]
