from django.shortcuts import render, redirect
from Cholito.models import ONG
from users.models import CholitoUser


# Create your views here.

def landingPage(request):
    ongs = ONG.objects.all()

    context = {
        'user':request.user,
        'ONGData':ongs
    }

    if request.user.has_perm(''):
        return render(request, 'usuario-in-adoptar.html', context)

    else:
        return render(request, 'usuario-out-adoptar.html')