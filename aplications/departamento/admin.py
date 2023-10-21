from django.contrib import admin

from aplications.departamento.models import Departamento

# Register your models here.

class DepartamentoAdmin (admin.ModelAdmin):
    list_display = (
        'nombre',
        'sigla',
        'activo',
        'piso',
        'oficina',
    )
    list_filter = ('nombre',)
    search_fields= ('nombre','sigla','piso',)
admin.site.register(Departamento,DepartamentoAdmin)