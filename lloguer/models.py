from django.db import models
from django.contrib.auth.models import User


class Automobil(models.Model):
    marca = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    matricula = models.CharField(max_length=10)
    
    def __str__(self):
        return f"{self.marca} {self.model} ({self.matricula})"

class Reserva(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Usuari que fa la reserva
    automobil = models.ForeignKey(Automobil, on_delete=models.CASCADE)  # Automòbil reservat
    data_inici = models.DateTimeField()  # Data d'inici del lloguer
    data_fi = models.DateTimeField(null=True, blank=True)  # Data de finalització del lloguer
    
    class Meta:
        unique_together = ('automobil', 'data_inici')  # Evita que el mateix cotxe es reservi el mateix dia
        
    def __str__(self):
        return f"Reserva de {self.automobil} per {self.user.username} el {self.data_inici}"