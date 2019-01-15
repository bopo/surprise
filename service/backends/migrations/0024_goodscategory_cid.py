# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restful', '0023_taobaocategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='goodscategory',
            name='cid',
            field=models.ManyToManyField(to='restful.TaobaoCategory'),
        ),
    ]
