from django.contrib.auth import login
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import CreateView

from users.forms import UserCreationForm, UserCholitoUserFormset

class SignUp(CreateView):
    template_name = "dummy" #TODO: Frontend para esto
    form_class = UserCreationForm

    def get(self, request, *args, **kwargs):

        if self.request.user_is_authenticated:
            return redirect("dummy") #TODO: Frontend para esto
        else:
            return super(SignUp, self).get(request, *args, *kwargs)

    def get_context_data(self, **kwargs):

        data =super(SignUp, self).get_context_data(**kwargs)
        if self.request.POST:
            data['formset'] = UserCholitoUserFormset(self.request.POST)
        else:
            data['formset'] = UserCholitoUserFormset()

        return data

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        self.object = form.save()

        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super(SignUp, self).form_valid(form)

    def get_success_url(self):

        login(self.request, self.object)
        return reverse("dummy") #TODO: Frontend Para Esto