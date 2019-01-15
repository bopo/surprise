# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restful', '0044_auto_20160630_1742'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='ordering',
            field=models.IntegerField(default=99999, verbose_name='\u6392\u5e8f'),
        ),
    ]
