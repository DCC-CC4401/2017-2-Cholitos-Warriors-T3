from django.conf.urls import url, include, url
from . import views

app_name ='municipalidad'

urlpatterns = [
    url(r'^estadisticasdenuncias/$', views.ListaDenuncias.as_view(), name='statsdenuncias'),
    url(r'^estadisticasongs/$', views.stats_fichas, name='statsongs'),
    url(r'^listadenuncias/$', views.denuncias_recibidas, name='fichasdenuncias')
]