# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('restful', '0010_remove_goods_saved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='first',
            name='owner',
            field=models.ForeignKey(verbose_name='\u6240\u5c5e\u7528\u6237', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
