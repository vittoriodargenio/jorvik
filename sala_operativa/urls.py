from django.conf.urls import url
from . import views as so_views


app_label = 'so'
urlpatterns = [
    url(r'^$', so_views.sala_operativa_index, name='index'),
    url(r'^r/$', so_views.sala_operativa_reperibilita, name='reperibilita'),
    url(r'^r/backup/$', so_views.sala_operativa_reperibilita_backup, name='reperibilita_backup'),
    url(r'^r/(?P<r_pk>[0-9]+)/delete/$', so_views.sala_operativa_reperibilita_cancella, name='reperibilita_cancella'),
    url(r'^r/(?P<r_pk>[0-9]+)/edit/$', so_views.sala_operativa_reperibilita_edit, name='reperibilita_modifica'),
    url(r'^t/$', so_views.sala_operativa_turni, name='turni'),
    url(r'^p/$', so_views.sala_operativa_poteri, name='poteri'),
]
