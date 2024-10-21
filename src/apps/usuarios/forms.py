from django import forms
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