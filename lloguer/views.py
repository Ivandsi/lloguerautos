from django.shortcuts import render
from lloguer.models import *

# Create your views here.
def view_autos(request):
    # Obtenim tots els automòbils de la base de dades
    automobils = Automobil.objects.all()
    
    # Retornem la plantilla amb la llista d'automòbils
    return render(request, 'autos.html', {'automobils': automobils})