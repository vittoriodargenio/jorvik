# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2019-07-30 14:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formazione', '0045_partecipazionecorsobase_esaminato_seconda_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='corsobase',
            name='commissione_esame_file',
            field=models.FileField(blank=True, null=True, upload_to='courses/commissione_esame', verbose_name='Commissione esame delibera'),
        ),
        migrations.AddField(
            model_name='corsobase',
            name='commissione_esame_names',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Commissione esame nomi'),
        ),
    ]
