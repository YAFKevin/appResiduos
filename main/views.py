from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import tipoDocumentoForm, tipoCiudadanoForm, tipoMaquinariaForm, residuoForm, tipoIncentivoForm, tipoPersonalForm, zonaForm, personalForm, ciudadanoForm, maquinariaForm, rutaForm, horarioForm, tipoRecoleccionForm, recoleccionForm, detalleIncentivoForm, medidaRecoleccionForm
from .models import tipoDocumento, tipoMaquinaria, residuo, tipoIncentivo, tipoPersonal, zona, personal, tipoCiudadano, ciudadano, maquinaria, ruta, horario, tipoRecoleccion, recoleccion, detalleIncentivo, medidaRecoleccion, auditoria
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
import datetime as dt


# def home(request):
#     return render(request, 'home.html')

def home(request):
    username = None
    if request.user.is_authenticated:
        username = request.user.username
    context = {
        'username': username
    }
    return render(request, 'home.html', context)


def signout(request):
    logout(request)
    return redirect('home')


def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])

        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'Nombre de usuario o contraseña incorrectos'
            })
        else:
            login(request, user)
            return redirect('home')

        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })


def signup(request):

    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            # registrar usuario
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                 #Obtener la fecha actual
                fechas = dt.datetime.now()
                #Insertar la fecha a la tabla auditoria 
                auditorisa = auditoria(fecha=fechas, accion="Registro de usuario", usuario=request.user)
                auditorisa.save()
                return redirect('tipoDocumento')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    "error": 'El usuario ya existe'})

        return render(request, 'signup.html', {
            'form': UserCreationForm,
            "error": 'Las contraseñas no coinciden'})

@login_required
def listarAuditoria(request):
    auditorias = auditoria.objects.all()

    return render(request, 'auditoria.html', {'auditorias': auditorias})

@login_required
def listarTipoDocumento(request):
    tipoDocumentos = tipoDocumento.objects.all()

    return render(request, 'tipoDocumento.html', {'tipoDocumentos': tipoDocumentos})


@login_required
def listarTipoMaquinaria(request):
    tipoMaquinarias = tipoMaquinaria.objects.all()

    return render(request, 'tipoMaquinaria.html', {'tipoMaquinarias': tipoMaquinarias})


@login_required
def listarResiduo(request):
    residuos = residuo.objects.all()

    return render(request, 'residuo.html', {'residuos': residuos})


@login_required
def listarTipoIncentivo(request):
    tipoIncentivos = tipoIncentivo.objects.all()

    return render(request, 'tipoIncentivo.html', {'tipoIncentivos': tipoIncentivos})


@login_required
def listarTipoPersonal(request):
    tipoPersonals = tipoPersonal.objects.all()

    return render(request, 'tipoPersonal.html', {'tipoPersonals': tipoPersonals})


@login_required
def listarZona(request):
    zonas = zona.objects.all()

    return render(request, 'zona.html', {'zonas': zonas})


@login_required
def listarPersonal(request):
    personals = personal.objects.all()

    return render(request, 'personal.html', {'personals': personals})


@login_required
def listarTipoCiudadano(request):
    tipoCiudadanos = tipoCiudadano.objects.all()

    return render(request, 'tipoCiudadano.html', {'tipoCiudadanos': tipoCiudadanos})


@login_required
def listarCiudadano(request):
    ciudadanos = ciudadano.objects.all()

    return render(request, 'ciudadano.html', {'ciudadanos': ciudadanos})


@login_required
def listarMaquinaria(request):
    maquinarias = maquinaria.objects.all()

    return render(request, 'maquinaria.html', {'maquinarias': maquinarias})


@login_required
def listarRuta(request):
    rutas = ruta.objects.all()

    return render(request, 'ruta.html', {'rutas': rutas})


def listarHorario(request):
    horarios = horario.objects.all()

    return render(request, 'horario.html', {'horarios': horarios})


@login_required
def listarTipoRecoleccion(request):
    tipoRecoleccions = tipoRecoleccion.objects.all()

    return render(request, 'tipoRecoleccion.html', {'tipoRecoleccions': tipoRecoleccions})


@login_required
def listarRecoleccion(request):
    recoleccions = recoleccion.objects.all()

    return render(request, 'recoleccion.html', {'recoleccions': recoleccions})


@login_required
def listarDetalleIncentivo(request):
    detalleIncentivos = detalleIncentivo.objects.all()

    return render(request, 'detalleIncentivo.html', {'detalleIncentivos': detalleIncentivos})


@login_required
def listarMedidaRecoleccion(request):
    medidaRecoleccions = medidaRecoleccion.objects.all()

    return render(request, 'medidaRecoleccion.html', {'medidaRecoleccions': medidaRecoleccions})


#--CREAR

@login_required
def crearTipoDocumento(request):

    if request.method == 'GET':
        return render(request, 'crearTipoDocumento.html', {
            'form': tipoDocumentoForm
        })

    else:
        try:
            # print(request.POST)
            form = tipoDocumentoForm(request.POST)
            newTipoDocumento = form.save(commit=False)
            newTipoDocumento.save()
            # return redirect('tipoDocumento')

            #Obtener la fecha actual
            fechas = dt.datetime.now()
            #Insertar la fecha a la tabla auditoria 
            auditorisa = auditoria(fecha=fechas, accion="Creacion de Tipo Documento", usuario=request.user)
            auditorisa.save()

            return render(request, 'crearTipoDocumento.html', {
                'form': tipoDocumentoForm
            })
        except ValueError:
            return render(request, 'crearTipoDocumento.html', {
                'form': tipoDocumentoForm,
                'error': 'Por favor, ingrese un dato válido'
            })


