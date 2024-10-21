from django.shortcuts import render

from .models import Usuario

def lista_usuarios(request):
    usuarios = Usuario.objects.all() # filter(id__in=[1,2,3])#
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
        "usuarios": usuarios
    }
    return render(request, 'usuarios/lista.html', ctx)
