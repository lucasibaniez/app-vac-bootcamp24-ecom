from django import forms

from .models import Vacuna


class FormVacuna(forms.ModelForm):
    class Meta:
        model = Vacuna
        fields = "__all__"