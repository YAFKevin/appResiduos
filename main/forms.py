from django.forms import ModelForm
from .models import tipoDocumento

class tipoDocumentoForm(ModelForm):
    class Meta:
        model = tipoDocumento
        fields = ['nombres']