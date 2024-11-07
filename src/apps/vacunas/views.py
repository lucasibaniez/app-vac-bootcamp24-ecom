# from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic import UpdateView, DetailView
from django.views.generic.edit import DeleteView
from .models import Vacuna, Dosis


class Listar(ListView):
    template_name = 'vacunas/lista.html'
    model = Vacuna
    context_object_name = "vacunas"
    paginate_by = 20

    def get_context_data(self, **kwargs):
        ctx = super(Listar, self).get_context_data(**kwargs)
        ctx["titulo"] = "LISTA DE VACUNAS"
        return ctx

class VacunaUpdate(UpdateView):
    model = Vacuna
    fields = ['codigo', 'nombre', 'ca_dosis']
    template_name = 'vacunas/editar.html'
    success_url = reverse_lazy('vacunas:lista')  # Redirigir a la lista de vacunas después de la edición

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Vacuna'
        return context

class VacunaDetail(DetailView):
    model = Vacuna
    template_name = 'vacunas/detalle.html'
    context_object_name = 'vacuna'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dosis'] = Dosis.objects.filter(vacuna=self.object)
        return context

class VacunaDeleteView(DeleteView):
    model = Vacuna
    template_name = 'vacunas/confirmar_eliminacion.html'
    success_url = reverse_lazy('vacunas:lista')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dosis'] = Dosis.objects.filter(vacuna=self.object)
        return context