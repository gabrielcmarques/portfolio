from django.urls import path
from . import views


urlpatterns = [        
    path('', views.projetosHome, name="projetosHome"),
    path('projeto/<str:pk>/', views.projetoPage, name="projetoPage"),
    path('login/', views.loginUsuario, name="loginUsuario"),
    path('registro/', views.registroUsuario, name="registroUsuario"),
    path('editar-conta/', views.editarConta, name="editar-conta"),
    path('criar-projeto/', views.criarProjeto, name="criar-projeto"),
	path('deletar-projeto/', views.deletarProjeto, name="deletar-projeto"),
    ]