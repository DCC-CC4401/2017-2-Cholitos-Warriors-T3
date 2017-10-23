from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class AdoptionForm (models.Model):
    """
        AdoptionForm model.
        It has:
        - name
        - date from it is in adoption
        - type of animal
        - gender
        - description
        - if the animal's been adopted or not
    """

    name = models.CharField(max_length=20, default='pedro')
    type = models.CharField(max_length=20)
    gender = models.CharField(max_length=10)
    in_adoption_from = models.DateTimeField()
    description = models.TextField(max_length=140)
    adopted = models.BooleanField(False)
    picture_location = models.CharField(max_length=100)
    age = models.IntegerField()
    adoptionRequests = models.IntegerField()
    comments = models.TextField()

    def __str__(self):
        return self.name + ", "+ self.type

class AdoptionRequest(models.Model):
    user = models.ForeignKey(User, blank=True, null=True)
    animal = models.ForeignKey(AdoptionForm, blank=True, null=True)