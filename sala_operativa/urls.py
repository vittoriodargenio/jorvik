from django.conf.urls import url

from . import views


pk = "(?P<pk>[0-9]+)"

app_label = 'so'
urlpatterns = [
    url(r'^$', views.so_index, name='index'),

    # Organizza
    url(r'^organizza/$', views.so_organizza, name='organizza'),
    url(r'^organizza/(?P<pk>[0-9\-]+)/referenti/$', views.so_referenti, {"nuova": True}, name='organizza_referenti'),
    url(r'^organizza/(?P<pk>[0-9\-]+)/fatto/$', views.so_organizza_fatto, name='organizza_referenti_fatto'),

    # Gestisci
    url(r'^gestisci/$', views.so_gestisci, {"stato": "aperte"}, name='gestisci'),
    url(r'^gestisci/chiuse/$', views.so_gestisci, {"stato": "chiuse"}, name='gestisci_chiuse'),

    # Calendario
    url(r'^calendario/$', views.so_calendario, name='calendario'),
    url(r'^calendario/(?P<inizio>[0-9\-]+)/(?P<fine>[0-9\-]+)/$', views.so_calendario, name='calendario_con_range'),

    # Storico
    url(r'^storico/$', views.so_storico, name='storico'),
    url(r'^storico/excel/$', views.so_storico_excel, name='storico_excel'),
    url(r'^statistiche/$', views.so_statistiche, name='statistiche'),

    # Reperibilita
    url(r'^r/$', views.so_reperibilita, name='reperibilita'),
    url(r'^r/backup/$', views.so_reperibilita_backup, name='reperibilita_backup'),
    url(r'^r/%s/delete/$' % pk, views.so_reperibilita_cancella, name='reperibilita_cancella'),
    url(r'^r/%s/edit/$' % pk, views.so_reperibilita_edit, name='reperibilita_modifica'),

    # servizio
    url(r'^servizio/%s/$' % pk, views.so_scheda_informazioni, name='servizio'),
    url(r'^servizio/%s/cancella/$' % pk, views.so_scheda_cancella, name='servizio_cancella'),
    url(r'^servizio/%s/mappa/$' % pk, views.so_scheda_mappa, name='servizio_mappa'),
    url(r'^servizio/%s/partecipanti/$' % pk, views.so_scheda_partecipanti, name='servizio_partecipanti'),
    url(r'^servizio/%s/modifica/$' % pk, views.so_scheda_informazioni_modifica, name='servizio_modifica'),
    url(r'^servizio/%s/riapri/$' % pk, views.so_riapri, name='servizio_riapri'),
    url(r'^servizio/%s/referenti/$' % pk, views.so_referenti, name='servizio_referenti'),
    url(r'^servizio/%s/report/$' % pk, views.so_scheda_report, name='servizio_report'),

    # Turni
    url(r'^servizio/%s/turni/$' % pk, views.so_scheda_turni, name='servizio_turni'),
    url(r'^servizio/%s/turni/nuovo/$' % pk, views.so_scheda_turni_nuovo, name='servizio_turni_nuovo'),
    url(r'^servizio/%s/turni/(?P<pagina>[0-9]+)/$' % pk, views.so_scheda_turni, name='servizio_turni_pagina'),
    url(r'^servizio/%s/turni/(?P<turno_pk>[0-9]+)/partecipanti/$' % pk, views.so_scheda_turni_partecipanti, name='servizio_turni_partecipanti'),
    url(r'^servizio/%s/turni/(?P<turno_pk>[0-9]+)/partecipa/$' % pk, views.so_scheda_turni_partecipa, name='servizio_turni_partecipa'),
    url(r'^servizio/%s/turni/(?P<turno_pk>[0-9]+)/ritirati/$' % pk, views.so_scheda_turni_ritirati, name='servizio_turni_ritirati'),
    url(r'^servizio/%s/turni/permalink/(?P<turno_pk>[0-9]+)/$' % pk, views.so_scheda_turni_permalink, name='servizio_turni_link_permanente'),
    url(r'^servizio/%s/turni/cancella/(?P<turno_pk>[0-9]+)/$' % pk, views.so_scheda_turni_turno_cancella, name='servizio_turni_cancella'),
    url(r'^servizio/%s/turni/modifica/$' % pk, views.so_scheda_turni_modifica, name='servizio_turni_modifica'),
    url(r'^servizio/%s/turni/modifica/(?P<pagina>[0-9]+)/$' % pk, views.so_scheda_turni_modifica, name='servizio_turni_modifica_pagina'),
    url(r'^servizio/%s/turni/modifica/permalink/(?P<turno_pk>[0-9]+)/$' % pk, views.so_scheda_turni_modifica_permalink, name='servizio_turni_modifica_link_permanente'),

    # Partecipazione
    url(r'^servizio/%s/partecipazione/(?P<partecipazione_pk>[0-9]+)/cancella/$' % pk, views.so_scheda_partecipazione_cancella, name='servizio_partecipazione_cancella'),

    # Mezzi e materiali
    url(r'^mm/$', views.so_mezzi, name='mezzi'),
    url(r'^mm/%s/edit/$' % pk, views.so_mezzo_modifica, name='mezzo_modifica'),
    url(r'^mm/%s/delete/$' % pk, views.so_mezzo_cancella, name='mezzo_cancella'),
]
