from atexit import register
from django.contrib import admin
from tkinter import *

from .models import Empleado, EstCiv, Habilidades

# Register your models here.


class EmpleadoAdmin (admin.ModelAdmin):
    list_display = (
        'id',
        'nombre',
        'apellido',
        'trabajo',
        'departamento',
        'email',
        'imagen_de_perfil',
      )
    search_fields = ('nombre','apellido')
    list_filter = ('nombre','apellido','trabajo')
admin.site.register(Empleado,EmpleadoAdmin)

class HabilidadesAdmin (admin.ModelAdmin):
    list_display =(
        'habilidad',
    )
    search_fields = ('habilidad',)
    list_filter = ('habilidad',)
admin.site.register(Habilidades,HabilidadesAdmin)

class EstCivAdmin (admin.ModelAdmin):
    list_display = (
        'estadocivil',
    )
    search_fields = ('estadocivil',)
    list_filter = ('estadocivil',)
admin.site.register(EstCiv)