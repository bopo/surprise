# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restful', '0027_auto_20160601_1716'),
    ]

    operations = [
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField(verbose_name='\u63cf\u8ff0\u4fe1\u606f')),
            ],
        ),
        migrations.AddField(
            model_name='goods',
            name='cid',
            field=models.IntegerField(null=True, verbose_name='\u6dd8\u5b9d\u5206\u7c7bID', blank=True),
        ),
        migrations.AlterField(
            model_name='goods',
            name='shop_type',
            field=models.CharField(default='C', max_length=2, null=True, verbose_name='\u5e97\u94fa\u7c7b\u578b:B(\u5546\u57ce),C(\u96c6\u5e02)', blank=True),
        ),
        migrations.AddField(
            model_name='goods',
            name='detail',
            field=models.OneToOneField(null=True, blank=True, to='restful.Detail'),
        ),
    ]
