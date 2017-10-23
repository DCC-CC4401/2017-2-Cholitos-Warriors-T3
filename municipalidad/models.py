from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Municipalidad(models.Model):
    name = models.CharField(max_length=50)
    comuna = models.CharField(max_length=30, unique=True, default="desconocido")
    user = models.OneToOneField(User, null=True)
    profile_picture = models.ImageField(null=True)#upload_to=""

    def __str__(self):
        return self.comuna