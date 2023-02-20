from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import tipoDocumentoForm, tipoCiudadanoForm, tipoMaquinariaForm, residuoForm, tipoIncentivoForm, tipoPersonalForm, zonaForm, personalForm, ciudadanoForm, maquinariaForm, rutaForm, horarioForm, tipoRecoleccionForm, recoleccionForm, detalleIncentivoForm
from .models import tipoDocumento, tipoMaquinaria, residuo, tipoIncentivo, tipoPersonal, zona, personal, tipoCiudadano, ciudadano, maquinaria, ruta, horario, tipoRecoleccion, recoleccion, detalleIncentivo
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'home.html')


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
                return redirect('tipoDocumento')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    "error": 'El usuario ya existe'})

        return render(request, 'signup.html', {
            'form': UserCreationForm,
            "error": 'Las contraseñas no coinciden'})


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
            newRecoleccion.save()
            return render(request, 'crearRecoleccion.html', {
                'form': recoleccionForm
            })
        except ValueError:
            return render(request, 'crearRecoleccion.html', {
                'form': recoleccionForm,
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
            return render(request, 'crearDetalleIncentivo.html', {
                'form': detalleIncentivoForm
            })
        except ValueError:
            return render(request, 'crearDetalleIncentivo.html', {
                'form': detalleIncentivoForm,
                'error': 'Por favor, ingrese un dato válido'
            })


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
            return redirect('recoleccion')
        except ValueError:
            return render(request, 'recoleccionDetail.html', {'recoleccion': recoleccions, 'form': form, 'error': 'Error al actualizar datos'})


@login_required
def eliminarRecoleccion(request, recoleccion_id):
    recoleccions = get_object_or_404(recoleccion, pk=recoleccion_id)
    if request.method == 'POST':
        recoleccions.delete()
        return redirect('recoleccion')


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
            return redirect('ciudadano')
        except ValueError:
            return render(request, 'ciudadanoDetail.html', {'ciudadano': ciudadanos, 'form': form, 'error': 'Error al actualizar datos'})


@login_required
def eliminarCiudadano(request, ciudadano_id):
    ciudadanos = get_object_or_404(ciudadano, pk=ciudadano_id)
    if request.method == 'POST':
        ciudadanos.delete()
        return redirect('ciudadano')


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
            return redirect('detalleIncentivo')
        except ValueError:
            return render(request, 'detalleIncentivoDetail.html', {'detalleIncentivo': detalleIncentivos, 'form': form, 'error': 'Error al actualizar datos'})


@login_required
def eliminarDetalleIncentivo(request, detalleIncentivo_id):
    detalleIncentivos = get_object_or_404(
        detalleIncentivo, pk=detalleIncentivo_id)
    if request.method == 'POST':
        detalleIncentivos.delete()
        return redirect('detalleIncentivo')


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
            return redirect('horario')
        except ValueError:
            return render(request, 'horarioDetail.html', {'horario': horarios, 'form': form, 'error': 'Error al actualizar datos'})


@login_required
def eliminarHorario(request, horario_id):
    horarios = get_object_or_404(horario, pk=horario_id)
    if request.method == 'POST':
        horarios.delete()
        return redirect('horario')


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
            return redirect('personal')
        except ValueError:
            return render(request, 'personalDetail.html', {'personal': personals, 'form': form, 'error': 'Error al actualizar datos'})


@login_required
def eliminarPersonal(request, personal_id):
    personals = get_object_or_404(personal, pk=personal_id)
    if request.method == 'POST':
        personals.delete()
        return redirect('personal')


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
            return redirect('residuo')
        except ValueError:
            return render(request, 'residuoDetail.html', {'residuo': residuos, 'form': form, 'error': 'Error al actualizar datos'})


@login_required
def eliminarResiduo(request, residuo_id):
    residuos = get_object_or_404(residuo, pk=residuo_id)
    if request.method == 'POST':
        residuos.delete()
        return redirect('residuo')


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
            return redirect('ruta')
        except ValueError:
            return render(request, 'rutaDetail.html', {'ruta': rutas, 'form': form, 'error': 'Error al actualizar datos'})


@login_required
def eliminarRuta(request, ruta_id):
    rutas = get_object_or_404(ruta, pk=ruta_id)
    if request.method == 'POST':
        rutas.delete()
        return redirect('ruta')


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
            return redirect('zona')
        except ValueError:
            return render(request, 'zonaDetail.html', {'zona': zonas, 'form': form, 'error': 'Error al actualizar datos'})


@login_required
def eliminarZona(request, zona_id):
    zonas = get_object_or_404(zona, pk=zona_id)
    if request.method == 'POST':
        zonas.delete()
        return redirect('zona')


@login_required
def tipoDocumentoDetail(request, tipoDocumento_id):
    if request.method == 'GET':
        tipoDocumentos = get_object_or_404(tipoDocumento, pk=tipoDocumento_id)
        form = tipoDocumentoForm(instance=tipoDocumentos)
        return render(request, 'tipoDocumentoDetail.html', {'tipoDocumento': tipoDocumentos, 'form': form})
    else:
        try:
            tipoDocumentos = get_object_or_404(tipoDocumento, pk=tipoDocumento_id)
            form = tipoDocumentoForm(request.POST, instance=tipoDocumentos)
            form.save()
            return redirect('tipoDocumento')
        except ValueError:
            return render(request, 'tipoDocumentoDetail.html', {'tipoDocumento': tipoDocumentos, 'form': form, 'error': 'Error al actualizar datos'})

@login_required
def eliminarTipoDocumento(request, tipoDocumento_id):
    tipoDocumentos = get_object_or_404(tipoDocumento, pk=tipoDocumento_id)
    if request.method == 'POST':
        tipoDocumentos.delete()
        return redirect('tipoDocumento')
    
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
            return redirect('maquinaria')
        except ValueError:
            return render(request, 'maquinariaDetail.html', {'maquinaria': maquinarias, 'form': form, 'error': 'Error al actualizar datos'})
        
@login_required
def eliminarMaquinaria(request, maquinaria_id):
    maquinarias = get_object_or_404(maquinaria, pk=maquinaria_id)
    if request.method == 'POST':
        maquinarias.delete()
        return redirect('maquinaria')
    
