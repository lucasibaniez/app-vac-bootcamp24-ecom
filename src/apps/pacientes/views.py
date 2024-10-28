from django.shortcuts import render, redirect

from .forms import FormPaciente


def lista(request):
    return render(request, 'pacientes/lista.html', {})

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
