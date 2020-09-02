# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2020-09-02 12:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('anagrafica', '0066_datorelavoro_nominativo'),
    ]

    operations = [
        migrations.AddField(
            model_name='datorelavoro',
            name='persona',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='datore', to='anagrafica.Persona'),
        ),
    ]
