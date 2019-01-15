# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restful', '0048_tbkcategory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goodscategory',
            name='catids',
        ),
        migrations.AddField(
            model_name='goodscategory',
            name='catids',
            field=models.ManyToManyField(to='restful.TBKCategory', verbose_name='\u5206\u7c7bIDs'),
        ),
    ]
