from django.conf.urls import url, include, url
from . import views

urlpatterns = [
    url(r'^$', views.denuncia, name='landingpage'),
    url(r'^listadenuncias/$', views.denuncias_municipalidad, name='denuncias')
]