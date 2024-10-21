from django.shortcuts import render

def lista_usuarios(request):
    return render(request, 'lista_usuarios.html', {})