@login_required
def crearTipoMaquinaria(request):

    if request.method == 'GET':
        return render(request, 'crearTipoMaquinaria.html', {
            'form': tipoMaquinariaForm
        })
    else:
        try:
            form = tipoMaquinariaForm(request.POST)
            newTipoMaquinaria = form.save(commit=False)
            newTipoMaquinaria.save()

             #Obtener la fecha actual
            fechas = dt.datetime.now()
            #Insertar la fecha a la tabla auditoria 
            auditorisa = auditoria(fecha=fechas, accion="Creacion de Tipo Maquinaria", usuario=request.user)
            auditorisa.save()
            return render(request, 'crearTipoMaquinaria.html', {
                'form': tipoMaquinariaForm
            })
        except ValueError:
            return render(request, 'crearTipoMaquinaria.html', {
                'form': tipoMaquinariaForm,
                'error': 'Por favor, ingrese un dato válido'
            })


@login_required
def crearResiduo(request):

    if request.method == 'GET':
        return render(request, 'crearResiduo.html', {
            'form': residuoForm
        })
    else:
        try:
            form = residuoForm(request.POST)
            newResiduo = form.save(commit=False)
            newResiduo.save()
             #Obtener la fecha actual
            fechas = dt.datetime.now()
            #Insertar la fecha a la tabla auditoria 
            auditorisa = auditoria(fecha=fechas, accion="Creacion de residuo", usuario=request.user)
            auditorisa.save()
            return render(request, 'crearResiduo.html', {
                'form': residuoForm
            })
        except ValueError:
            return render(request, 'crearResiduo.html', {
                'form': residuoForm,
                'error': 'Por favor, ingrese un dato válido'
            })


@login_required
def crearTipoIncentivo(request):

    if request.method == 'GET':
        return render(request, 'crearTipoIncentivo.html', {
            'form': tipoIncentivoForm
        })
    else:
        try:
            form = tipoIncentivoForm(request.POST)
            newTipoIncentivo = form.save(commit=False)
            newTipoIncentivo.save()
             #Obtener la fecha actual
            fechas = dt.datetime.now()
            #Insertar la fecha a la tabla auditoria 
            auditorisa = auditoria(fecha=fechas, accion="Creacion de Tipo Incentivo", usuario=request.user)
            auditorisa.save()
            return render(request, 'crearTipoIncentivo.html', {
                'form': tipoIncentivoForm
            })
        except ValueError:
            return render(request, 'crearTipoIncentivo.html', {
                'form': tipoIncentivoForm,
                'error': 'Por favor, ingrese un dato válido'
            })


@login_required
def crearTipoPersonal(request):

    if request.method == 'GET':
        return render(request, 'crearTipoPersonal.html', {
            'form': tipoPersonalForm
        })
    else:
        try:
            form = tipoPersonalForm(request.POST)
            newTipoPersonal = form.save(commit=False)
            newTipoPersonal.save()
             #Obtener la fecha actual
            fechas = dt.datetime.now()
            #Insertar la fecha a la tabla auditoria 
            auditorisa = auditoria(fecha=fechas, accion="Creacion de Tipo Personal", usuario=request.user)
            auditorisa.save()
            return render(request, 'crearTipoPersonal.html', {
                'form': tipoPersonalForm
            })
        except ValueError:
            return render(request, 'crearTipoPersonal.html', {
                'form': tipoPersonalForm,
                'error': 'Por favor, ingrese un dato válido'
            })


@login_required
def crearZona(request):

    if request.method == 'GET':
        return render(request, 'crearZona.html', {
            'form': zonaForm
        })
    else:
        try:
            form = zonaForm(request.POST)
            newZona = form.save(commit=False)
            newZona.save()
             #Obtener la fecha actual
            fechas = dt.datetime.now()
            #Insertar la fecha a la tabla auditoria 
            auditorisa = auditoria(fecha=fechas, accion="Creacion de Zona", usuario=request.user)
            auditorisa.save()
            return render(request, 'crearZona.html', {
                'form': zonaForm
            })
        except ValueError:
            return render(request, 'crearZona.html', {
                'form': zonaForm,
                'error': 'Por favor, ingrese un dato válido'
            })


@login_required
def crearPersonal(request):

    if request.method == 'GET':
        return render(request, 'crearPersonal.html', {
            'form': personalForm
        })
    else:
        try:
            form = personalForm(request.POST)
            newPersonal = form.save(commit=False)
            newPersonal.save()
             #Obtener la fecha actual
            fechas = dt.datetime.now()
            #Insertar la fecha a la tabla auditoria 
            auditorisa = auditoria(fecha=fechas, accion="Creacion de Personal", usuario=request.user)
            auditorisa.save()
            return render(request, 'crearPersonal.html', {
                'form': personalForm
            })
        except ValueError:
            return render(request, 'crearPersonal.html', {
                'form': personalForm,
                'error': 'Por favor, ingrese un dato válido'
            })


@login_required
def crearTipoCiudadano(request):

    if request.method == 'GET':
        return render(request, 'crearTipoCiudadano.html', {
            'form': tipoCiudadanoForm
        })
    else:
        try:
            form = tipoCiudadanoForm(request.POST)
            newTipoCiudadano = form.save(commit=False)
            newTipoCiudadano.save()
             #Obtener la fecha actual
            fechas = dt.datetime.now()
            #Insertar la fecha a la tabla auditoria 
            auditorisa = auditoria(fecha=fechas, accion="Creacion de Tipo Ciudadano", usuario=request.user)
            auditorisa.save()
            return render(request, 'crearTipoCiudadano.html', {
                'form': tipoCiudadanoForm
            })
        except ValueError:
            return render(request, 'crearTipoCiudadano.html', {
                'form': tipoCiudadanoForm,
                'error': 'Por favor, ingrese un dato válido'
            })


@login_required
def crearCiudadano(request):

    if request.method == 'GET':
        return render(request, 'crearCiudadano.html', {
            'form': ciudadanoForm
        })
    else:
        try:
            form = ciudadanoForm(request.POST)
            newCiudadano = form.save(commit=False)
            newCiudadano.save()
             #Obtener la fecha actual
            fechas = dt.datetime.now()
            #Insertar la fecha a la tabla auditoria 
            auditorisa = auditoria(fecha=fechas, accion="Creacion de ciudadano", usuario=request.user)
            auditorisa.save()
            return render(request, 'crearCiudadano.html', {
                'form': ciudadanoForm
            })
        except ValueError:
            return render(request, 'crearCiudadano.html', {
                'form': ciudadanoForm,
                'error': 'Por favor, ingrese un dato válido'
            })


