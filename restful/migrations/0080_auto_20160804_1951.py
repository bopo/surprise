# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restful', '0079_preselectioncategory'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='preselectioncategory',
            options={'verbose_name': '\u91c7\u96c6\u7c7b\u522b\u5173\u8054', 'verbose_name_plural': '\u91c7\u96c6\u7c7b\u522b\u5173\u8054'},
        ),
        migrations.AddField(
            model_name='preselectioncategory',
            name='category',
            field=models.ForeignKey(verbose_name='\u5546\u54c1\u5206\u7c7b', to='restful.GoodsCategory', null=True),
        ),
    ]
