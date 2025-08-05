from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_registro, name = 'registro'),
    path('<int:info_user>/', views.exibiruser, name = 'usuario')
]