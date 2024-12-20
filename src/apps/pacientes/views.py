from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from apps.utils.mixins import VerificarPermisosMixins

from .models import Paciente
from .forms import FormPaciente

"""
def lista(request):
    return render(request, 'pacientes/lista.html', {})
"""


class Lista(VerificarPermisosMixins,ListView):
    template_name = 'pacientes/lista_new.html'
    model = Paciente
    context_object_name = "pacientes"
    paginate_by = 1
    permiso_requerido = 'pacientes.view_paciente'

    def get_context_data(self, **kwargs):
        ctx = super(Lista, self).get_context_data(**kwargs)
        ctx["titulo"] = "LISTA DE PACIENTES"
        return ctx

    def get_queryset(self):
        query = self.model.objects.all()
        nombre = self.request.GET.get('nombre', None)
        if nombre:
            query = query.filter(nombre=nombre)
        return query.order_by("apellido")


class Nuevo(LoginRequiredMixin,CreateView):
    template_name = 'pacientes/nuevo_new.html'
    model = Paciente
    form_class = FormPaciente
    success_url = reverse_lazy("pacientes:lista")

    def get_context_data(self, **kwargs):
        ctx = super(Nuevo, self).get_context_data(**kwargs)
        ctx["titulo"] = "NUEVO PACIENTE"
        return ctx


"""

def nuevo(request):
    template_name = 'pacientes/nuevo.html'
    # form = FormUsuario()
    form = FormPaciente()
    message = ""
    if request.method == 'POST':
        form = FormPaciente(request.POST)
        if form.is_valid():
            form.save()
            return redirect("pacientes:lista")
        else:
            message = "No se pudo guardar de forma correcta el formulario"

    ctx = {
        "form": form,
        "message": message
    }
    return render(request, template_name, ctx) 
"""
