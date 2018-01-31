# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restful', '0104_auto_20160906_1607'),
    ]

    operations = [
        migrations.AddField(
            model_name='sharedrule',
            name='every',
            field=models.CharField(default=None, max_length=100, verbose_name='\u5468\u671f', choices=[('monthly', '\u6bcf\u6708'), ('weekly', '\u6bcf\u5468'), ('day', '\u6bcf\u5929')]),
        ),
    ]
