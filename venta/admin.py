from django.contrib import admin
from venta.models import Venta

# Register your models here.

class VentaAdmin(admin.ModelAdmin):
    list_display = ["barrio", "venta", "mes"]
    list_search = ["barrio"] 

admin.site.register(Venta, VentaAdmin)