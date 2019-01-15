# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restful', '0051_goodscategory_catids'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodscategory',
            name='catids',
            field=models.ForeignKey(verbose_name='\u6dd8\u5b9d\u5206\u7c7b', blank=True, to='restful.TBKCategory', null=True),
        ),
        migrations.AlterField(
            model_name='tbkcategory',
            name='count',
            field=models.IntegerField(null=True, verbose_name='count', blank=True),
        ),
        migrations.AlterField(
            model_name='tbkcategory',
            name='flag',
            field=models.CharField(max_length=100, null=True, verbose_name='\u6807\u793a', blank=True),
        ),
        migrations.AlterField(
            model_name='tbkcategory',
            name='level',
            field=models.IntegerField(null=True, verbose_name='\u5c42\u7ea7', blank=True),
        ),
        migrations.AlterField(
            model_name='tbkcategory',
            name='subIds',
            field=models.IntegerField(null=True, verbose_name='\u5b50\u7c7b', blank=True),
        ),
        migrations.AlterField(
            model_name='tbkcategory',
            name='type',
            field=models.CharField(max_length=100, null=True, verbose_name='\u7c7b\u578b', blank=True),
        ),
    ]
