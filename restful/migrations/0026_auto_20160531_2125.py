# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restful', '0025_remove_taobaocategory_cid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goodscategory',
            name='cid',
        ),
        migrations.AddField(
            model_name='goodscategory',
            name='taobao',
            field=models.ForeignKey(blank=True, to='restful.TaobaoCategory', null=True),
        ),
    ]
