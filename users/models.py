from django.db import models
from django.contrib.auth.models import User, Permission, Group
from Cholito.models import ONG
from municipalidad.models import Municipalidad

class CholitoUser (models.Model):
    """
    CholitoUser model.
    Base Model for all users, user model from django.
    It has:
    - usermane
    - password
    - email
    - first_name
    - last_name
    """

    user = models.OneToOneField(User)
    profile_picture = models.ImageField(upload_to="usuarios")

    #Groups
    #municipalidad = models.ForeignKey(Municipalidad, blank=True, null=True) #TODO: App para Municipalidad
    #ong = models.ForeignKey(ONG, blank= True, null=True) #TODO: App para ONG

    def __str__(self):
        return self.user.username

    def delete(self, using = None, keep_parents = False):
        self.user.delete()
        return super(CholitoUser, self).delete(using= using, keep_parents= keep_parents)