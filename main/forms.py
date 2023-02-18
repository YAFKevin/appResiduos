from django.forms import ModelForm
from .models import tipoDocumento, tipoCiudadano, tipoMaquinaria, residuo, tipoIncentivo, tipoPersonal, zona, personal, ciudadano, maquinaria, ruta, horario, tipoRecoleccion, recoleccion, detalleIncentivo


class tipoDocumentoForm(ModelForm):
    class Meta:
        model = tipoDocumento
        fields = ['nombre']


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


class personalForm(ModelForm):
    class Meta:
        model = personal
        fields = ['nombre', 'apellido', 'documento', 'fechaNacimiento', 'correo',
                  'celular', 'direccion', 'estado', 'idTipoDoc', 'idTipoPersonal']


class tipoCiudadanoForm(ModelForm):
    class Meta:
        model = tipoCiudadano
        fields = ['nombre', 'descripcion']


class ciudadanoForm(ModelForm):
    class Meta:
        model = ciudadano
        fields = ['nombre', 'apellido', 'documento', 'celular',
                  'direccion', 'estado', 'idTipoDoc', 'idTipoCiud']
        
class maquinariaForm(ModelForm):
    class Meta:
        model = maquinaria
        fields = ['nombre', 'placa', 'estado', 'cargaNeta', 'cargaUtil', 'idTipoMaqui']

class rutaForm(ModelForm):
    class Meta:
        model = ruta
        fields = ['nombre', 'lugarInicio', 'lugarFin', 'idZona']

class horarioForm(ModelForm):
    class Meta:
        model = horario
        fields = ['fecha', 'hora', 'estado', 'idRuta']

class tipoRecoleccionForm(ModelForm):
    class Meta:
        model = tipoRecoleccion
        fields = ['nombre', 'descripcion']

class recoleccionForm(ModelForm):
    class Meta:
        model = recoleccion
        fields = ['observacion', 'Personal_ID', 'Maquinaria_ID', 'Residuo_ID', 'Horario_ID', 'Usuario_ID', 'TipoRecoleccion_ID']
    
class detalleIncentivoForm(ModelForm):
    class Meta:
        model = detalleIncentivo
        fields = ['cantidad', 'idTipoIncentivo', 'idRecoleccion', 'idCiudadano']



# class empadronamientoForm(ModelForm):
#     class Meta:
#         model = empadronamiento
#         fields = ['nombre', 'descripcion']
