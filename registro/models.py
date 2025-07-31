from django.db import models

class registro(models.Model):
    nome = models.CharField(max_length= 50)
    sobrenome = models.CharField(max_length= 100)
    telefone = models.CharField(max_length=15, null=True)
    email = models.EmailField(unique = True, max_length=254)
    data_criacao = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True)