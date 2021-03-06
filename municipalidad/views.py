from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from denuncias.models import Denuncia
from municipalidad.models import Municipalidad

# Create your views here.
def stats_denuncias(request):
    template_name = 'muni-estadisticas-denuncias.html'

    munis = Municipalidad.objects.all()
    context = {
        'user': request.user,
    }
    try:
        miMuni = munis.filter(user_id=request.user.id)
        if miMuni.count() == 1:
            context['miMuni'] = miMuni.first()
    except KeyError:
        context['miMuni'] = Municipalidad(comuna="dummy")
    return render(request, template_name, context)

def stats_fichas(request):
    munis = Municipalidad.objects.all()
    context = {
        'user': request.user,
    }
    try:
        miMuni = munis.filter(user_id=request.user.id)
        if miMuni.count() == 1:
            context['miMuni'] = miMuni.first()
    except KeyError:
        context['miMuni'] = Municipalidad(comuna="dummy")
    return render(request, 'muni-estadisticas-ongs-fichas.html', context)

def lista_denuncias(request):
    template_name = 'muni-denuncias-recibidas.html'

    context = {
        'user': request.user,
    }
    munis = Municipalidad.objects.all()
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

class UpdateReportView(View):

    def post(self, request, id, **kwargs):
        other_items = Denuncia.objects.filter(id=id)
        other_items.update(actual_state=request.POST.get('estado'))

        return lista_denuncias(request)

def detalle_denuncia(request, id):
    template_name = 'muni-detalle-denuncia.html'
    my_id = id
    context = {
        'user': request.user,
        'denuncia': Denuncia.objects.filter(id=int(my_id)).first()
    }
    munis = Municipalidad.objects.all()
    try:
        miMuni = munis.filter(user_id=request.user.id)
        if miMuni.count() == 1:
            context['miMuni'] = miMuni.first()
        muni = context['miMuni']
    except KeyError:
        context['miMuni'] = Municipalidad(comuna="dummy")
    return render(request, template_name, context)