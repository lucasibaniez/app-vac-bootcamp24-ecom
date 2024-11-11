from django.shortcuts import render, redirect

from .forms import FormUsuario, FormUser
from .models import Usuario


def nuevo(request):
    template_name = 'usuarios/nuevo_new.html'
    # form = FormUsuario()
    form = FormUser()
    message = ""
    if request.method == 'POST':
        form = FormUser(request.POST)
        if form.is_valid():
            form.save()
            return redirect("usuarios:lista")
        else:
            message = "No se pudo guardar de forma correcta el formulario"

    ctx = {
        "formUsuario": form,
        "message": message
    }
    return render(request, template_name, ctx)


def lista_usuarios(request):
    usuarios = Usuario.objects.all()  # filter(id__in=[1,2,3])#
    """
    u = Usuario.objects.filter(id=1).first()
    # u = Usuario.objects.get(id=5)
    print("TODOS LOS USUARIOS")
    if u is None:
        print("no existe")
    else:

        print(u)
        # print(u.query)
        #u = u[0]
        print(u.username)
    
    print("long:", len(usuarios))
    print("long:", usuarios.count())
    for us in usuarios:
        print(us.last_login)
    """
    ctx = {
        "usuarios": usuarios,
        "titulo": "LISTA DE USUARIOS"
    }
    return render(request, 'usuarios/lista_new.html', ctx)