@login_required
def crearMaquinaria(request):

    if request.method == 'GET':
        return render(request, 'crearMaquinaria.html', {
            'form': maquinariaForm
        })
    else:
        try:
            form = maquinariaForm(request.POST)
            newMaquinaria = form.save(commit=False)
            newMaquinaria.save()
             #Obtener la fecha actual
            fechas = dt.datetime.now()
            #Insertar la fecha a la tabla auditoria 
            auditorisa = auditoria(fecha=fechas, accion="Creacion de maquinaria", usuario=request.user)
            auditorisa.save()
            return render(request, 'crearMaquinaria.html', {
                'form': maquinariaForm
            })
        except ValueError:
            return render(request, 'crearMaquinaria.html', {
                'form': maquinariaForm,
                'error': 'Por favor, ingrese un dato válido'
            })


@login_required
def crearRuta(request):

    if request.method == 'GET':
        return render(request, 'crearRuta.html', {
            'form': rutaForm
        })
    else:
        try:
            form = rutaForm(request.POST)
            newRuta = form.save(commit=False)
            newRuta.save()
             #Obtener la fecha actual
            fechas = dt.datetime.now()
            #Insertar la fecha a la tabla auditoria 
            auditorisa = auditoria(fecha=fechas, accion="Creacion de ruta", usuario=request.user)
            auditorisa.save()
            return render(request, 'crearRuta.html', {
                'form': rutaForm
            })
        except ValueError:
            return render(request, 'crearRuta.html', {
                'form': rutaForm,
                'error': 'Por favor, ingrese un dato válido'
            })


@login_required
def crearHorario(request):

    if request.method == 'GET':
        return render(request, 'crearHorario.html', {
            'form': horarioForm
        })
    else:
        try:
            form = horarioForm(request.POST)
            newHorario = form.save(commit=False)
            newHorario.save()
             #Obtener la fecha actual
            fechas = dt.datetime.now()
            #Insertar la fecha a la tabla auditoria 
            auditorisa = auditoria(fecha=fechas, accion="Creacion de Horario", usuario=request.user)
            auditorisa.save()
            return render(request, 'crearHorario.html', {
                'form': horarioForm
            })
        except ValueError:
            return render(request, 'crearHorario.html', {
                'form': horarioForm,
                'error': 'Por favor, ingrese un dato válido'
            })


@login_required
def crearTipoRecoleccion(request):

    if request.method == 'GET':
        return render(request, 'crearTipoRecoleccion.html', {
            'form': tipoRecoleccionForm
        })
    else:
        try:
            form = tipoRecoleccionForm(request.POST)
            newTipoRecoleccion = form.save(commit=False)
            newTipoRecoleccion.save()
             #Obtener la fecha actual
            fechas = dt.datetime.now()
            #Insertar la fecha a la tabla auditoria 
            auditorisa = auditoria(fecha=fechas, accion="Creacion de Tipo Recoleccion", usuario=request.user)
            auditorisa.save()
            return render(request, 'crearTipoRecoleccion.html', {
                'form': tipoRecoleccionForm
            })
        except ValueError:
            return render(request, 'crearTipoRecoleccion.html', {
                'form': tipoRecoleccionForm,
                'error': 'Por favor, ingrese un dato válido'
            })


@login_required
def crearRecoleccion(request):

    if request.method == 'GET':
        return render(request, 'crearRecoleccion.html', {
            'form': recoleccionForm
        })
    else:
        try:
            form = recoleccionForm(request.POST)
            newRecoleccion = form.save(commit=False)
            
            newRecoleccion.usuario = request.user
            newRecoleccion.save()

            #Obtener la fecha actual
            fechas = dt.datetime.now()
            #Insertar la fecha a la tabla auditoria 
            auditorisa = auditoria(fecha=fechas, accion="Creacion de recoleccion", usuario=request.user)
            auditorisa.save()

            return render(request, 'crearRecoleccion.html', {
                'form': recoleccionForm
            })

        except ValueError:
            return render(request, 'crearRecoleccion.html', {
                'form': recoleccionForm,
                'error': 'Por favor, ingrese un dato válido'
            })


def crearMedidaRecoleccion(request):

    if request.method == 'GET':
        return render(request, 'crearMedidaRecoleccion.html', {
            'form': medidaRecoleccionForm
        })
    else:
        try:
            form = medidaRecoleccionForm(request.POST)
            newMedidaRecoleccion = form.save(commit=False)
            newMedidaRecoleccion.save()
             #Obtener la fecha actual
            fechas = dt.datetime.now()
            #Insertar la fecha a la tabla auditoria 
            auditorisa = auditoria(fecha=fechas, accion="Creacion de medida recolección", usuario=request.user)
            auditorisa.save()
            return render(request, 'crearMedidaRecoleccion.html', {
                'form': medidaRecoleccionForm
            })
        except ValueError:
            return render(request, 'crearMedidaRecoleccion.html', {
                'form': medidaRecoleccionForm,
                'error': 'Por favor, ingrese un dato válido'
            })


@login_required
def crearDetalleIncentivo(request):

    if request.method == 'GET':
        return render(request, 'crearDetalleIncentivo.html', {
            'form': detalleIncentivoForm
        })
    else:
        try:
            form = detalleIncentivoForm(request.POST)
            newDetalleIncentivo = form.save(commit=False)
            newDetalleIncentivo.save()
             #Obtener la fecha actual
            fechas = dt.datetime.now()
            #Insertar la fecha a la tabla auditoria 
            auditorisa = auditoria(fecha=fechas, accion="Creacion de Detalle incentivo", usuario=request.user)
            auditorisa.save()
            return render(request, 'crearDetalleIncentivo.html', {
                'form': detalleIncentivoForm
            })
        except ValueError:
            return render(request, 'crearDetalleIncentivo.html', {
                'form': detalleIncentivoForm,
                'error': 'Por favor, ingrese un dato válido'
            })
