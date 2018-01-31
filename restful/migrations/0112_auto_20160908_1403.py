# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restful', '0111_auto_20160908_1208'),
    ]

    operations = [
        migrations.CreateModel(
            name='SharePrompt',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField(verbose_name='\u5206\u4eab\u63d0\u793a')),
            ],
        ),
        migrations.AlterField(
            model_name='goods',
            name='price',
            field=models.DecimalField(null=True, verbose_name='\u539f\u4ef7\u683c', max_digits=10, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='goods',
            name='promotion_price',
            field=models.CharField(max_length=255, null=True, verbose_name='\u4fc3\u9500\u4ef7', blank=True),
        ),
    ]
