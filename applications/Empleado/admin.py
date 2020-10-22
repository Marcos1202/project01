from django.contrib import admin
from .models import Empleado, Habilidades
# Register your models here.
admin.site.register(Habilidades)

class EmpleadoAdmin(admin.ModelAdmin):
    #vista arbol
    list_display = (
        'id',
        'first_name',
        'last_name',
        'departamento_id',
        'job',
        'full_name',

    )
    
    #crear una funcion para crear un campo que no existe en el model
    def full_name(self, obj):
        return '{} {}'.format(obj.first_name, obj.last_name)
    
    #busqueda
    search_fields=('first_name',)
    #filtrador
    list_filter = ('job','habilidades','departamento_id')
    #FILTRO PARA CAMPO MUCHOS A MUCHOS
    filter_horizontal = ('habilidades',)

admin.site.register(Empleado, EmpleadoAdmin)