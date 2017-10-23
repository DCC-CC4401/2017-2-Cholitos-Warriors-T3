from django.conf.urls import url, include, url
from . import views

app_name ='municipalidad'

urlpatterns = [
    url(r'^estadisticasdenuncias/$', views.stats_denuncias, name='statsdenuncias'),
    url(r'^estadisticasongs/$', views.stats_fichas, name='statsongs'),
    url(r'^listadenuncias/$', views.lista_denuncias, name='fichasdenuncias')
]