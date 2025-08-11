from django.urls import path
from . import views



urlpatterns = [
    path('', views.listar_registro, name = 'registro'),
    path('<int:info_user>/', views.exibiruser, name = 'usuario'),
    path('search/', views.pesquisa, name = 'search'),
    path('registrar/', views.registrar, name = 'registrar'),
    path('editar/<int:id>/', views.editarUsuario, name = 'editar'),
    path('deletar/<int:id>/', views.deletarUsuario, name = 'deletar')
]
