from django import forms

from .models import Usuario

class FormUsuario(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ["password", "username", "first_name", "last_name", "email", "is_active", "dni"]