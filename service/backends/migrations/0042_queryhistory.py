# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restful', '0041_auto_20160616_1406'),
    ]

    operations = [
        migrations.CreateModel(
            name='QueryHistory',
            fields=[
                ('goods_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='restful.Goods')),
            ],
            options={
                'verbose_name': '\u641c\u7d22\u5386\u53f2',
                'verbose_name_plural': '\u641c\u7d22\u5386\u53f2',
            },
            bases=('restful.goods',),
        ),
    ]
