# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-09-06 17:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sangue', '0004_auto_20160504_1757'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='donatore',
            options={'permissions': (('view_donatore', 'Can view Donatore di Sangue'),), 'verbose_name': 'Donatore di Sangue', 'verbose_name_plural': 'Donatori di Sangue'},
        ),
        migrations.AlterModelOptions(
            name='donazione',
            options={'permissions': (('view_donazione', 'Can view Donazione'),)},
        ),
        migrations.AlterModelOptions(
            name='merito',
            options={'permissions': (('view_merito', 'Can view Merito'),)},
        ),
        migrations.AlterModelOptions(
            name='sede',
            options={'ordering': ['regione', 'provincia', 'citta', 'nome'], 'permissions': (('view_sede', 'Can view Sede'),), 'verbose_name': 'Sede di Donazione Sangue', 'verbose_name_plural': 'Sedi di Donazione Sangue'},
        ),
    ]
