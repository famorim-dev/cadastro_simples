from django.db import models
from django.contrib.auth.models import User


# class Categoria(models.Model):
#     categoria = models.CharField(max_length=60)
    
class Registro(models.Model):
    nome = models.CharField(max_length= 50)
    sobrenome = models.CharField(max_length= 100)
    telefone = models.CharField(max_length=15, null=True)
    email = models.EmailField(unique = True, max_length=254)
    data_criacao = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True)
    # categoria = models.ForeignKey(Categoria, blank=True, on_delete=models.SET_NULL, null=True)

    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='registros')