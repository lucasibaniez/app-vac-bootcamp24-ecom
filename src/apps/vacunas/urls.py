from tkinter.font import names

from django.urls import path
from . import views

app_name = "vacunas"

urlpatterns = [
    # lista vacunas
    path('lista/', views.Listar.as_view(), name="lista"), # tarea: hacer busqueda
    # crear vacuna  -> tarea
    path('nuevo/', views.Nuevo.as_view(), name="nuevo"), # tarea: hacer busqueda
    # editar vacuna
    path('vacuna/editar/<int:id_vacuna>/', views.VacunaUpdate.as_view(), name='editar'),
    # detalle vacuna
    path('vacuna/<int:pk>/', views.VacunaDetail.as_view(), name='detalle'),
    # eliminar vacuna
    path('vacuna/<int:pk>/eliminar',views.VacunaDeleteView.as_view(), name='eliminar')

]