from django.contrib import admin
from .models import tipoDocumento, tipoMaquinaria, residuo, tipoUsuario, tipoIncentivo, tipoPersonal, zona, empadronamiento, personal, tipoCiudadano, ciudadano, maquinaria, ruta, horario, recoleccion, detalleIncentivo


# Register your models here.

admin.site.register(tipoDocumento)
admin.site.register(tipoMaquinaria)
admin.site.register(residuo)
admin.site.register(tipoUsuario)
admin.site.register(tipoIncentivo)
admin.site.register(tipoPersonal)   
admin.site.register(zona)
admin.site.register(empadronamiento)
admin.site.register(personal)
admin.site.register(tipoCiudadano)
admin.site.register(ciudadano)
admin.site.register(maquinaria)
admin.site.register(ruta)
admin.site.register(horario)
admin.site.register(recoleccion)
admin.site.register(detalleIncentivo)