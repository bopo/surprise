# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restful', '0116_shared_effective'),
    ]

    operations = [
        migrations.AddField(
            model_name='goodscategory',
            name='total',
            field=models.IntegerField(default=0, null=True, verbose_name='\u5546\u54c1\u6570', blank=True),
        ),
    ]
