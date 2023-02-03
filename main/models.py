from django.db import models

# Create your models here.
class tipoDocumento(models.Model):
    nombre = models.CharField(max_length= 20)

class tipoMaquinaria(models.Model):
    descripcion = models.TextField(blank=True)

class residuo(models.Model):
    nombre = models.CharField(max_length=20, unique=True)
    descripcion = models.TextField(blank=True)
    estado = models.BooleanField()

class tipoUsuario(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.TextField(blank=True)
    estado = models.BooleanField()

class tipoIncentivo(models.Model):
    nombre = models.CharField(max_length=20)
    descripcion = models.TextField(blank=True)

class tipoPersonal(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.TextField(blank=True)

class zona(models.Model):
    nombre = models.CharField(max_length=50)
    estado = models.BooleanField()

class empadronamiento(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.TextField(blank=True)

class usuario(models.Model):
    nombre_usuario = models.CharField(max_length=30, unique=True)
    nombreCompleto = models.CharField(max_length=100)
    contraseña = models.CharField(max_length=30)
    estado = models.BooleanField()
    TipoUsuario_ID = models.ForeignKey(tipoUsuario, on_delete=models.CASCADE)

class personal(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    documento = models.CharField(max_length=20, unique=True)
    fechaNacimiento = models.DateField()
    correo = models.CharField(max_length=100, unique=True)
    celular = models.CharField(max_length=9, unique=True)
    direccion = models.CharField(max_length=100)
    estado = models.BooleanField()
    idTipoDoc = models.ForeignKey(tipoDocumento, on_delete=models.CASCADE)
    idTipoPersonal = models.ForeignKey(tipoPersonal, on_delete=models.CASCADE)
    idEmpadro = models.ForeignKey(empadronamiento, on_delete=models.CASCADE)

class tipoCiudadano(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(blank=True)

class ciudadano(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    documento = models.CharField(max_length=20, unique=True)
    celular = models.CharField(max_length=9, unique=True)
    direccion = models.CharField(max_length=100)
    estado = models.BooleanField()
    idTipoDoc = models.ForeignKey(tipoDocumento, on_delete=models.CASCADE)
    idEmpadro = models.ForeignKey(empadronamiento, on_delete=models.CASCADE)
    idTipoCiud = models.ForeignKey(tipoCiudadano, on_delete=models.CASCADE)


class maquinaria(models.Model):
    nombre = models.CharField(max_length=30)
    placa = models.CharField(max_length=7, unique=True)
    estado = models.BooleanField()
    cargaNeta = models.FloatField()
    cargaUtil = models.FloatField()
    idTipoMaqui = models.ForeignKey(tipoMaquinaria, on_delete=models.CASCADE)

class ruta(models.Model):
    ruta = models.CharField(max_length=200)
    lugarInicio = models.CharField(max_length=100)
    lugarFin = models.CharField(max_length=100)
    idZona = models.ForeignKey(zona, on_delete=models.CASCADE)

class horario(models.Model):
    fecha = models.DateField()
    hora = models.TimeField()
    estado = models.BooleanField()
    idRuta = models.ForeignKey(ruta, on_delete=models.CASCADE)

class recoleccion(models.Model):
    observacion = models.CharField(max_length=200)
    Personal_ID = models.ForeignKey(personal, on_delete=models.CASCADE)
    Maquinaria_ID = models.ForeignKey(maquinaria, on_delete=models.CASCADE)
    Residuo_ID = models.ForeignKey(residuo, on_delete=models.CASCADE)
    Horario_ID = models.ForeignKey(horario, on_delete=models.CASCADE)
    Usuario_ID = models.ForeignKey(usuario, on_delete=models.CASCADE)



class detalleIncentivo(models.Model):
    cantidad = models.IntegerField()
    idTipoIncentivo = models.ForeignKey(tipoIncentivo, on_delete=models.CASCADE)
    idRecoleccion = models.ForeignKey(recoleccion, on_delete=models.CASCADE)
    idCiudadano = models.ForeignKey(ciudadano, on_delete=models.CASCADE)