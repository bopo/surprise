# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restful', '0045_goods_ordering'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trend',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.IntegerField(default='0', verbose_name='\u5927\u76d8\u6570\u5b57\u540e\u4e09\u4f4d')),
                ('exchange', models.DateField(null=True, verbose_name='\u5151\u5956\u65f6\u95f4', blank=True)),
            ],
            options={
                'verbose_name': '\u5927\u76d8\u8d70\u52bf',
                'verbose_name_plural': '\u5927\u76d8\u8d70\u52bf',
            },
        ),
    ]
