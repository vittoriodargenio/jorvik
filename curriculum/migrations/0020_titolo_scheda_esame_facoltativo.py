# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2019-09-16 12:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0019_titolo_scheda_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='titolo',
            name='scheda_esame_facoltativo',
            field=models.BooleanField(default=False, verbose_name='Esame facoltativo'),
        ),
    ]
