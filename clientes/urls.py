
from django.urls import path
from .views import *

urlpatterns = [
    path('listar', listar_clientes, name='listar_clientes'),
    path('cadastrar', cadastrar_cliente, name='cadastrar_cliente'),
    path('listar/<int:id>', listar_cliente_id, name='listar_cliente_id'),
    path('editar/<int:id>', editar_cliente, name='editar_cliente'),
    path('remover/<int:id>', remover_cliente, name='remover_cliente'),
    path('cadastrar_usuario/', cadastrar_usuario, name='cadastrar_usuario'),
    path('logar_usuario/', logar_usuario, name='logar_usuario'),
    path('deslogar_usuario/', deslogar_usuario, name='deslogar_usuario'),
]