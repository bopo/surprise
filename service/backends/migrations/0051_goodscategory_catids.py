# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restful', '0050_remove_goodscategory_catids'),
    ]

    operations = [
        migrations.AddField(
            model_name='goodscategory',
            name='catids',
            field=models.ForeignKey(verbose_name='\u5206\u7c7bIDs', blank=True, to='restful.TBKCategory', null=True),
        ),
    ]
