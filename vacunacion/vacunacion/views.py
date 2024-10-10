from django.shortcuts import render

def mi_pagina_inicio(request):
    contexto = {}
    return render(request, 'mi_pagina_inicio.html', contexto)