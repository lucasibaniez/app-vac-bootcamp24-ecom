from django.urls import path

from . import views

app_name = "pacientes"

urlpatterns = [
    path('lista/', views.lista, name="lista"),
    path('nuevo/', views.nuevo, name="nuevo"),
]