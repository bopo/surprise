# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consumer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='qrcode',
            field=models.ImageField(default='', upload_to=b'', max_length=255, verbose_name='\u4e8c\u7ef4\u7801', blank=True),
        ),
    ]