##-----------------------EDITAR-----------------------##

@login_required
def recoleccionDetail(request, recoleccion_id):
    if request.method == 'GET':
        recoleccions = get_object_or_404(recoleccion, pk=recoleccion_id)
        form = recoleccionForm(instance=recoleccions)
        return render(request, 'recoleccionDetail.html', {'recoleccion': recoleccions, 'form': form})
    else:
        try:
            recoleccions = get_object_or_404(recoleccion, pk=recoleccion_id)
            form = recoleccionForm(request.POST, instance=recoleccions)
            form.save()
             #Obtener la fecha actual
            fechas = dt.datetime.now()
            #Insertar la fecha a la tabla auditoria 
            auditorisa = auditoria(fecha=fechas, accion="Actualizar recolección", usuario=request.user)
            auditorisa.save()
            return redirect('recoleccion')
        except ValueError:
            return render(request, 'recoleccionDetail.html', {'recoleccion': recoleccions, 'form': form, 'error': 'Error al actualizar datos'})


@login_required
def tipoRecoleccionDetail(request, tipoRecoleccion_id):
    if request.method == 'GET':
        tipoRecoleccions = get_object_or_404(
            tipoRecoleccion, pk=tipoRecoleccion_id)
        form = tipoRecoleccionForm(instance=tipoRecoleccions)
        return render(request, 'tipoRecoleccionDetail.html', {'tipoRecoleccion': tipoRecoleccions, 'form': form})
    else:
        try:
            tipoRecoleccions = get_object_or_404(
                tipoRecoleccion, pk=tipoRecoleccion_id)
            form = tipoRecoleccionForm(request.POST, instance=tipoRecoleccions)
            form.save()
             #Obtener la fecha actual
            fechas = dt.datetime.now()
            #Insertar la fecha a la tabla auditoria 
            auditorisa = auditoria(fecha=fechas, accion="Actualizar de Tipo de Recolección", usuario=request.user)
            auditorisa.save()
            return redirect('tipoRecoleccion')
        except ValueError:
            return render(request, 'tipoRecoleccionDetail.html', {'tipoRecoleccion': tipoRecoleccions, 'form': form, 'error': 'Error al actualizar datos'})


@login_required
def ciudadanoDetail(request, ciudadano_id):
    if request.method == 'GET':
        ciudadanos = get_object_or_404(ciudadano, pk=ciudadano_id)
        form = ciudadanoForm(instance=ciudadanos)
        return render(request, 'ciudadanoDetail.html', {'ciudadano': ciudadanos, 'form': form})
    else:
        try:
            ciudadanos = get_object_or_404(ciudadano, pk=ciudadano_id)
            form = ciudadanoForm(request.POST, instance=ciudadanos)
            form.save()
             #Obtener la fecha actual
            fechas = dt.datetime.now()
            #Insertar la fecha a la tabla auditoria 
            auditorisa = auditoria(fecha=fechas, accion="Actualizar ciudadano", usuario=request.user)
            auditorisa.save()
            return redirect('ciudadano')
        except ValueError:
            return render(request, 'ciudadanoDetail.html', {'ciudadano': ciudadanos, 'form': form, 'error': 'Error al actualizar datos'})


@login_required
def detalleIncentivoDetail(request, detalleIncentivo_id):
    if request.method == 'GET':
        detalleIncentivos = get_object_or_404(
            detalleIncentivo, pk=detalleIncentivo_id)
        form = detalleIncentivoForm(instance=detalleIncentivos)
        return render(request, 'detalleIncentivoDetail.html', {'detalleIncentivo': detalleIncentivos, 'form': form})
    else:
        try:
            detalleIncentivos = get_object_or_404(
                detalleIncentivo, pk=detalleIncentivo_id)
            form = detalleIncentivoForm(
                request.POST, instance=detalleIncentivos)
            form.save()
             #Obtener la fecha actual
            fechas = dt.datetime.now()
            #Insertar la fecha a la tabla auditoria 
            auditorisa = auditoria(fecha=fechas, accion="Actualizar detalle incentivo", usuario=request.user)
            auditorisa.save()
            return redirect('detalleIncentivo')
        except ValueError:
            return render(request, 'detalleIncentivoDetail.html', {'detalleIncentivo': detalleIncentivos, 'form': form, 'error': 'Error al actualizar datos'})


@login_required
def tipoCiudadanoDetail(request, tipoCiudadano_id):
    if request.method == 'GET':
        tipoCiudadanos = get_object_or_404(
            tipoCiudadano, pk=tipoCiudadano_id)
        form = tipoCiudadanoForm(instance=tipoCiudadanos)
        return render(request, 'tipoCiudadanoDetail.html', {'tipoCiudadano': tipoCiudadanos, 'form': form})
    else:
        try:
            tipoCiudadanos = get_object_or_404(
                tipoCiudadano, pk=tipoCiudadano_id)
            form = tipoCiudadanoForm(
                request.POST, instance=tipoCiudadanos)
            form.save()
             #Obtener la fecha actual
            fechas = dt.datetime.now()
            #Insertar la fecha a la tabla auditoria 
            auditorisa = auditoria(fecha=fechas, accion="Actualizar tipo ciudadano", usuario=request.user)
            auditorisa.save()
            return redirect('tipoCiudadano')
        except ValueError:
            return render(request, 'tipoCiudadanoDetail.html', {'tipoCiudadano': tipoCiudadanos, 'form': form, 'error': 'Error al actualizar datos'})


