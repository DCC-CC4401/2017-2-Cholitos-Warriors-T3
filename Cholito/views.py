from django.shortcuts import render, redirect
from Cholito.models import ONG
from denuncias.models import Denuncia, Place
from municipalidad.models import Municipalidad
from municipalidad.views import lista_denuncias

# Create your views here.
def landingPage(request):
    ongs = ONG.objects.all()
    munis = Municipalidad.objects.all()
    context = {
        'user': request.user,
        'ONGData': ongs
    }

    if request.user.is_authenticated():
        miMuni = munis.filter(user_id=request.user.id)
        if miMuni.count() == 1:
            context['miMuni'] = miMuni.first()
            return lista_denuncias(request)
        return render(request, 'usuario-in-adoptar.html', context)
    else:
        return render(request, 'usuario-out-adoptar.html', context)


def denuncia(request):
    if request.method == 'POST':
        typeOfAbuse = request.POST['typeOfAbuse']
        animal = request.POST['animal']
        hurt = False
        gender = request.POST['sexo']
        if request.POST['herido'] == 'si':
            hurt = True
        color = request.POST['color']
        comment = request.POST['comentario']

        lugar = Place(ciudad="dummy", comuna="dummy", calle="dummy", numero=549)
        lugar.save()
        denuncia = Denuncia(kindOfAbuse=typeOfAbuse, kindOfAnimal=animal, gender=gender, colour=color, hurt=hurt, comments=comment, location=lugar)
        denuncia.save()
    return landingPage(request)
