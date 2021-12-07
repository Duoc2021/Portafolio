from django.contrib import admin
from .models import Departamento, Contacto, Direccion, Reserva, Tour, Trabajador, Reserva, Carrito

# Register your models here.

class DepartamentoAdmin(admin.ModelAdmin):# para crear vista en admin django
    list_display = ["nombre", "ubicacion", "precio"] # para ver lista
    #list_editable =["descripcion"] # para editar
    search_fields = ["nombre"] # para buscar
    list_filter = ["ubicacion"] # filtro de busqueda

admin.site.register(Departamento, DepartamentoAdmin)
#admin.site.register(Cliente)
admin.site.register(Contacto)
admin.site.register(Direccion)
admin.site.register(Tour)
admin.site.register(Trabajador)
admin.site.register(Reserva)
admin.site.register(Carrito)