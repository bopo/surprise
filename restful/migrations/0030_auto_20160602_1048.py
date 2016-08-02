# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restful', '0029_remove_goods_description'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Detail',
            new_name='Description',
        ),
        migrations.RemoveField(
            model_name='goods',
            name='detail',
        ),
        migrations.AddField(
            model_name='goods',
            name='description',
            field=models.OneToOneField(null=True, blank=True, to='restful.Description', verbose_name='\u8be6\u7ec6\u4fe1\u606f'),
        ),
    ]
