from django import forms
from .models import tipoDocumento, tipoCiudadano, tipoMaquinaria, residuo, tipoIncentivo, tipoPersonal, zona, personal, ciudadano, maquinaria, ruta, horario, tipoRecoleccion, recoleccion, detalleIncentivo, medidaRecoleccion, auditoria


class tipoDocumentoForm(forms.ModelForm):
    class Meta:
        model = tipoDocumento
        fields = ['nombre']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
        }


class tipoMaquinariaForm(forms.ModelForm):

    class Meta:
        model = tipoMaquinaria
        fields = ['nombre']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
        }


class residuoForm(forms.ModelForm):
    class Meta:
        model = residuo
        fields = ['nombre', 'descripcion', 'estado']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'estado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class tipoIncentivoForm(forms.ModelForm):
    class Meta:
        model = tipoIncentivo
        fields = ['nombre', 'descripcion']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
        }


class tipoPersonalForm(forms.ModelForm):
    class Meta:
        model = tipoPersonal
        fields = ['nombre', 'descripcion']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
        }


class zonaForm(forms.ModelForm):
    class Meta:
        model = zona
        fields = ['nombre', 'estado']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'estado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class personalForm(forms.ModelForm):
    class Meta:
        model = personal
        fields = ['nombre', 'apellido', 'documento', 'fechaNacimiento', 'correo',
                  'celular', 'direccion', 'estado', 'idTipoDoc', 'idTipoPersonal']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'idTipoDoc': forms.Select(attrs={'class': 'form-select'}),
            'documento': forms.TextInput(attrs={'class': 'form-control'}),
            # 'fechaNacimiento': forms.DateInput(format='%d/%m/%Y'),
            'correo': forms.TextInput(attrs={'class': 'form-control'}),
            'celular': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'estado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'idTipoPersonal': forms.Select(attrs={'class': 'form-select'}),
        }


class tipoCiudadanoForm(forms.ModelForm):
    class Meta:
        model = tipoCiudadano
        fields = ['nombre', 'descripcion']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
        }


class ciudadanoForm(forms.ModelForm):
    class Meta:
        model = ciudadano
        fields = ['nombre', 'apellido', 'documento', 'celular',
                  'direccion', 'estado', 'idTipoDoc', 'idTipoCiud']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'documento': forms.TextInput(attrs={'class': 'form-control'}),
            'celular': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'estado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'idTipoDoc': forms.Select(attrs={'class': 'form-select'}),
            'idTipoCiud': forms.Select(attrs={'class': 'form-select'}),
        }


class maquinariaForm(forms.ModelForm):
    class Meta:
        model = maquinaria
        fields = ['nombre', 'placa', 'estado',
                  'cargaNeta', 'cargaUtil', 'idTipoMaqui']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'placa': forms.TextInput(attrs={'class': 'form-control'}),
            'estado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'cargaNeta': forms.TextInput(attrs={'class': 'form-control'}),
            'cargaUtil': forms.TextInput(attrs={'class': 'form-control'}),
            'idTipoMaqui': forms.Select(attrs={'class': 'form-select'}),
        }


class rutaForm(forms.ModelForm):
    class Meta:
        model = ruta
        fields = ['nombre', 'lugarInicio', 'lugarFin', 'idZona']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'lugarInicio': forms.TextInput(attrs={'class': 'form-control'}),
            'lugarFin': forms.TextInput(attrs={'class': 'form-control'}),
            'idZona': forms.Select(attrs={'class': 'form-select'}),
        }


class horarioForm(forms.ModelForm):
    class Meta:
        model = horario
        fields = ['fecha', 'hora', 'estado', 'idRuta']
        widgets = {
            # 'fecha': forms.DateInput(format='%d/%m/%Y'),
            # 'fecha' : forms.DateField(widget=forms.DateInput(attrs={'class': 'datepicker'})),
            # "fecha": DatePickerInput(),
            # 'hora': forms.TimeInput(attrs={'class': 'form-control'}),
            'estado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'idRuta': forms.Select(attrs={'class': 'form-select'}),
        }


class tipoRecoleccionForm(forms.ModelForm):
    class Meta:
        model = tipoRecoleccion
        fields = ['nombre', 'descripcion']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
        }


class recoleccionForm(forms.ModelForm):

    class Meta:
        model = recoleccion
        fields = ['Personal_ID', 'Maquinaria_ID', 'Residuo_ID', 'Horario_ID',
                  'Usuario_ID', 'TipoRecoleccion_ID', 'peso', 'medida', 'observacion']
        widgets = {
            'Personal_ID': forms.Select(attrs={'class': 'form-select'}),
            'Maquinaria_ID': forms.Select(attrs={'class': 'form-select'}),
            'Residuo_ID': forms.Select(attrs={'class': 'form-select'}),
            'Horario_ID': forms.Select(attrs={'class': 'form-select'}),
            'Usuario_ID': forms.Select(attrs={'class': 'form-select'}),
            'TipoRecoleccion_ID': forms.Select(attrs={'class': 'form-select'}),
            'peso': forms.NumberInput(attrs={'class': 'form-control'}),
            'medida': forms.Select(attrs={'class': 'form-select'}),
            'observacion': forms.Textarea(attrs={'class': 'form-control'}),
        }


class detalleIncentivoForm(forms.ModelForm):
    class Meta:
        model = detalleIncentivo
        fields = ['cantidad', 'idTipoIncentivo',
                  'idRecoleccion', 'idCiudadano']
        widgets = {
            'cantidad': forms.NumberInput(attrs={'class': 'form-control'}),
            'idTipoIncentivo': forms.Select(attrs={'class': 'form-select'}),
            'idRecoleccion': forms.Select(attrs={'class': 'form-select'}),
            'idCiudadano': forms.Select(attrs={'class': 'form-select'}),
        }


class medidaRecoleccionForm(forms.ModelForm):
    class Meta:
        model = medidaRecoleccion
        fields = ['nombre']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
        }
