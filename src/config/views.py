from tempfile import template

from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login as login_django
from django.views.generic import TemplateView

from apps.utils.decorators import verificar_permisos


@verificar_permisos()
def mi_pagina_inicio(request):
    lista_usuarios = [
        {"nombre": "Lucas", "apellido": "Ibañez"},
        {"nombre": "Federico", "apellido": "Aguirre"},
        {"nombre": "Raul", "apellido": "Rolon"},
    ]
    contexto = {
        "todo_los_usuarios": lista_usuarios,
        "usuario_autenticado": "Lucas Ibañez",
        "TITULO": "INICIO"
    }
    return render(request, 'mi_pagina_inicio_new.html', contexto)


def login(request):
    # print("=========================")
    # print("method", request.method)
    # print(request)
    # print(request.__class__.__name__)
    # print(request.__dict__)
    """
    print("PARAMETROS GET--> ", request.GET)
    username = request.GET.get("username", default=None)
    password = request.GET.get("password", default=None)    
    """
    se_autentico = False
    salio_mal = True
    username = ""
    if request.method == "POST":
        username = request.POST.get("username", default=None)
        password = request.POST.get("password", default=None)
        usuario = authenticate(request, username=username, password=password)
        se_autentico = True
        if usuario:
            salio_mal = False
            login_django(request, usuario)
            return redirect("inicio")
        else:
            print("autenticacion mal")

    ctx = {
        "se_autentico": se_autentico,
        "salio_mal": salio_mal,
        "username": username
    }
    return render(request, 'login_new.html', ctx)


class BaseTemplateView(TemplateView):
    template_name = "blank.html"


def pagina_error_permisos(request):
    template_name = 'paginas/error_permisos.html'

    ctx = {
    }
    return render(request, template_name, ctx)