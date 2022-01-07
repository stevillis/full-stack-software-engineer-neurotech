from django.urls import path

from .views import autenticacao, editar_contato, cadastrar_contato, remover_contato, listar_contatos, home

urlpatterns = [
    path('', autenticacao, name='autenticacao'),
    path('home/', home, name='home'),
    path('contatos/', listar_contatos, name='listar_contatos'),
    path('contatos/inserir', cadastrar_contato, name='cadastrar_contato'),
    path('contatos/editar-contato/<str:pk>', editar_contato, name='editar_contato'),
    path('contatos/remover-contato/<str:pk>', remover_contato, name='remover_contato'),
]
