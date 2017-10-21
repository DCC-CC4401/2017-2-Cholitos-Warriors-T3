from django.contrib.auth.forms import AuthenticationForm, UsernameField, UserCreationForm
from django.contrib.auth.models import User
from django.forms import CharField, ModelForm, inlineformset_factory
from users.models import CholitoUser

class CholitoUserSignUp(ModelForm):
    class Meta:
        model = CholitoUser

class UserCreationForm(UserCreationForm):

    class Meta:
        model = User

UserCholitoUserFormset = inlineformset_factory(User, CholitoUser, form = CholitoUserSignUp, can_delete=False)