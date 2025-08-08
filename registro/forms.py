from registro.models import Registro
from django import forms

class RegistroForm(forms.ModelForm):
    class Meta:
        model = Registro
        fields = ('nome', 'sobrenome', 'telefone', 'email', 'description')