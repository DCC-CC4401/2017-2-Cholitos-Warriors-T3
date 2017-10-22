from django.shortcuts import render

# Create your views here.
def stats_denuncias(request):
    return render(request, 'muni-estadisticas-denuncias.html')

# Create your views here.
def stats_fichas(request):
    return render(request, 'muni-estadisticas-ongs-fichas.html')

# Create your views here.
def denuncias_recibidas(request):
    return render(request, 'muni-denuncias-recibidas.html')
