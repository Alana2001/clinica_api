"""core URL Configuration

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
from django.urls import path, include
from rest_framework import routers
from medicos.views import EspecialidadesViewSet, Cadastrar_MedicosViewSet, AgendaViewSet, ListaEspecialidadesSerializer, ListaMedicosCadastradosSerializer, ListaAgendamentosSerializer
from clientes.views import ClientesViewSet
from consultas.views import ConsultasViewSet

router = routers.DefaultRouter()
router.register('Especialidades', EspecialidadesViewSet, basename='Especialidades')
router.register('Cadastrar_Medicos', Cadastrar_MedicosViewSet, basename='Cadastrar_Medicos')
router.register('Agenda', AgendaViewSet, basename='Agenda')
router.register('Clientes', ClientesViewSet, basename='Clientes')
router.register('Consultas', ConsultasViewSet, basename='Consultas')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('clientes/', include('clientes.urls', namespace="clientes")),
    path('consultas/', include('consultas.urls', namespace="consultas")),
]
