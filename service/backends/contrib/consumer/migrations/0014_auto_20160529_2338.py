# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consumer', '0013_auto_20160529_1149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='qrcode',
            field=models.ImageField(upload_to='qrcode', verbose_name='\u4e8c\u7ef4\u7801'),
        ),
    ]
