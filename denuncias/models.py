from django.db import models
from datetime import datetime

# Create your models here.

estado = {"reportada": 0,
          "consolidada": 1,
          "verificada": 2,
          "cerrada": 3,
          "desechada": 4}

class Place (models.Model):
    ciudad = models.CharField(max_length=50)
    comuna = models.CharField(max_length=50, default="desconocido")
    calle = models.CharField(max_length=50)
    numero = models.IntegerField()

    def __str__(self):
        return self.calle + " " + str(self.numero) + ", " + self.comuna

class Denuncia (models.Model):

    kindOfAbuse = models.CharField(max_length=100)
    kindOfAnimal = models.CharField(max_length=100)
    gender = models.CharField(max_length=1)
    colour = models.CharField(max_length=20)
    hurt = models.BooleanField()
    comments = models.TextField()
    denouncedDate = models.DateField(default=datetime.now, blank=True)
    location = models.ForeignKey(Place, on_delete=models.CASCADE, null=True) #models.ManyToOneRel(field_name=id, to=Place)

    actual_state = models.CharField(max_length=15, default="reportada")

    def __str__(self):
        return "Denuncia #" + str(self.id) + ", " + self.location.comuna + " (" + self.actual_state + ")"