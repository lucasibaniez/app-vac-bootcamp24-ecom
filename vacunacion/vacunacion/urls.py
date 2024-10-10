
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/', views.mi_pagina_inicio, name="inicio"),
    path('usuarios/lista/', views.lista_usuarios, name="lista_de_usuarios"),
    path('pacientes/lista/', views.lista_pacientes, name="lista_de_pacientes")
]
