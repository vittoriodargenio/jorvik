# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-09-06 17:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formazione', '0013_auto_20160302_1341'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aspirante',
            options={'permissions': (('view_aspirante', 'Can view corso aspirante'),), 'verbose_name_plural': 'Aspiranti'},
        ),
        migrations.AlterModelOptions(
            name='assenzacorsobase',
            options={'permissions': (('view_assenzacorsobase', 'Can view corso Assenza a Corso Base'),), 'verbose_name': 'Assenza a Corso Base', 'verbose_name_plural': 'Assenze ai Corsi Base'},
        ),
        migrations.AlterModelOptions(
            name='corsobase',
            options={'ordering': ['-anno', '-progressivo'], 'permissions': (('view_corsobase', 'Can view corso base'),), 'verbose_name': 'Corso Base', 'verbose_name_plural': 'Corsi Base'},
        ),
        migrations.AlterModelOptions(
            name='lezionecorsobase',
            options={'ordering': ['inizio'], 'permissions': (('view_lezionecorsobase', 'Can view corso Lezione di Corso Base'),), 'verbose_name': 'Lezione di Corso Base', 'verbose_name_plural': 'Lezioni di Corsi Base'},
        ),
        migrations.AlterModelOptions(
            name='partecipazionecorsobase',
            options={'ordering': ('persona__nome', 'persona__cognome', 'persona__codice_fiscale'), 'permissions': (('view_partecipazionecorsobarse', 'Can view corso Richiesta di partecipazione'),), 'verbose_name': 'Richiesta di partecipazione', 'verbose_name_plural': 'Richieste di partecipazione'},
        ),
    ]
