from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class tipoDocumento(models.Model):
    nombres = models.CharField(max_length= 20, unique=True)
    def __str__(self):
        return self.nombres

class tipoMaquinaria(models.Model):
    nombre = models.CharField(max_length=20, unique=True, null=True)
    def __str__(self):
        return self.nombre

class residuo(models.Model):
    nombre = models.CharField(max_length=20, unique=True)
    descripcion = models.TextField(blank=True)
    estado = models.BooleanField()

    def __str__(self):
        return self.nombre

# class tipoUsuario(models.Model):
#     nombre = models.CharField(max_length=30)
#     descripcion = models.TextField(blank=True)
#     estado = models.BooleanField()

#     def __str__(self):
#         return self.nombre

class tipoIncentivo(models.Model):
    nombre = models.CharField(max_length=35)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre

class tipoPersonal(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre

class zona(models.Model):
    nombre = models.CharField(max_length=50)
    estado = models.BooleanField()

    def __str__(self):
        return self.nombre

# class empadronamiento(models.Model):
#     nombre = models.CharField(max_length=30)
#     descripcion = models.TextField(blank=True)

#     def __str__(self):
#         return self.nombre

# class usuario(models.Model):
#     nombre_usuario = models.CharField(max_length=30, unique=True)
#     nombreCompleto = models.CharField(max_length=100)
#     contraseña = models.CharField(max_length=30)
#     estado = models.BooleanField()
#     TipoUsuario_ID = models.ForeignKey(tipoUsuario, on_delete=models.CASCADE)

class personal(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    documento = models.CharField(max_length=20, unique=True)
    fechaNacimiento = models.DateField()
    correo = models.CharField(max_length=100, unique=True)
    celular = models.CharField(max_length=9, unique=True)
    direccion = models.CharField(max_length=100)
    estado = models.BooleanField(default=True)
    idTipoDoc = models.ForeignKey(tipoDocumento, on_delete=models.CASCADE)
    idTipoPersonal = models.ForeignKey(tipoPersonal, on_delete=models.CASCADE)
    # idEmpadro = models.ForeignKey(empadronamiento, on_delete=models.CASCADE)

    def __str__(self):
        return self.apellido + ' ' + self.nombre

class tipoCiudadano(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre

class ciudadano(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    documento = models.CharField(max_length=20, unique=True)
    celular = models.CharField(max_length=9, unique=True)
    direccion = models.CharField(max_length=100)
    estado = models.BooleanField() 
    idTipoDoc = models.ForeignKey(tipoDocumento, on_delete=models.CASCADE)
    # idEmpadro = models.ForeignKey(empadronamiento, on_delete=models.CASCADE)
    idTipoCiud = models.ForeignKey(tipoCiudadano, on_delete=models.CASCADE)

    def __str__(self):
        return self.apellido + ' ' + self.nombre


class maquinaria(models.Model):
    nombre = models.CharField(max_length=30)
    placa = models.CharField(max_length=7, unique=True)
    estado = models.BooleanField()
    cargaNeta = models.FloatField()
    cargaUtil = models.FloatField()
    idTipoMaqui = models.ForeignKey(tipoMaquinaria, on_delete=models.CASCADE)

    def __str__(self):
        return self.placa + ' | ' + self.nombre + ' | ' + self.idTipoMaqui.nombre

class ruta(models.Model):
    nombre = models.CharField(max_length=200)
    lugarInicio = models.CharField(max_length=100)
    lugarFin = models.CharField(max_length=100)
    idZona = models.ForeignKey(zona, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre

class horario(models.Model):
    fecha = models.DateField()
    hora = models.TimeField()
    estado = models.BooleanField()
    idRuta = models.ForeignKey(ruta, on_delete=models.CASCADE)

    #mostrar la ruta con la hora y fecha del horario en string
    def __str__(self):
        return self.idRuta.nombreruta + ' | ' +  str(self.fecha) + ' ' + str(self.hora)  


class tipoRecoleccion(models.Model):
    nombre = models.CharField(max_length=40)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre  


class recoleccion(models.Model):
    #agregar el campo de observacion con un maximo de 200 caracteres y que sea nulo
    observacion = models.CharField(max_length=200, blank=True)
    Personal_ID = models.ForeignKey(personal, on_delete=models.CASCADE)
    Maquinaria_ID = models.ForeignKey(maquinaria, on_delete=models.CASCADE)
    Residuo_ID = models.ForeignKey(residuo, on_delete=models.CASCADE)
    Horario_ID = models.ForeignKey(horario, on_delete=models.CASCADE)
    Usuario_ID = models.ForeignKey(User, on_delete=models.CASCADE)
    TipoRecoleccion_ID = models.ForeignKey(tipoRecoleccion, on_delete=models.CASCADE, null = True)

    #mostrar el el nombre del residuo y la fecha de recoleccion en string
    def __str__(self):
        return self.Residuo_ID.nombre + ' | ' + str(self.Horario_ID.fecha) + ' ' + str(self.Horario_ID.hora)

class detalleIncentivo(models.Model):
    cantidad = models.IntegerField()
    idTipoIncentivo = models.ForeignKey(tipoIncentivo, on_delete=models.CASCADE)
    idRecoleccion = models.ForeignKey(recoleccion, on_delete=models.CASCADE)
    idCiudadano = models.ForeignKey(ciudadano, on_delete=models.CASCADE)

    def __str__(self):
        return self.idCiudadano.apellido + ' ' + self.idCiudadano.nombre + ' | ' + self.idRecoleccion.Residuo_ID.nombre + ' | ' + str(self.idRecoleccion.Horario_ID.fecha) + ' ' + str(self.idRecoleccion.Horario_ID.hora)
    

