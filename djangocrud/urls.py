"""djangocrud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main import views 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('tipoDocumento/', views.tipoDocumento, name='tipoDocumento'),
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin'),
    path('tipoDocumento/crear/', views.crearTipoDocumento, name='crearTipoDocumento'),
    path('tipoCiudadano/crear/', views.crearTipoCiudadano, name='crearTipoCiudadano'),
    path('tipoMaquinaria/crear/', views.crearTipoMaquinaria, name='crearTipoMaquinaria'),
    path('residuo/crear/', views.crearResiduo, name='crearResiduo'),
    path('tipoIncentivo/crear/', views.crearTipoIncentivo, name='crearTipoIncentivo'),
    path('tipoPersonal/crear/', views.crearTipoPersonal, name='crearTipoPersonal'),
    path('zona/crear/', views.crearZona, name='crearZona'),
    # path('empadronamiento/crear/', views.crearEmpadronamiento, name='crearEmpadronamiento'),
    path('personal/crear/', views.crearPersonal, name='crearPersonal'),
]
