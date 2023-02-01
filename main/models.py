from django.db import models

# Create your models here.
class tipoDocumento(models.Model):
    nombre = models.CharField(max_length= 20)