@login_required
def horarioDetail(request, horario_id):
    if request.method == 'GET':
        horarios = get_object_or_404(horario, pk=horario_id)
        form = horarioForm(instance=horarios)
        return render(request, 'horarioDetail.html', {'horario': horarios, 'form': form})
    else:
        try:
            horarios = get_object_or_404(horario, pk=horario_id)
            form = horarioForm(request.POST, instance=horarios)
            form.save()
             #Obtener la fecha actual
            fechas = dt.datetime.now()
            #Insertar la fecha a la tabla auditoria 
            auditorisa = auditoria(fecha=fechas, accion="Actualizar horario", usuario=request.user)
            auditorisa.save()
            return redirect('horario')
        except ValueError:
            return render(request, 'horarioDetail.html', {'horario': horarios, 'form': form, 'error': 'Error al actualizar datos'})


@login_required
def personalDetail(request, personal_id):
    if request.method == 'GET':
        personals = get_object_or_404(personal, pk=personal_id)
        form = personalForm(instance=personals)
        return render(request, 'personalDetail.html', {'personal': personals, 'form': form})
    else:
        try:
            personals = get_object_or_404(personal, pk=personal_id)
            form = personalForm(request.POST, instance=personals)
            form.save()
             #Obtener la fecha actual
            fechas = dt.datetime.now()
            #Insertar la fecha a la tabla auditoria 
            auditorisa = auditoria(fecha=fechas, accion="Actualizar personal", usuario=request.user)
            auditorisa.save()
            return redirect('personal')
        except ValueError:
            return render(request, 'personalDetail.html', {'personal': personals, 'form': form, 'error': 'Error al actualizar datos'})


@login_required
def residuoDetail(request, residuo_id):
    if request.method == 'GET':
        residuos = get_object_or_404(residuo, pk=residuo_id)
        form = residuoForm(instance=residuos)
        return render(request, 'residuoDetail.html', {'residuo': residuos, 'form': form})
    else:
        try:
            residuos = get_object_or_404(residuo, pk=residuo_id)
            form = residuoForm(request.POST, instance=residuos)
            form.save()
             #Obtener la fecha actual
            fechas = dt.datetime.now()
            #Insertar la fecha a la tabla auditoria 
            auditorisa = auditoria(fecha=fechas, accion="Actualizar residuo", usuario=request.user)
            auditorisa.save()
            return redirect('residuo')
        except ValueError:
            return render(request, 'residuoDetail.html', {'residuo': residuos, 'form': form, 'error': 'Error al actualizar datos'})

@login_required
def rutaDetail(request, ruta_id):
    if request.method == 'GET':
        rutas = get_object_or_404(ruta, pk=ruta_id)
        form = rutaForm(instance=rutas)
        return render(request, 'rutaDetail.html', {'ruta': rutas, 'form': form})
    else:
        try:
            rutas = get_object_or_404(ruta, pk=ruta_id)
            form = rutaForm(request.POST, instance=rutas)
            form.save()
                    #Obtener la fecha actual
            fechas = dt.datetime.now()
            #Insertar la fecha a la tabla auditoria 
            auditorisa = auditoria(fecha=fechas, accion="Actualizar ruta", usuario=request.user)
            auditorisa.save()
            return redirect('ruta')
        except ValueError:
            return render(request, 'rutaDetail.html', {'ruta': rutas, 'form': form, 'error': 'Error al actualizar datos'})

@login_required
def zonaDetail(request, zona_id):
    if request.method == 'GET':
        zonas = get_object_or_404(zona, pk=zona_id)
        form = zonaForm(instance=zonas)
        return render(request, 'zonaDetail.html', {'zona': zonas, 'form': form})
    else:
        try:
            zonas = get_object_or_404(zona, pk=zona_id)
            form = zonaForm(request.POST, instance=zonas)
            form.save()
                    #Obtener la fecha actual
            fechas = dt.datetime.now()
            #Insertar la fecha a la tabla auditoria 
            auditorisa = auditoria(fecha=fechas, accion="Actualizar zona", usuario=request.user)
            auditorisa.save()
            return redirect('zona')
        except ValueError:
            return render(request, 'zonaDetail.html', {'zona': zonas, 'form': form, 'error': 'Error al actualizar datos'})

@login_required
def tipoMaquinariaDetail(request, tipoMaquinaria_id):
    if request.method == 'GET':
        tipoMaquinarias = get_object_or_404(
            tipoMaquinaria, pk=tipoMaquinaria_id)
        form = tipoMaquinariaForm(instance=tipoMaquinarias)
        return render(request, 'tipoMaquinariaDetail.html', {'tipoMaquinaria': tipoMaquinarias, 'form': form})
    else:
        try:
            tipoMaquinarias = get_object_or_404(
                tipoMaquinaria, pk=tipoMaquinaria_id)
            form = tipoMaquinariaForm(request.POST, instance=tipoMaquinarias)
            form.save()
                    #Obtener la fecha actual
            fechas = dt.datetime.now()
            #Insertar la fecha a la tabla auditoria 
            auditorisa = auditoria(fecha=fechas, accion="Actualizar tipo de maquinaria", usuario=request.user)
            auditorisa.save()
            return redirect('tipoMaquinaria')
        except ValueError:
            return render(request, 'tipoMaquinariaDetail.html', {'tipoMaquinaria': tipoMaquinarias, 'form': form, 'error': 'Error al actualizar datos'})

@login_required
def tipoDocumentoDetail(request, tipoDocumento_id):
    if request.method == 'GET':
        tipoDocumentos = get_object_or_404(tipoDocumento, pk=tipoDocumento_id)
        form = tipoDocumentoForm(instance=tipoDocumentos)
        return render(request, 'tipoDocumentoDetail.html', {'tipoDocumento': tipoDocumentos, 'form': form})
    else:
        try:
            tipoDocumentos = get_object_or_404(
                tipoDocumento, pk=tipoDocumento_id)
            form = tipoDocumentoForm(request.POST, instance=tipoDocumentos)
            form.save()
                    #Obtener la fecha actual
            fechas = dt.datetime.now()
            #Insertar la fecha a la tabla auditoria 
            auditorisa = auditoria(fecha=fechas, accion="Actualizar tipo documento", usuario=request.user)
            auditorisa.save()
            return redirect('tipoDocumento')
        except ValueError:
            return render(request, 'tipoDocumentoDetail.html', {'tipoDocumento': tipoDocumentos, 'form': form, 'error': 'Error al actualizar datos'})

