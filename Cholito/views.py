from django.shortcuts import render, redirect
<<<<<<< HEAD
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
        return render(request, 'usuario-out-adoptar.html')        return render(request, 'usuario-out-adoptar.html')
=======
# Create your views here.

url = ''

def index(request):
    return render(request, url + 'login.html')

def landing_page_out(request):
    return render(request, url + 'usuario-out-adoptar.html')

def landing_page_in(request):
    return render(request, url + 'usuario-in-adoptar.html')
>>>>>>> ficha-adopcion
