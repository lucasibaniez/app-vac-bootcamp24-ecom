from django import forms

from .models import Paciente

class FormPaciente(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = "__all__"