from django.urls import path
from registro import views

urlpatterns = [
    path('', views.registro, name = 'registro')
]