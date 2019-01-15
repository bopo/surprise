# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consumer', '0002_userprofile_qrcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='qrcode',
            field=models.URLField(default='', max_length=255, verbose_name='\u4e8c\u7ef4\u7801', blank=True),
        ),
    ]
