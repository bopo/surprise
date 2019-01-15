# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restful', '0085_preselectioncategory_subcategory_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='firstprize',
            name='phonebrand',
            field=models.CharField(max_length=100, null=True, verbose_name='\u624b\u673a\u54c1\u724c', blank=True),
        ),
    ]
