# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restful', '0017_auto_20160522_1253'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='discount',
            options={'verbose_name': '\u4e2d\u5956\u6bd4\u7387', 'verbose_name_plural': '\u4e2d\u5956\u6bd4\u7387'},
        ),
        migrations.AddField(
            model_name='collectwebsite',
            name='category',
            field=models.ForeignKey(blank=True, to='restful.GoodsCategory', null=True),
        ),
        migrations.AlterField(
            model_name='discount',
            name='discount',
            field=models.DecimalField(default='0.00', verbose_name='\u4e2d\u5956\u6bd4\u7387', max_digits=10, decimal_places=2),
        ),
        migrations.RemoveField(
            model_name='firstprize',
            name='prizegoods',
        ),
        migrations.AddField(
            model_name='firstprize',
            name='prizegoods',
            field=models.ManyToManyField(to='restful.Goods', verbose_name='\u5bf9\u5e94\u5956\u54c1'),
        ),
    ]
