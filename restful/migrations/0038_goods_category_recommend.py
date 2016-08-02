# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restful', '0037_auto_20160613_1147'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='category_recommend',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='\u5206\u7c7b\u63a8\u8350', choices=[('1', '\u7537\u4eba'), ('2', '\u5973\u4eba'), ('90', '\u6f6e\u7ae5')]),
        ),
    ]
