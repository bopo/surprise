# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restful', '0049_auto_20160710_1135'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goodscategory',
            name='catids',
        ),
    ]
