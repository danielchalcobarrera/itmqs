from django.contrib import admin

# Register your models here.

from .models import Catedratico
from .models import Tema
from .models import Contenido
from .models import Materia
from .models import Reporte_semanal
"""
Catedratico
"""
class CatedraticoAdmin(admin.ModelAdmin):
    list_display = ("id","paterno","materno","nombres","activo")
    ordering=["paterno"]
    search_fields=["paterno"]
    
admin.site.register(Catedratico, CatedraticoAdmin)
"""
Materias
"""
class MateriaAdmin(admin.ModelAdmin):
    list_display = ("id","materia","codigo_materia")
    ordering=["materia"]
    search_fields=["materia"]
    
admin.site.register(Materia, MateriaAdmin)

"""
Temas
"""
class TemaAdmin(admin.ModelAdmin):
    list_display = ("id","indice","tema","materia_id")
    ordering=["tema"]
    search_fields=["tema"]
    
admin.site.register(Tema, TemaAdmin)
"""
Contenido
"""

class ContenidoAdmin(admin.ModelAdmin):
    list_display = ("id","indice","contenido","tema_id")
    ordering = ["contenido"]
    search_fields=["contenido"]
   
admin.site.register(Contenido, ContenidoAdmin)

class Reporte_semanalAdmin(admin.ModelAdmin):
    list_display = ("id","fecha_entrega","nro_semana","catedratico_id")
    ordering = ["fecha_entrega"]
    search_fields=["nro_semana"]

admin.site.register(Reporte_semanal, Reporte_semanalAdmin)

