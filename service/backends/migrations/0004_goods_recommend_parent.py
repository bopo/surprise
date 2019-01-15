# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restful', '0003_auto_20160511_1504'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='recommend_parent',
            field=models.BooleanField(default=False, verbose_name='\u7236\u7c7b\u63a8\u8350'),
        ),
    ]
