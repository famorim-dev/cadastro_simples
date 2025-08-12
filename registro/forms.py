from registro.models import Registro
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class RegistroForm(forms.ModelForm):
    class Meta:
        model = Registro
        fields = ('nome', 'sobrenome', 'telefone', 'email', 'description')

#criar usuario de login

class CreateUser(UserCreationForm):
    first_name = forms.CharField(
        label="Nome",
        required=True,
        min_length=2,
        max_length=30,
        widget=forms.TextInput(attrs={'placeholder': 'Digite seu nome'})
    )

    last_name = forms.CharField(
        label="Sobrenome",
        required=True,
        min_length=2,
        max_length=50,
        widget=forms.TextInput(attrs={'placeholder': 'Digite seu sobrenome'})
    )

    email = forms.EmailField(
        label="E-mail",
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'Digite seu e-mail'})
    )

    username = forms.CharField(
        label="Usuário",
        required=True,
        min_length=4,
        max_length=20,
        widget=forms.TextInput(attrs={'placeholder': 'Digite seu nome de usuário'})
    )

    password1 = forms.CharField(
        label="Senha",
        required=True,
        min_length=8,
        widget=forms.PasswordInput(attrs={'placeholder': 'Digite sua senha'})
    )

    password2 = forms.CharField(
        label="Confirme a Senha",
        required=True,
        min_length=8,
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirme sua senha'})
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']

    # Validação: e-mail único
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("Este e-mail já está cadastrado.")
        return email

    # Validação: nome só com letras
    def clean_first_name(self):
        nome = self.cleaned_data.get('first_name')
        if not nome.isalpha():
            raise ValidationError("O nome deve conter apenas letras.")
        return nome

    def clean_last_name(self):
        sobrenome = self.cleaned_data.get('last_name')
        if not sobrenome.isalpha():
            raise ValidationError("O sobrenome deve conter apenas letras.")
        return sobrenome
    
#login de usuario
class EditUserForm(forms.ModelForm):
    first_name = forms.CharField(
        label="Nome",
        required=True,
        min_length=2,
        max_length=30,
        widget=forms.TextInput(attrs={'placeholder': 'Digite seu nome'})
    )

    last_name = forms.CharField(
        label="Sobrenome",
        required=True,
        min_length=2,
        max_length=50,
        widget=forms.TextInput(attrs={'placeholder': 'Digite seu sobrenome'})
    )

    email = forms.EmailField(
        label="E-mail",
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'Digite seu e-mail'})
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

    # Validação de e-mail único
    def clean_email(self):
        email = self.cleaned_data.get('email')
        user_id = self.instance.id

        if User.objects.exclude(id=user_id).filter(email=email).exists():
            raise ValidationError("Este e-mail já está em uso por outro usuário.")
        return email

    # Validação extra para nome
    def clean_first_name(self):
        nome = self.cleaned_data.get('first_name')
        if not nome.isalpha():
            raise ValidationError("O nome deve conter apenas letras.")
        return nome

    def clean_last_name(self):
        sobrenome = self.cleaned_data.get('last_name')
        if not sobrenome.isalpha():
            raise ValidationError("O sobrenome deve conter apenas letras.")
        return sobrenome