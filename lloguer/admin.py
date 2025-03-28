from django.contrib import admin
from lloguer.models import *

# Register your models here.

class AutomobilAdmin(admin.ModelAdmin):
    list_display = ("marca", "model", "matricula")

admin.site.register(Automobil, AutomobilAdmin)