from django.shortcuts import render, redirect
from lloguer.models import *
from lloguer.forms import ReservaForm

# Create your views here.
def view_autos(request):
    # Obtenim tots els automòbils de la base de dades
    automobils = Automobil.objects.all()
    
    # Retornem la plantilla amb la llista d'automòbils
    return render(request, 'autos.html', {'automobils': automobils})

def create_reserva(request):
    if request.method == 'POST':
        # Crear un formulari amb les dades del POST
        form = ReservaForm(request.POST)
        if form.is_valid():
            # Guardem la nova reserva a la base de dades
            form.save()
            return redirect('view_autos')  # Redirigim a una pàgina (per exemple, la llista d'automòbils)
    else:
        form = ReservaForm()

    return render(request, 'reserva.html', {'form': form})