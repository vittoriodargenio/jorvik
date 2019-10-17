# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2018-12-04 15:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('anagrafica', '0049_auto_20181028_1639'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(default=True)),
                ('required', models.BooleanField(default=True, verbose_name='Obbligatorio')),
            ],
            options={
                'verbose_name': 'Domanda',
                'verbose_name_plural': 'Domande',
            },
        ),
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('text', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Questionario di gradimento',
                'verbose_name_plural': 'Questionari di gradimento',
            },
        ),
        migrations.CreateModel(
            name='SurveyResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('response', models.TextField(blank=True, max_length=1000, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey.Question')),
                ('survey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey.Survey')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='anagrafica.Persona')),
            ],
            options={
                'verbose_name': "Risposta dell'utente",
                'verbose_name_plural': 'Risposte degli utenti',
            },
        ),
        migrations.AddField(
            model_name='question',
            name='survey',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey.Survey'),
        ),
    ]
