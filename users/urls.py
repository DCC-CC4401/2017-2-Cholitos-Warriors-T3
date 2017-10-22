from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView

from users.forms import AuthenticationForm
import users.views

app_name ='users'

urlpatterns =[
    url(r'^signup/$', users.views.signup, name='signup'),
    url(r'^login/$',
        LoginView.as_view(template_name="login.html",
                          authentication_form=AuthenticationForm,
                          redirect_authenticated_user=True),
        name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout')

]