from django import forms
from django.contrib.auth.models import User
from lloguer.models import Automobil, Reserva

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['user', 'automobil', 'data_inici', 'data_fi']

    # Opcional: Modificar els camps per tenir textos més descriptius
    user = forms.ModelChoiceField(queryset=User.objects.all(), label="Usuari")
    automobil = forms.ModelChoiceField(queryset=Automobil.objects.all(), label="Automòbil")
    data_inici = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}), label="Data d'Inici")
    data_fi = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}), label="Data de Finalització")
