from django.db import models


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

    name = models.CharField(max_length=20)
    type = models.CharField(max_length=20)
    gender = models.CharField(max_length=10)
    in_adoption_from = models.DateTimeField()
    description = models.TextField(max_length=140)
    adopted = models.BooleanField(False)

    def __str__(self):
        return self.name + ", "+ self.type

