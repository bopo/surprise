# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restful', '0087_first_phonebrand'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='firstprize',
            name='prizegoods',
        ),
    ]
