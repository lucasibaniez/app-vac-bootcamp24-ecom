from django.urls import path

from . import views

app_name = "usuarios"

urlpatterns = [
    path('lista/', views.lista_usuarios, name="lista"),
    path('nuevo/', views.nuevo, name="nuevo"),
]