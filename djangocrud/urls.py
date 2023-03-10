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
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin'),

    path('', views.home, name='home'),



    path('tipoDocumento/', views.listarTipoDocumento, name='tipoDocumento'),
    path('tipoMaquinaria/', views.listarTipoMaquinaria, name='tipoMaquinaria'),
    path('tipoIncentivo/', views.listarTipoIncentivo, name='tipoIncentivo'),
    path('tipoPersonal/', views.listarTipoPersonal, name='tipoPersonal'),
    path('residuo/', views.listarResiduo, name='residuo'),
    path('zona/', views.listarZona, name='zona'),
    path('personal/', views.listarPersonal, name='personal'),
    path('tipoCiudadano/', views.listarTipoCiudadano, name='tipoCiudadano'),
    path('ciudadano/', views.listarCiudadano, name='ciudadano'),
    path('maquinaria/', views.listarMaquinaria, name='maquinaria'),
    path('ruta/', views.listarRuta, name='ruta'),
    path('horario/', views.listarHorario, name='horario'),
    path('tipoRecoleccion/', views.listarTipoRecoleccion, name='tipoRecoleccion'),
    path('recoleccion/', views.listarRecoleccion, name='recoleccion'),
    path('detalleIncentivo/', views.listarDetalleIncentivo, name='detalleIncentivo'),
    path('medidaRecoleccion/', views.listarMedidaRecoleccion, name='medidaRecoleccion'),

    path('auditoria/', views.listarAuditoria, name='auditoria'),
    



    path('tipoDocumento/crear/', views.crearTipoDocumento, name='crearTipoDocumento'),
    path('tipoCiudadano/crear/', views.crearTipoCiudadano, name='crearTipoCiudadano'),
    path('tipoMaquinaria/crear/', views.crearTipoMaquinaria, name='crearTipoMaquinaria'),
    path('residuo/crear/', views.crearResiduo, name='crearResiduo'),
    path('tipoIncentivo/crear/', views.crearTipoIncentivo, name='crearTipoIncentivo'),
    path('tipoPersonal/crear/', views.crearTipoPersonal, name='crearTipoPersonal'),
    path('medidaRecoleccion/crear/', views.crearMedidaRecoleccion, name='crearMedidaRecoleccion'),
    path('zona/crear/', views.crearZona, name='crearZona'),
    path('personal/crear/', views.crearPersonal, name='crearPersonal'),
    path('ciudadano/crear/', views.crearCiudadano, name='crearCiudadano'),
    path('maquinaria/crear/', views.crearMaquinaria, name='crearMaquinaria'),
    path('ruta/crear/', views.crearRuta, name='crearRuta'),
    path('horario/crear/', views.crearHorario, name='crearHorario'),
    path('tipoRecoleccion/crear/', views.crearTipoRecoleccion, name='crearTipoRecoleccion'),
    path('recoleccion/crear/', views.crearRecoleccion, name='crearRecoleccion'),
    path('detalleIncentivo/crear/', views.crearDetalleIncentivo, name='crearDetalleIncentivo'),

    path('recoleccion/<int:recoleccion_id>/eliminar', views.eliminarRecoleccion, name='eliminarRecoleccion'),
    path('ciudadano/<int:ciudadano_id>/eliminar', views.eliminarCiudadano, name='eliminarCiudadano'),
    path('detalleIncentivo/<int:detalleIncentivo_id>/eliminar', views.eliminarDetalleIncentivo, name='eliminarDetalleIncentivo'),
    path('tipoIncentivo/<int:tipoIncentivo_id>/eliminar', views.eliminarTipoIncentivo, name='eliminarTipoIncentivo'),
    path('tipoCiudadano/<int:tipoCiudadano_id>/eliminar', views.eliminarTipoCiudadano, name='eliminarTipoCiudadano'),
    path('personal/<int:personal_id>/eliminar', views.eliminarPersonal, name='eliminarPersonal'),
    path('horario/<int:horario_id>/eliminar', views.eliminarHorario, name='eliminarHorario'),
    path('residuo/<int:residuo_id>/eliminar', views.eliminarResiduo, name='eliminarResiduo'),
    path('ruta/<int:ruta_id>/eliminar', views.eliminarRuta, name='eliminarRuta'),
    path('zona/<int:zona_id>/eliminar', views.eliminarZona, name='eliminarZona'),
    path('tipoDocumento/<int:tipoDocumento_id>/eliminar', views.eliminarTipoDocumento, name='eliminarTipoDocumento'),
    path('maquinaria/<int:maquinaria_id>/eliminar', views.eliminarMaquinaria, name='eliminarMaquinaria'),
    path('tipoPersonal/<int:tipoPersonal_id>/eliminar', views.eliminarTipoPersonal, name='eliminarTipoPersonal'),
    path('tipoMaquinaria/<int:tipoMaquinaria_id>/eliminar', views.eliminarTipoMaquinaria, name='eliminarTipoMaquinaria'),
    path('tipoRecoleccion/<int:tipoRecoleccion_id>/eliminar', views.eliminarTipoRecoleccion, name='eliminarTipoRecoleccion'),
    path('medidaRecoleccion/<int:medidaRecoleccion_id>/eliminar', views.eliminarMedidaRecoleccion, name='eliminarMedidaRecoleccion'),


    path('horario/<int:horario_id>', views.horarioDetail, name='horarioDetail'),
    path('recoleccion/<int:recoleccion_id>', views.recoleccionDetail, name='recoleccionDetail'),
    path('personal/<int:personal_id>', views.personalDetail, name='personalDetail'),
    path('detalleIncentivo/<int:detalleIncentivo_id>', views.detalleIncentivoDetail, name='detalleIncentivoDetail'),
    path('ciudadano/<int:ciudadano_id>', views.ciudadanoDetail, name='ciudadanoDetail'),
    path('residuo/<int:residuo_id>', views.residuoDetail, name='residuoDetail'),
    path('ruta/<int:ruta_id>', views.rutaDetail, name='rutaDetail'),
    path('zona/<int:zona_id>', views.zonaDetail, name='zonaDetail'),
    path('tipoDocumento/<int:tipoDocumento_id>', views.tipoDocumentoDetail, name='tipoDocumentoDetail'),
    path('maquinaria/<int:maquinaria_id>', views.maquinariaDetail, name='maquinariaDetail'),
    path('medidaRecoleccion/<int:medidaRecoleccion_id>', views.medidaRecoleccionDetail, name='medidaRecoleccionDetail'),
    path('tipoIncentivo/<int:tipoIncentivo_id>', views.tipoIncentivoDetail, name='tipoIncentivoDetail'),
    path('tipoCiudadano/<int:tipoCiudadano_id>', views.tipoCiudadanoDetail, name='tipoCiudadanoDetail'),
    path('tipoPersonal/<int:tipoPersonal_id>', views.tipoPersonalDetail, name='tipoPersonalDetail'),
    path('tipoMaquinaria/<int:tipoMaquinaria_id>', views.tipoMaquinariaDetail, name='tipoMaquinariaDetail'),
    path('tipoRecoleccion/<int:tipoRecoleccion_id>', views.tipoRecoleccionDetail, name='tipoRecoleccionDetail'),
    

    #Buscar
    path('buscarPersonal/', views.buscarPersonal, name='buscarPersonal'),
    path('buscarCiudadano/', views.buscarCiudadano, name='buscarCiudadano'),
    path('buscarRuta/', views.buscarRuta, name='buscarRuta'),
    path('buscarZona/', views.buscarZona, name='buscarZona'),
    path('buscarResiduo/', views.buscarResiduo, name='buscarResiduo'),
    path('buscarTipoIncentivo/', views.buscarTipoIncentivo, name='buscarTipoIncentivo'),
    path('buscarMaquinaria/', views.buscarMaquinaria, name='buscarMaquinaria'),
    path('buscarTipoPersonal/', views.buscarTipoPersonal, name='buscarTipoPersonal'),
    path('buscarTipoCiudadano/', views.buscarTipoCiudadano, name='buscarTipoCiudadano'),
    path('buscarTipoMaquinaria/', views.buscarTipoMaquinaria, name='buscarTipoMaquinaria'),
    path('buscarDetalleIncentivo/', views.buscarDetalleIncentivo, name='buscarDetalleIncentivo'),
    path('buscarTipoRecoleccion/', views.buscarTipoRecoleccion, name='buscarTipoRecoleccion'),
    path('buscarHorario/', views.buscarHorario, name='buscarHorario'),
    
    #reportes
    path('maquinariaVigente/', views.maquinariaVigente, name='maquinariaVigente'),
    # path('tipoMaquinariaSegunTipo/', views.tipoMaquinariaSegunTipo, name='tipoMaquinariaSegunTipo'),



]
