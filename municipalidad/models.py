from django.db import models

# Create your models here.
class Municipalidad(models.Model):
    name = models.CharField(max_length=50)
    comuna = models.CharField(max_length=30, unique=True, null=True)

    def __str__(self):
        return self.comuna