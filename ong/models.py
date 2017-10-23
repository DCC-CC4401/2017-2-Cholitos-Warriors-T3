from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ONG(models.Model):
    name = models.CharField(max_length=50)
    user = models.OneToOneField(User, null=True)
    profile_picture = models.ImageField(upload_to="municipalidad/profile_pictures", null=True)

    def __str__(self):
        return self.name