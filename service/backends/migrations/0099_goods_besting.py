# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restful', '0098_auto_20160815_2044'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='besting',
            field=models.BooleanField(default=False, verbose_name='\u662f\u5426"\u60ca"\u63a8\u8350'),
        ),
    ]
