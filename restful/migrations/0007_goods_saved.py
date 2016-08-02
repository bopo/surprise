# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restful', '0006_auto_20160512_2335'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='saved',
            field=models.DecimalField(decimal_places=2, default='0.00', max_digits=10, blank=True, null=True, verbose_name='\u8282\u7701\u4ef7\u683c'),
        ),
    ]
