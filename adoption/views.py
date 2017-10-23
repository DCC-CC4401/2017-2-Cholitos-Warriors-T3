from django.shortcuts import render, redirect
from adoption.models import AdoptionForm, AdoptionRequest
from django.contrib.auth.models import User
import datetime

# Create your views here.


def adopcion(request):
    if(AdoptionForm.objects.all().count() < 1):
        names = ["Chino", "Jenetta", "Alice", "Dumbo", "Ares", "Hades", "Rose"]
        types = ["Conejo", "Conejo", "Gato", "Perro", "Conejo", "Gato", "Oveja"]
        sexo = ["Hembra", "Hembra", "Hembra", "Macho", "Macho", "Macho", "Hembra"]
        date = datetime.datetime.today()
        description = "Me gustan los conejitos"
        adopted = [False, False, False, False, False, True, False]
        age = [1, 4, 2, 6, 3, 1, 8]
        adoptions = [2, 5, 4, 4, 1, 0, 12]
        description = "Esta es la descripcion de "
        description2 = ", nuestro amado animal que busca un nuevo hogar"
        for i in range(0, 7):
            temp = '/static/dist/img/animal-' + str(i + 1) + '.jpg'
            animal = AdoptionForm(name=names[i], type=types[i], gender=sexo[i], in_adoption_from=date, description=description, adopted=adopted[i], picture_location=temp, age=age[i], adoptionRequests=adoptions[i], comments=(description + names[i] + description2))
            animal.save()

    animals = AdoptionForm.objects.all()
    context = {
        'animals':animals
    }

    if request.user.is_authenticated():
        return render(request, 'usuario-in-ong.html', context)
    else:
        return render(request, 'usuario-out-ong.html', context)

def adoptionPage(request):
    if(request.method == 'POST'):
        if(not request.user.is_authenticated()):
            return redirect('users:login')
        buttonID = -1
        for animal in AdoptionForm.objects.all():
            if request.POST.get("button" + str(animal.id)):
                buttonID = animal.id
                break
        if buttonID != -1:
            animal = AdoptionForm.objects.get(id=buttonID)
            animal.adoptionRequests = animal.adoptionRequests + 1
            adoptionRequest = AdoptionRequest(animal=animal, user=User.objects.get(id=request.user.id))
            animal.save()
            adoptionRequest.save()
    return adopcion(request)
