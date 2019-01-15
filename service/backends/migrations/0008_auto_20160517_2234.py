# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restful', '0007_goods_saved'),
    ]

    operations = [
        migrations.AddField(
            model_name='firstprize',
            name='phonemodel',
            field=models.CharField(max_length=100, null=True, verbose_name='\u624b\u673a\u578b\u53f7', blank=True),
        ),
        migrations.AlterField(
            model_name='firstprize',
            name='screensize',
            field=models.CharField(max_length=200, verbose_name='\u5c4f\u5e55\u5c3a\u5bf8', choices=[('320x480', 'iPhone 4/4S'), ('320x568', 'iPhone 5/5S/5C'), ('375x667', 'iPhone 6/6S'), ('414x736', 'iPhone 6/6S Plus')]),
        ),
    ]
