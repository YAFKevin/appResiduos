from django.forms import ModelForm
from .models import tipoDocumento, tipoCiudadano, tipoMaquinaria, residuo

class tipoDocumentoForm(ModelForm):
    class Meta:
        model = tipoDocumento
        fields = ['nombres']

class tipoCiudadanoForm(ModelForm):
    class Meta:
        model = tipoCiudadano
        fields = ['nombre', 'descripcion']

class tipoMaquinariaForm(ModelForm):
    class Meta:
        model = tipoMaquinaria
        fields = ['nombre']

class residuoForm(ModelForm):
    class Meta:
        model = residuo
        fields = ['nombre', 'descripcion', 'estado']