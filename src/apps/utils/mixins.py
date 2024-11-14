from django.shortcuts import render, redirect
from django.core.exceptions import PermissionDenied

class VerificarPermisosMixins:
    permiso_requerido = None

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("login")
        print("equest.user.es_admin", request.user.es_admin)
        if not request.user.es_admin:
            raise PermissionDenied
            # return redirect("error_permisos")

        print("Permiso requerido-->", self.permiso_requerido)
        if not request.user.has_perm(self.permiso_requerido):
            return redirect("error_permisos")

        return super(VerificarPermisosMixins, self).dispatch(request, *args, **kwargs)
