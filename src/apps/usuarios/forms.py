from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm


from .models import Usuario

class FormUsuario(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ["password", "username", "first_name", "last_name", "email", "is_active", "dni"]

class FormUser(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ["username", "first_name", "last_name", "email", "is_active", "dni"]

    def clean_dni(self):
        dni = self.cleaned_data["dni"]
        if not ( 7 <= len(str(dni)) <=8 ):
            raise ValidationError("el dni debe tener entre 7 y 8 digitos numericos")
        print(dni.__class__.__name__)
        return dni
