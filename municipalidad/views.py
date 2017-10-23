from django.shortcuts import render
from django.views.generic import ListView
from denuncias.models import Denuncia

# Create your views here.
def stats_denuncias(request):
    return render(request, 'muni-estadisticas-denuncias.html')

def stats_fichas(request):
    return render(request, 'muni-estadisticas-ongs-fichas.html')

def denuncias_recibidas(request):
    return render(request, 'muni-denuncias-recibidas.html')

class ListaDenuncias(ListView):

    template_name = 'muni-denuncias-recibidas.html'

    def get(self, request, **kwargs):
        return render(request, self.template_name, {'denuncias': Denuncia.objects.all()})


