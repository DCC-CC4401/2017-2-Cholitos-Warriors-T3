from django.conf.urls import url, include, url
from . import views

urlpatterns = [
    url(r'^landing_page_out/$', views.landing_page_out, name='landing_page_out'),
    url(r'^landing_page_in/$', views.landing_page_in, name='landing_page_in'),
    url(r'^$', views.index, name='index'),
]
