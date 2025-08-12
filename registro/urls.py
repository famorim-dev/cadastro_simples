from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required



urlpatterns = [
    path('', login_required(views.listar_registro), name = 'registro'),
    path('<int:info_user>/', login_required(views.exibiruser), name = 'usuario'),
    path('search/', login_required(views.pesquisa), name = 'search'),
    path('registrar/', login_required(views.registrar), name = 'registrar'),
    path('editar/<int:id>/', login_required(views.editarUsuario), name = 'editar'),
    path('deletar/<int:id>/', login_required(views.deletarUsuario), name = 'deletar'),

    # URLS DE LOGIN
    path('user/criar', views.criarUser, name = 'criarUser'),
    path('login/', views.loginUser, name = 'login'),
    path('perfil/editar', login_required(views.editarPerfil), name = 'editarPerfil'),
    path('logout/', login_required(views.logoutUser), name='logout')
]