@login_required
def tipoIncentivoDetail(request, tipoIncentivo_id):
    if request.method == 'GET':
        tipoIncentivos = get_object_or_404(tipoIncentivo, pk=tipoIncentivo_id)
        form = tipoIncentivoForm(instance=tipoIncentivos)
        return render(request, 'tipoIncentivoDetail.html', {'tipoIncentivo': tipoIncentivos, 'form': form})
    else:
        try:
            tipoIncentivos = get_object_or_404(
                tipoIncentivo, pk=tipoIncentivo_id)
            form = tipoIncentivoForm(request.POST, instance=tipoIncentivos)
            form.save()
                            #Obtener la fecha actual
            fechas = dt.datetime.now()
            #Insertar la fecha a la tabla auditoria 
            auditorisa = auditoria(fecha=fechas, accion="Actualizar tipo de incentivo", usuario=request.user)
            auditorisa.save()
            return redirect('tipoIncentivo')
        except ValueError:
            return render(request, 'tipoIncentivoDetail.html', {'tipoIncentivo': tipoIncentivos, 'form': form, 'error': 'Error al actualizar datos'})


@login_required
def maquinariaDetail(request, maquinaria_id):
    if request.method == 'GET':
        maquinarias = get_object_or_404(maquinaria, pk=maquinaria_id)
        form = maquinariaForm(instance=maquinarias)
        return render(request, 'maquinariaDetail.html', {'maquinaria': maquinarias, 'form': form})
    else:
        try:
            maquinarias = get_object_or_404(maquinaria, pk=maquinaria_id)
            form = maquinariaForm(request.POST, instance=maquinarias)
            form.save()
                                    #Obtener la fecha actual
            fechas = dt.datetime.now()
            #Insertar la fecha a la tabla auditoria 
            auditorisa = auditoria(fecha=fechas, accion="Actualizar maquinaria", usuario=request.user)
            auditorisa.save()
            return redirect('maquinaria')
        except ValueError:
            return render(request, 'maquinariaDetail.html', {'maquinaria': maquinarias, 'form': form, 'error': 'Error al actualizar datos'})

@login_required
def medidaRecoleccionDetail(request, medidaRecoleccion_id):
    if request.method == 'GET':
        medidaRecoleccions = get_object_or_404(
            medidaRecoleccion, pk=medidaRecoleccion_id)
        form = medidaRecoleccionForm(instance=medidaRecoleccions)
        return render(request, 'medidaRecoleccionDetail.html', {'medidaRecoleccion': medidaRecoleccions, 'form': form})
    else:
        try:
            medidaRecoleccions = get_object_or_404(
                medidaRecoleccion, pk=medidaRecoleccion_id)
            form = medidaRecoleccionForm(
                request.POST, instance=medidaRecoleccions)
            form.save()
                                    #Obtener la fecha actual
            fechas = dt.datetime.now()
            #Insertar la fecha a la tabla auditoria 
            auditorisa = auditoria(fecha=fechas, accion="Actualizar medida de recolección", usuario=request.user)
            auditorisa.save()

            return redirect('medidaRecoleccion')
        except ValueError:
            return render(request, 'medidaRecoleccionDetail.html', {'medidaRecoleccion': medidaRecoleccions, 'form': form, 'error': 'Error al actualizar datos'})

@login_required
def tipoPersonalDetail(request, tipoPersonal_id):
    if request.method == 'GET':
        tipoPersonals = get_object_or_404(tipoPersonal, pk=tipoPersonal_id)
        form = tipoPersonalForm(instance=tipoPersonals)
        return render(request, 'tipoPersonalDetail.html', {'tipoPersonal': tipoPersonals, 'form': form})
    else:
        try:
            tipoPersonals = get_object_or_404(tipoPersonal, pk=tipoPersonal_id)
            form = tipoPersonalForm(request.POST, instance=tipoPersonals)
            form.save()
                    #Obtener la fecha actual
            fechas = dt.datetime.now()
            #Insertar la fecha a la tabla auditoria 
            auditorisa = auditoria(fecha=fechas, accion="Actualizar tipo de personal", usuario=request.user)
            auditorisa.save()
            return redirect('tipoPersonal')
        except ValueError:
            return render(request, 'tipoPersonalDetail.html', {'tipoPersonal': tipoPersonals, 'form': form, 'error': 'Error al actualizar datos'})

#----------------Eliminar

@login_required
def eliminarResiduo(request, residuo_id):
    residuos = get_object_or_404(residuo, pk=residuo_id)
    if request.method == 'POST':
        residuos.delete()
         #Obtener la fecha actual
        fechas = dt.datetime.now()
        #Insertar la fecha a la tabla auditoria 
        auditorisa = auditoria(fecha=fechas, accion="Eliminar residuo", usuario=request.user)
        auditorisa.save()
        return redirect('residuo')

@login_required
def eliminarRecoleccion(request, recoleccion_id):
    recoleccions = get_object_or_404(recoleccion, pk=recoleccion_id)
    if request.method == 'POST':
        recoleccions.delete()
        #Obtener la fecha actual
        fechas = dt.datetime.now()
        #Insertar la fecha a la tabla auditoria 
        auditorisa = auditoria(fecha=fechas, accion="Eliminar recolección", usuario=request.user)
        auditorisa.save()
        return redirect('recoleccion')


@login_required
def eliminarTipoRecoleccion(request, tipoRecoleccion_id):
    tipoRecoleccions = get_object_or_404(
        tipoRecoleccion, pk=tipoRecoleccion_id)
    if request.method == 'POST':
        tipoRecoleccions.delete()
        #Obtener la fecha actual
        fechas = dt.datetime.now()
        #Insertar la fecha a la tabla auditoria 
        auditorisa = auditoria(fecha=fechas, accion="Eliminar tipo de recolección", usuario=request.user)
        auditorisa.save()
        return redirect('tipoRecoleccion')


