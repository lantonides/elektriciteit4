# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-10 13:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bereken', '0003_kosten_datum'),
    ]

    operations = [
        migrations.AddField(
            model_name='kosten',
            name='product',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
