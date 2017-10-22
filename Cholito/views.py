from django.shortcuts import render, redirect
# Create your views here.

url = ''

def index(request):
    return render(request, url + 'login.html')

def landing_page_out(request):
    return render(request, url + 'usuario-out-adoptar.html')

def landing_page_in(request):
    return render(request, url + 'usuario-in-adoptar.html')