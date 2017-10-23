from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from adoption.models import AdoptionForm
from . import views

app_name='adoption'

urlpatterns = [ url(r'^adopt/', views.adoptionPage, name='adopt'),
                url(r'^$', ListView.as_view(queryset=AdoptionForm.objects.all().order_by("name")[:25],
                                            template_name="adoptionlist.html")),
               ]