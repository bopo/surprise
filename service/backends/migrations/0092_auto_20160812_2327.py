# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restful', '0091_firstprize_phonebrand'),
    ]

    operations = [
        migrations.CreateModel(
            name='NoticeTemplate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.CharField(default='', max_length=255, verbose_name='\u6d88\u606f\u6a21\u677f\u6807\u793a')),
                ('subject', models.CharField(default='', max_length=255, verbose_name='\u6d88\u606f\u6a21\u677f\u6807\u9898')),
                ('content', models.TextField(default='', verbose_name='\u6d88\u606f\u6a21\u677f\u6b63\u6587')),
            ],
        ),
        migrations.AddField(
            model_name='first',
            name='phonemodel',
            field=models.CharField(max_length=100, null=True, verbose_name='\u624b\u673a\u578b\u53f7', blank=True),
        ),
    ]