@login_required
def eliminarRuta(request, ruta_id):
    rutas = get_object_or_404(ruta, pk=ruta_id)
    if request.method == 'POST':
        rutas.delete()
        #Obtener la fecha actual
        fechas = dt.datetime.now()
        #Insertar la fecha a la tabla auditoria 
        auditorisa = auditoria(fecha=fechas, accion="Eliminar ruta", usuario=request.user)
        auditorisa.save()        
        return redirect('ruta')


@login_required
def eliminarZona(request, zona_id):
    zonas = get_object_or_404(zona, pk=zona_id)
    if request.method == 'POST':
        zonas.delete()
                #Obtener la fecha actual
        fechas = dt.datetime.now()
        #Insertar la fecha a la tabla auditoria 
        auditorisa = auditoria(fecha=fechas, accion="Eliminar zona", usuario=request.user)
        auditorisa.save()
        return redirect('zona')

@login_required
def eliminarHorario(request, horario_id):
    horarios = get_object_or_404(horario, pk=horario_id)
    if request.method == 'POST':
        horarios.delete()
                #Obtener la fecha actual
        fechas = dt.datetime.now()
        #Insertar la fecha a la tabla auditoria 
        auditorisa = auditoria(fecha=fechas, accion="Eliminar horario", usuario=request.user)
        auditorisa.save()
        return redirect('horario')

@login_required
def eliminarTipoMaquinaria(request, tipoMaquinaria_id):
    tipoMaquinarias = get_object_or_404(tipoMaquinaria, pk=tipoMaquinaria_id)
    if request.method == 'POST':
        tipoMaquinarias.delete()
                #Obtener la fecha actual
        fechas = dt.datetime.now()
        #Insertar la fecha a la tabla auditoria 
        auditorisa = auditoria(fecha=fechas, accion="Eliminar tipo de maquinaria", usuario=request.user)
        auditorisa.save()
        return redirect('tipoMaquinaria')


@login_required
def eliminarTipoDocumento(request, tipoDocumento_id):
    tipoDocumentos = get_object_or_404(tipoDocumento, pk=tipoDocumento_id)
    if request.method == 'POST':
        tipoDocumentos.delete()
                        #Obtener la fecha actual
        fechas = dt.datetime.now()
        #Insertar la fecha a la tabla auditoria 
        auditorisa = auditoria(fecha=fechas, accion="Eliminar tipo de documento", usuario=request.user)
        auditorisa.save()
        return redirect('tipoDocumento')


@login_required
def eliminarTipoIncentivo(request, tipoIncentivo_id):
    tipoIncentivos = get_object_or_404(tipoIncentivo, pk=tipoIncentivo_id)
    if request.method == 'POST':
        tipoIncentivos.delete()
                        #Obtener la fecha actual
        fechas = dt.datetime.now()
        #Insertar la fecha a la tabla auditoria 
        auditorisa = auditoria(fecha=fechas, accion="Eliminar tipo de incentivo", usuario=request.user)
        auditorisa.save()
        return redirect('tipoIncentivo')


@login_required
def eliminarMaquinaria(request, maquinaria_id):
    maquinarias = get_object_or_404(maquinaria, pk=maquinaria_id)
    if request.method == 'POST':
        maquinarias.delete()
        #Obtener la fecha actual
        fechas = dt.datetime.now()
        #Insertar la fecha a la tabla auditoria 
        auditorisa = auditoria(fecha=fechas, accion="Eliminar maquinaria", usuario=request.user)
        auditorisa.save()
        return redirect('maquinaria')
    

@login_required
def eliminarDetalleIncentivo(request, detalleIncentivo_id):
    detalleIncentivos = get_object_or_404(
        detalleIncentivo, pk=detalleIncentivo_id)
    if request.method == 'POST':
        detalleIncentivos.delete()
                #Obtener la fecha actual
        fechas = dt.datetime.now()
        #Insertar la fecha a la tabla auditoria 
        auditorisa = auditoria(fecha=fechas, accion="Eliminar detalle incentivo", usuario=request.user)
        auditorisa.save()
        return redirect('detalleIncentivo')


@login_required
def eliminarTipoCiudadano(request, tipoCiudadano_id):
    tipoCiudadanos = get_object_or_404(tipoCiudadano, pk=tipoCiudadano_id)
    if request.method == 'POST':
        tipoCiudadanos.delete()
                #Obtener la fecha actual
        fechas = dt.datetime.now()
        #Insertar la fecha a la tabla auditoria 
        auditorisa = auditoria(fecha=fechas, accion="Eliminar tipo de ciudadano", usuario=request.user)
        auditorisa.save()
        return redirect('tipoCiudadano')


@login_required
def eliminarMedidaRecoleccion(request, medidaRecoleccion_id):
    medidaRecoleccions = get_object_or_404(
        medidaRecoleccion, pk=medidaRecoleccion_id)
    if request.method == 'POST':
        medidaRecoleccions.delete()
                #Obtener la fecha actual
        fechas = dt.datetime.now()
        #Insertar la fecha a la tabla auditoria 
        auditorisa = auditoria(fecha=fechas, accion="Eliminar medida de recolección", usuario=request.user)
        auditorisa.save()
        return redirect('medidaRecolección')
    
@login_required
def eliminarCiudadano(request, ciudadano_id):
    ciudadanos = get_object_or_404(ciudadano, pk=ciudadano_id)
    if request.method == 'POST':
        ciudadanos.delete()
                #Obtener la fecha actual
        fechas = dt.datetime.now()
        #Insertar la fecha a la tabla auditoria 
        auditorisa = auditoria(fecha=fechas, accion="Eliminar ciudadano", usuario=request.user)
        auditorisa.save()
        return redirect('ciudadano')


