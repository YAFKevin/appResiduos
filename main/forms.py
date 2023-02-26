from django import forms
from .models import tipoDocumento, tipoCiudadano, tipoMaquinaria, residuo, tipoIncentivo, tipoPersonal, zona, personal, ciudadano, maquinaria, ruta, horario, tipoRecoleccion, recoleccion, detalleIncentivo, medidaRecoleccion


class tipoDocumentoForm(forms.ModelForm):
    class Meta:
        model = tipoDocumento
        fields = ['nombre']


class tipoMaquinariaForm(forms.ModelForm):

    class Meta:
        model = tipoMaquinaria
        fields = ['nombre']


class residuoForm(forms.ModelForm):
    class Meta:
        model = residuo
        fields = ['nombre', 'descripcion', 'estado']


class tipoIncentivoForm(forms.ModelForm):
    class Meta:
        model = tipoIncentivo
        fields = ['nombre', 'descripcion']


class tipoPersonalForm(forms.ModelForm):
    class Meta:
        model = tipoPersonal
        fields = ['nombre', 'descripcion']


class zonaForm(forms.ModelForm):
    class Meta:
        model = zona
        fields = ['nombre', 'estado']


class personalForm(forms.ModelForm):
    class Meta:
        model = personal
        fields = ['nombre', 'apellido', 'documento', 'fechaNacimiento', 'correo',
                  'celular', 'direccion', 'estado', 'idTipoDoc', 'idTipoPersonal']


class tipoCiudadanoForm(forms.ModelForm):
    class Meta:
        model = tipoCiudadano
        fields = ['nombre', 'descripcion']


class ciudadanoForm(forms.ModelForm):
    class Meta:
        model = ciudadano
        fields = ['nombre', 'apellido', 'documento', 'celular',
                  'direccion', 'estado', 'idTipoDoc', 'idTipoCiud']
        
class maquinariaForm(forms.ModelForm):
    class Meta:
        model = maquinaria
        fields = ['nombre', 'placa', 'estado', 'cargaNeta', 'cargaUtil', 'idTipoMaqui']

class rutaForm(forms.ModelForm):
    class Meta:
        model = ruta
        fields = ['nombre', 'lugarInicio', 'lugarFin', 'idZona']

class horarioForm(forms.ModelForm):
    class Meta:
        model = horario
        fields = ['fecha', 'hora', 'estado', 'idRuta']
        widgets = {
            # "fecha": DatePickerInput(),
            # 'hora': forms.TimeInput(attrs={'class': 'form-control'}),
            # 'estado': forms.Select(attrs={'class': 'form-control'}),
            # 'idRuta': forms.Select(attrs={'class': 'form-control'}),
        }

class tipoRecoleccionForm(forms.ModelForm):
    class Meta:
        model = tipoRecoleccion
        fields = ['nombre', 'descripcion']

class recoleccionForm(forms.ModelForm):
    class Meta:
        model = recoleccion
        fields = ['Personal_ID', 'Maquinaria_ID', 'Residuo_ID', 'Horario_ID', 'Usuario_ID', 'TipoRecoleccion_ID', 'peso','medida', 'observacion']
        widgets = {

            'Personal_ID': forms.Select(attrs={'class': 'form-select'}),
            'Maquinaria_ID': forms.Select(attrs={'class': 'form-select'}),
            'Residuo_ID': forms.Select(attrs={'class': 'form-select'}),
            'Horario_ID': forms.Select(attrs={'class': 'form-select'}),
            'Usuario_ID': forms.Select(attrs={'class': 'form-select'}),
            'TipoRecoleccion_ID': forms.Select(attrs={'class': 'form-select'}),
            'peso': forms.TextInput(attrs={'class': 'form-control'}),
            'medida': forms.Select(attrs={'class': 'form-select'}),
            'observacion': forms.Textarea(attrs={'class': 'form-control'}),

        }
       
    
class detalleIncentivoForm(forms.ModelForm):
    class Meta:
        model = detalleIncentivo
        fields = ['cantidad', 'idTipoIncentivo', 'idRecoleccion', 'idCiudadano']
        


class medidaRecoleccionForm(forms.ModelForm):
    class Meta:
        model = medidaRecoleccion
        fields = ['nombre']