# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2019-05-29 15:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formazione', '0040_auto_20190524_1411'),
    ]

    operations = [
        migrations.AddField(
            model_name='corsofile',
            name='download_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
