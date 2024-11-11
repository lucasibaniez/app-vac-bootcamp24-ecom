from tkinter.font import names

from django.contrib import admin
from django.contrib.auth import views as views_django
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('inicio/', views.mi_pagina_inicio, name="inicio"),
    path('', views.mi_pagina_inicio, name="inicio"),

    path('base', views.BaseTemplateView.as_view(), name='base'),

    # path('login/', views.login, name="login"),
    # path('login/', views_django.LoginView.as_view(), name="login"),
    path('login/', views_django.LoginView.as_view(template_name="login_new.html"), name="login"),
    path('logout/', views_django.logout_then_login, name="logout"),

    path("error-permisos", views.pagina_error_permisos, name="error_permisos"),
    
    # path('usuarios/lista/', views.lista_usuarios, name="lista_de_usuarios"),
    path('usuarios/', include("apps.usuarios.urls")),
    path('pacientes/', include("apps.pacientes.urls")),
    path('vacunas/', include("apps.vacunas.urls")),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


