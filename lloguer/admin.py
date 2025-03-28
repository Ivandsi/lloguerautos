from django.contrib import admin
from lloguer.models import *

# Register your models here.

class AutomobilAdmin(admin.ModelAdmin):
    list_display = ("marca", "model", "matricula")
    
class ReservaAdmin(admin.ModelAdmin):
    list_display = ("user", "automobil", "data_inici", "data_fi")

admin.site.register(Automobil, AutomobilAdmin)
admin.site.register(Reserva, ReservaAdmin)