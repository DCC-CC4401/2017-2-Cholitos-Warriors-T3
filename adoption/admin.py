from django.contrib import admin
from adoption.models import AdoptionForm, AdoptionRequest
# Register your models here.

admin.site.register(AdoptionForm)
admin.site.register(AdoptionRequest)