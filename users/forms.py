from django.contrib.auth.forms import AuthenticationForm, UsernameField, UserCreationForm
from django.contrib.auth.models import User
from django.forms import CharField, EmailField, ModelForm, inlineformset_factory
from users.models import CholitoUser

class AuthForm(AuthenticationForm):
    email = EmailField()
    password = CharField()

class CholitoUserSignUp(ModelForm):
    class Meta:
        model = CholitoUser
        fields = '__all__'

class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)

CholitoUserFormset = inlineformset_factory(User, CholitoUser, form =CholitoUserSignUp, can_delete=False)