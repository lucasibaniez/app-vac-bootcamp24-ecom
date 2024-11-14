from django.urls import path

from . import apis

urlpatterns = [
    path('', apis.VacunacionesCrearYListar.as_view())
    
]