from django.urls import path

from . import views

app_name = "pacientes"

urlpatterns = [
    path('lista/', views.Lista.as_view(), name="lista"),
    # path('lista/', views.lista, name="lista"),
    # path('nuevo/', views.nuevo, name="nuevo"),
    path('nuevo/', views.Nuevo.as_view(), name="nuevo"),
]