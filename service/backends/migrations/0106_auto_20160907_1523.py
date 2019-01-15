# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restful', '0105_sharedrule_every'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sharedrule',
            name='every',
            field=models.CharField(default=None, max_length=100, verbose_name='\u5206\u4eab\u5468\u671f', choices=[('monthly', '\u6bcf\u6708'), ('weekly', '\u6bcf\u5468'), ('day', '\u6bcf\u5929')]),
        ),
    ]
