from registro.models import Registro
from django import forms
from django.contrib.auth.forms import UserCreationForm

class RegistroForm(forms.ModelForm):
    class Meta:
        model = Registro
        fields = ('nome', 'sobrenome', 'telefone', 'email', 'description')

class CreateUser(UserCreationForm):
    ...