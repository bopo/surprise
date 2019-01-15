# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restful', '0112_auto_20160908_1403'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sharedrule',
            name='every',
        ),
        migrations.RemoveField(
            model_name='sharedrule',
            name='number',
        ),
        migrations.AddField(
            model_name='sharedrule',
            name='dayly',
            field=models.IntegerField(default=None, null=True, verbose_name='\u6bcf\u65e5\u6b21\u6570', blank=True),
        ),
        migrations.AddField(
            model_name='sharedrule',
            name='monthly',
            field=models.IntegerField(default=None, null=True, verbose_name='\u6bcf\u6708\u6b21\u6570', blank=True),
        ),
        migrations.AddField(
            model_name='sharedrule',
            name='reg_end_date',
            field=models.DateField(null=True, verbose_name='\u6ce8\u518c\u7ed3\u675f\u65f6\u95f4', blank=True),
        ),
        migrations.AddField(
            model_name='sharedrule',
            name='reg_start_date',
            field=models.DateField(null=True, verbose_name='\u6ce8\u518c\u5f00\u59cb\u65f6\u95f4', blank=True),
        ),
        migrations.AddField(
            model_name='sharedrule',
            name='weekly',
            field=models.IntegerField(default=None, null=True, verbose_name='\u6bcf\u5468\u6b21\u6570', blank=True),
        ),
        migrations.AlterField(
            model_name='sharedrule',
            name='price',
            field=models.FloatField(default='0.00', help_text='\u6bcf\u6b21\u5956\u52b1\u91d1\u989d', verbose_name='\u6bcf\u6b21\u5956\u52b1'),
        ),
    ]
