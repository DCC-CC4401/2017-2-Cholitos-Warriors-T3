from django.shortcuts import render
from django.views.generic import ListView
from denuncias.models import Denuncia
from municipalidad.models import Municipalidad
from Cholito.models import ONG

# Create your views here.
def stats_denuncias(request):
    template_name = 'muni-estadisticas-denuncias.html'

    munis = Municipalidad.objects.all()
    context = {
        'user': request.user,
        'ONGData': ONG.objects.all(),
    }
    try:
        miMuni = munis.filter(user_id=request.user.id)
        if miMuni.count() == 1:
            context['miMuni'] = miMuni.first()
    except KeyError:
        context['miMuni'] = Municipalidad(comuna="dummy")
    return render(request, template_name, context)

def stats_fichas(request):
    return render(request, 'muni-estadisticas-ongs-fichas.html')

def lista_denuncias(request):
    template_name = 'muni-denuncias-recibidas.html'

    munis = Municipalidad.objects.all()
    context = {
        'user': request.user,
        'ONGData': ONG.objects.all(),
    }
    try:
        miMuni = munis.filter(user_id=request.user.id)
        if miMuni.count() == 1:
            context['miMuni'] = miMuni.first()
        muni = context['miMuni']
        context['denuncias'] = Denuncia.objects.filter(location__comuna=muni.comuna)
    except KeyError:
        context['miMuni'] = Municipalidad(comuna="dummy")
        context['denuncias'] = Denuncia.objects.filter(location__comuna="dummy")
    return render(request, template_name, context)

