from django.db import models
from datetime import datetime

# Create your models here.

class Place (models.Model):
    ciudad = models.CharField(max_length=50)
    comuna = models.CharField(max_length=50)
    calle = models.CharField(max_length=50)
    numero = models.IntegerField()

class Denuncia (models.Model):
    kindOfAbuse = models.CharField(max_length=100)
    kindOfAnimal = models.CharField(max_length=100)
    gender = models.CharField(max_length=1)
    colour = models.CharField(max_length=20)
    hurt = models.BooleanField()
    comments = models.TextField()
    denouncedDate = models.DateField(default=datetime.now, blank=True)
    location = models.ForeignKey(Place, blank=True, null=True)