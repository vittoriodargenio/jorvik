from django.contrib import admin
from django.contrib.postgres.fields import JSONField

from prettyjson import PrettyJSONWidget

from base.admin import InlineAutorizzazione
from gruppi.readonly_admin import ReadonlyAdminMixin
from .models import (Titolo, TitleGoal, TitoloPersonale)


@admin.register(Titolo)
class AdminTitolo(ReadonlyAdminMixin, admin.ModelAdmin):
    search_fields = ['nome', 'sigla',]
    list_display = ('nome', 'tipo', 'is_active', 'sigla', 'cdf_livello', 'area',
        'inseribile_in_autonomia', 'expires_after', 'scheda_prevede_esame',)
    list_filter = ('is_active', 'cdf_livello', 'area', "tipo", "richiede_conferma",
        "inseribile_in_autonomia", 'goal__unit_reference', 'scheda_prevede_esame',)
    formfield_overrides = {
        JSONField: {'widget': PrettyJSONWidget}
    }

    def goal_obbiettivo_stragetico(self, obj):
        return obj.goal.unit_reference if hasattr(obj.goal,
                                    'unit_reference') else 'not set'

    def goal_propedeuticita(self, obj):
        return obj.goal.propedeuticita if hasattr(obj.goal,
                                    'propedeuticita') else 'not set'

    def goal_unit_reference(self, obj):
        return obj.goal.get_unit_reference_display() if hasattr(obj.goal,
                                    'unit_reference') else 'not set'

    goal_obbiettivo_stragetico.short_description = 'Obiettivo strategico di riferimento'
    goal_propedeuticita.short_description = 'Propedeuticità'
    goal_unit_reference.short_description = 'Unità  riferimento'


@admin.register(TitleGoal)
class AdminTitleGoal(admin.ModelAdmin):
    list_display = ['__str__', 'obbiettivo_stragetico', 'propedeuticita',
                    'unit_reference']
    list_filter = ['unit_reference',]


@admin.register(TitoloPersonale)
class AdminTitoloPersonale(ReadonlyAdminMixin, admin.ModelAdmin):
    search_fields = ["titolo__nome", "persona__nome", "persona__cognome",
                     "persona__codice_fiscale",]
    list_display = ("titolo", "persona", 'is_course_title',
                    "data_ottenimento", 'data_scadenza', "certificato",
                    "creazione", 'corso_partecipazione__corso')
    list_filter = ("titolo__tipo", "creazione", "data_ottenimento",
                   'is_course_title')
    raw_id_fields = ("persona", "certificato_da", "titolo", 'corso_partecipazione',)
    inlines = [InlineAutorizzazione]

    def corso_partecipazione__corso(self, obj):
        return obj.corso_partecipazione.corso \
            if hasattr(obj.corso_partecipazione, 'corso') else ''
    corso_partecipazione__corso.short_description = 'Corso Partecipazione'