@login_required
def eliminarTipoPersonal(request, tipoPersonal_id):
    tipoPersonals = get_object_or_404(tipoPersonal, pk=tipoPersonal_id)
    if request.method == 'POST':
        tipoPersonals.delete()
                #Obtener la fecha actual
        fechas = dt.datetime.now()
        #Insertar la fecha a la tabla auditoria 
        auditorisa = auditoria(fecha=fechas, accion="Eliminar tipo de personal", usuario=request.user)
        auditorisa.save()
        return redirect('tipoPersonal')



@login_required
def eliminarPersonal(request, personal_id):
    personals = get_object_or_404(personal, pk=personal_id)
    if request.method == 'POST':
        personals.delete()
                #Obtener la fecha actual
        fechas = dt.datetime.now()
        #Insertar la fecha a la tabla auditoria 
        auditorisa = auditoria(fecha=fechas, accion="Eliminar personal", usuario=request.user)
        auditorisa.save()
        return redirect('personal')

#-----BUSCAR

@login_required
def buscarPersonal(request):
    template_name = "personal.html"
    buscPersonal = request.GET['buscPersonal']
    personals = personal.objects.filter(documento__icontains=buscPersonal)
    context = {'personals': personals}
    print(request)
    return render(request, template_name, context)


@login_required
def buscarCiudadano(request):
    template_name = "ciudadano.html"
    buscCiudadano = request.GET['buscCiudadano']
    ciudadanos = ciudadano.objects.filter(documento__icontains=buscCiudadano)
    context = {'ciudadanos': ciudadanos}
    print(request)
    return render(request, template_name, context)


@login_required
def buscarRuta(request):
    template_name = "ruta.html"
    buscRuta = request.GET['buscRuta']
    rutas = ruta.objects.filter(nombre__icontains=buscRuta)
    context = {'rutas': rutas}
    print(request)
    return render(request, template_name, context)


@login_required
def buscarZona(request):
    template_name = "zona.html"
    buscZona = request.GET['buscZona']
    zonas = zona.objects.filter(nombre__icontains=buscZona)
    context = {'zonas': zonas}
    print(request)
    return render(request, template_name, context)


@login_required
def buscarResiduo(request):
    template_name = "residuo.html"
    buscResiduo = request.GET['buscResiduo']
    residuos = residuo.objects.filter(nombre__icontains=buscResiduo)
    context = {'residuos': residuos}
    print(request)
    return render(request, template_name, context)


@login_required
def buscarTipoIncentivo(request):
    template_name = "tipoIncentivo.html"
    buscTipoIncentivo = request.GET['buscTipoIncentivo']
    tipoIncentivos = tipoIncentivo.objects.filter(
        nombre__icontains=buscTipoIncentivo)
    context = {'tipoIncentivos': tipoIncentivos}
    print(request)
    return render(request, template_name, context)


@login_required
def buscarMaquinaria(request):
    template_name = "maquinaria.html"
    buscMaquinaria = request.GET['buscMaquinaria']
    maquinarias = maquinaria.objects.filter(placa__icontains=buscMaquinaria)
    context = {'maquinarias': maquinarias}
    print(request)
    return render(request, template_name, context)


@login_required
def buscarTipoPersonal(request):
    template_name = "tipoPersonal.html"
    buscTipoPersonal = request.GET['buscTipoPersonal']
    tipoPersonals = tipoPersonal.objects.filter(
        nombre__icontains=buscTipoPersonal)
    context = {'tipoPersonals': tipoPersonals}
    print(request)
    return render(request, template_name, context)


@login_required
def buscarTipoCiudadano(request):
    template_name = "tipoCiudadano.html"
    buscTipoCiudadano = request.GET['buscTipoCiudadano']
    tipoCiudadanos = tipoCiudadano.objects.filter(
        nombre__icontains=buscTipoCiudadano)
    context = {'tipoCiudadanos': tipoCiudadanos}
    print(request)
    return render(request, template_name, context)


@login_required
def buscarTipoMaquinaria(request):
    template_name = "tipoMaquinaria.html"
    buscTipoMaquinaria = request.GET['buscTipoMaquinaria']
    tipoMaquinarias = tipoMaquinaria.objects.filter(
        nombre__icontains=buscTipoMaquinaria)
    context = {'tipoMaquinarias': tipoMaquinarias}
    print(request)
    return render(request, template_name, context)


@login_required
def buscarDetalleIncentivo(request):
    template_name = "detalleIncentivo.html"
    buscDetalleIncentivo = request.GET['buscDetalleIncentivo']
    detalleIncentivos = detalleIncentivo.objects.filter(
        idTipoIncentivo__nombre__icontains=buscDetalleIncentivo)
    context = {'detalleIncentivos': detalleIncentivos}
    print(request)
    return render(request, template_name, context)


@login_required
def buscarTipoRecoleccion(request):
    template_name = "tipoRecoleccion.html"
    buscTipoRecoleccion = request.GET['buscTipoRecoleccion']
    tipoRecoleccions = tipoRecoleccion.objects.filter(
        nombre__icontains=buscTipoRecoleccion)
    context = {'tipoRecoleccions': tipoRecoleccions}
    print(request)
    return render(request, template_name, context)


@login_required
def buscarHorario(request):
    template_name = "horario.html"
    buscHorario = request.GET['buscHorario']
    horarios = horario.objects.filter(
        hora__icontains=buscHorario)
    context = {'horarios': horarios}
    print(request)
    return render(request, template_name, context)

@login_required
def maquinariaVigente(request):
    template_name = "maquinariaVigente.html"
    maquinarias = maquinaria.objects.filter(estado=True)
    context = {'maquinarias': maquinarias}
    print(request)
    return render(request, template_name, context)




# @login_required
# #Crear una funcion que reciba como parametro el id del tipo de maquinaria
# def tipoMaquinariaSegunTipo(request):
#     #Obtener el idTipoMaqui que se envia por el POST
#     idTipoMaqui = request.POST['idTipoMaqui']
#     #Obtener las maquinarias que tengan el idTipoMaqui
#     maquinarias = maquinaria.objects.filter(idTipoMaquinaria=idTipoMaqui)

#     return render(request, 'tipoMaquinariaSegunTipo.html', {'maquinarias': maquinarias})
    
