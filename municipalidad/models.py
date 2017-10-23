from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Municipalidad(models.Model):
    name = models.CharField(max_length=50)
    comuna = models.CharField(max_length=30, unique=True)
    user = models.OneToOneField(User)
    profile_picture = models.ImageField(upload_to="municipalidad/profile_pictures")

    def __str__(self):
        return self.comuna