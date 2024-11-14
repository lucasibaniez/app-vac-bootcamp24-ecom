from django.shortcuts import render, redirect


def verificar_permisos():
    def deco_verificar_permisos(f):
        def check(request, *arg, **kwargs):
            print("ESTOY DENTRO DE UN DECORADOR")
            print(request.user)
            if not request.user.is_authenticated:
                return redirect("login")
            # if not request.user.is_superuser and not request.user.es_admin: #
            #     return redirect("error_permisos")
            return f(request, *arg, **kwargs)

        return check

    return deco_verificar_permisos
