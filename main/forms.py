from django.forms import ModelForm
from .models import tipoDocumento, tipoCiudadano, tipoMaquinaria, residuo, tipoIncentivo, tipoPersonal, zona, empadronamiento, personal, ciudadano

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

class tipoIncentivoForm(ModelForm):
    class Meta:
        model = tipoIncentivo
        fields = ['nombre', 'descripcion']

class tipoPersonalForm(ModelForm):
    class Meta:
        model = tipoPersonal
        fields = ['nombre', 'descripcion']

class zonaForm(ModelForm):
    class Meta:
        model = zona
        fields = ['nombre', 'estado']

class empadronamientoForm(ModelForm):
    class Meta:
        model = empadronamiento
        fields = ['nombre', 'descripcion']

class personalForm(ModelForm):
    class Meta:
        model = personal
        fields = ['nombre', 'apellido', 'documento', 'fechaNacimiento', 'correo', 'celular', 'direccion', 'estado', 'idTipoDoc', 'idTipoPersonal', 'idEmpadro']

class ciudadanoForm(ModelForm):
    class Meta:
        model = ciudadano
        fields = ['nombre', 'apellido', 'documento', 'celular', 'direccion', 'estado', 'idTipoDoc', 'idTipoCiud', 'idEmpadro']