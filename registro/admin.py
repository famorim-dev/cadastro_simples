from django.contrib import admin
from registro import models

@admin.register(models.Registro)
class RegistroAdmin(admin.ModelAdmin):
    list_display = 'id', 'nome', 'sobrenome', 'telefone',
    ordering = '-id',
    list_filter = 'data_criacao',
    search_fields = 'id', 'nome', 'sobrenome', 'telefone', 

# @admin.register(models.Categoria)
# class CategoriaAdmin(admin.ModelAdmin):
#     list_display = 'categoria',
#     orderning = '-id',