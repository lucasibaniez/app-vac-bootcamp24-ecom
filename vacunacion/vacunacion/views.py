from django.shortcuts import render

def mi_pagina_inicio(request):
    lista_usuarios = [
        {"nombre": "Lucas", "apellido": "Ibañez"},
        {"nombre": "Federico", "apellido": "Aguirre"},
        {"nombre": "Raul", "apellido": "Rolon"},
    ]
    contexto = {
        "todo_los_usuarios": lista_usuarios,
        "usuario_autenticado": "Lucas Ibañez"
    }
    return render(request, 'mi_pagina_inicio.html', contexto)

def lista_usuarios(request):
    return render(request, 'lista_usuarios.html', {})

def lista_pacientes(request):
    return render(request, 'lista_pacientes.html', {})