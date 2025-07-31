from django.contrib import admin
from registro import models

@admin.register(models.registro)
class registroAdmin(admin.ModelAdmin):
    list_display = 'id', 'nome', 'sobrenome', 'telefone',
    ordering = '-id',
    list_filter = 'data_criacao',
    search_fields = 'id', 'nome', 'sobrenome', 'telefone', 
