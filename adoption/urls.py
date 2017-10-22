from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from adoption.models import AdoptionForm

urlpatterns = [url(r'^$', ListView.as_view(queryset=AdoptionForm.objects.all().order_by("name")[:25],
                                            template_name="adoptionlist.html")),
               ]