# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('restful', '0099_goods_besting'),
    ]

    operations = [
        migrations.CreateModel(
            name='TMC',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('orderid', models.CharField(default='', unique=True, max_length=200, verbose_name='\u6dd8\u5b9d\u8ba2\u5355')),
            ],
            options={
                'verbose_name': '\u6dd8\u5b9d\u8ba2\u5355\u786e\u8ba4\u8bb0\u5f55',
                'verbose_name_plural': '\u6dd8\u5b9d\u8ba2\u5355\u786e\u8ba4\u8bb0\u5f55',
            },
        ),
    ]
