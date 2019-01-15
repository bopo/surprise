# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restful', '0097_auto_20160814_1559'),
    ]

    operations = [
        migrations.AddField(
            model_name='trade',
            name='confirmed',
            field=models.DateTimeField(default=None, null=True, verbose_name='\u6dd8\u5b9d\u8ba2\u5355\u786e\u8ba4\u65f6\u95f4', blank=True),
        ),
        migrations.AlterField(
            model_name='noticetemplate',
            name='category',
            field=models.CharField(default='', max_length=255, verbose_name='\u6d88\u606f\u6a21\u677f\u5206\u7c7b', choices=[('reward', '\u4e2d\u5956\u6d88\u606f'), ('signup', '\u6ce8\u518c\u6d88\u606f'), ('system', '\u7cfb\u7edf\u6d88\u606f'), ('payment', '\u652f\u4ed8\u6d88\u606f')]),
        ),
    ]
