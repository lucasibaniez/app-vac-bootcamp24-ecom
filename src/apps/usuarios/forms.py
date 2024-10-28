from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm


from .models import Usuario

class FormUsuario(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ["password", "username", "first_name", "last_name", "email", "is_active", "dni"]

class FormUser(UserCreationForm):
    # atributo1 = forms.CharField()
    username = forms.CharField(label="Nombre de usuario", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese un nombre de usuario'}))
    class Meta:
        model = Usuario
        fields = ["username", "first_name", "last_name", "email", "is_active", "dni"]
    
    def __init__(self, *args, **kwargs):
        super(FormUser, self).__init__(*args, **kwargs)

        add_class_form_control = ["first_name", "username", "last_name", "email", "dni", "password1", "password2"]
        
        for attr_field in add_class_form_control:
            self.fields[attr_field].widget.attrs["class"] = "form-control"
        

    def clean_dni(self):
        dni = self.cleaned_data["dni"]
        if not ( 7 <= len(str(dni)) <=8 ):
            raise ValidationError("el dni debe tener entre 7 y 8 digitos numericos")
        print(dni.__class__.__name__)
        return dni
