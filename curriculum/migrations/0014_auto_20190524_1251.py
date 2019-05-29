# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2019-05-24 12:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0013_titolo_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='titlegoal',
            name='unit_reference',
            field=models.CharField(blank=True, choices=[('1', 'Salute'), ('2', 'Inclusione Sociale'), ('3', 'Emergenza'), ('4', 'Principi e Valori'), ('5', 'Giovani'), ('6', 'Sviluppo Organizzativo'), ('7', 'Migrazioni'), ('8', 'Cooperazione Internazionale')], max_length=3, null=True, verbose_name='Unità riferimento'),
        ),
        migrations.AlterField(
            model_name='titolo',
            name='area',
            field=models.CharField(blank=True, choices=[('1', 'Salute'), ('2', 'Inclusione Sociale'), ('3', 'Emergenza'), ('4', 'Principi e Valori'), ('5', 'Giovani'), ('6', 'Sviluppo Organizzativo'), ('7', 'Migrazioni'), ('8', 'Cooperazione Internazionale')], db_index=True, max_length=5, null=True),
        ),
    ]
