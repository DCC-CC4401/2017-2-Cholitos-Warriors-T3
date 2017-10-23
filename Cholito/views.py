from django.shortcuts import render, redirect
from Cholito.models import ONG
from denuncias.models import Denuncia
from denuncias.models import Place
from adoption.models import AdoptionForm
import datetime
from users.models import CholitoUser


# Create your views here.
def landingPage(request):
    ongs = ONG.objects.all()

    context = {
        'user':request.user,
        'ONGData':ongs
    }

    if  request.user.is_authenticated():
        return render(request, 'usuario-in-adoptar.html', context)

    else:
        return render(request, 'usuario-out-adoptar.html', context)

def denuncia(request):
    if(request.method == 'POST'):
        typeOfAbuse = request.POST['typeOfAbuse']
        animal = request.POST['animal']
        hurt = False
        gender = request.POST['sexo']
        if(request.POST['herido'] == 'si'):
            hurt = True
        color = request.POST['color']
        comment = request.POST['comentario']

        lugar = Place(ciudad="dummy", comuna="dummy", calle="dummy", numero=549)
        lugar.save()
        denuncia = Denuncia(kindOfAbuse=typeOfAbuse, kindOfAnimal=animal, gender=gender, colour=color, hurt=hurt, comments=comment, location=lugar)
        denuncia.save()
    return landingPage(request)

def adopcion(request):
    if(AdoptionForm.objects.all().count() < 1):
        names = ["Chino", "Jenetta", "Alice", "Dumbo", "Ares", "Hades", "Rose"]
        types = ["Conejo", "Conejo", "Gato", "Perro", "Conejo", "Gato", "Oveja"]
        sexo = ["Hembra", "Hembra", "Hembra", "Macho", "Macho", "Macho", "Hembra"]
        date = datetime.datetime.today()
        description = "Me gustan los conejitos"
        adopted = [False, False, False, False, False, True, False]
        for i in range(0, 7):
            temp = '/static/dist/img/animal-' + str(i + 1) + '.jpg'
            animal = AdoptionForm(name=names[i], type=types[i], gender=sexo[i], in_adoption_from=date, description=description, adopted=adopted[i], id_number=i+1, picture_location=temp)
            animal.save()

    animals = AdoptionForm.objects.all()
    context = {
        'animals':animals
    }

    if request.user.is_authenticated():
        return render(request, 'usuario-in-ong.html', context)
    else:
        return render(request, 'usuario-out-ong.html', context)