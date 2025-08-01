from django.db import models


class categoria(models.Model):
    categoria = models.CharField(max_length=60)
    
class registro(models.Model):
    nome = models.CharField(max_length= 50)
    sobrenome = models.CharField(max_length= 100)
    telefone = models.CharField(max_length=15, null=True)
    email = models.EmailField(unique = True, max_length=254)
    data_criacao = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True)
    categoria = models.ForeignKey(categoria, blank=True, on_delete=models.SET_NULL, null=True)