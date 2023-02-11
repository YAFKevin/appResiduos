from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import tipoDocumentoForm, tipoCiudadanoForm, tipoMaquinariaForm, residuoForm, tipoIncentivoForm, tipoPersonalForm, zonaForm, empadronamientoForm, personalForm
# Create your views here.


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


def tipoDocumento(request):
    return render(request, 'tipoDocumento.html')


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
            return redirect('tipoDocumento')

        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })

# crear


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


def crearEmpadronamiento(request):

    if request.method == 'GET':
        return render(request, 'crearEmpadronamiento.html', {
            'form': empadronamientoForm
        })
    else:
        try:
            form = empadronamientoForm(request.POST)
            newEmpadronamiento = form.save(commit=False)
            newEmpadronamiento.save()
            return render(request, 'crearEmpadronamiento.html', {
                'form': empadronamientoForm
            })
        except ValueError:
            return render(request, 'crearEmpadronamiento.html', {
                'form': empadronamientoForm,
                'error': 'Por favor, ingrese un dato válido'
            })


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
