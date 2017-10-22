from django.db import models
from django.contrib.auth.models import User, Permission, Group
from Cholito.models import ONG, Municipalidad

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
    profile_picture = models.ImageField(upload_to="users/profile_pictures")

    #Groups
    #municipalidad = models.ForeignKey(Municipalidad, blank=True, null=True) #TODO: App para Municipalidad
    #ong = models.ForeignKey(ONG, blank= True, null=True) #TODO: App para ONG

    def __unicode__(self):
        return self.user.username

    def delete(self, using = None, keep_parents = False):
        self.user.delete()
        return super(CholitoUser, self).delete(using= using, keep_parents= keep_parents)