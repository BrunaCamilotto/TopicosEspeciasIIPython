from django.urls import path
from .views import index, contatos, produtos, clientes, cadastraClientes, salvarClientes

urlpatterns = [
    path('', index, name="index"),                    # Página inicial
    path('contatos/', contatos, name="contatos"),    # Contatos
    path('produtos/', produtos, name="produtos"),    # Lista de produtos
    path('clientes/', clientes, name="urlclientes"),    # Lista de clientes
    path('cadastraClientes/', cadastraClientes, name="cadastraClientes"),   #Cadastro de clientes
    path('salvarClientes/', salvarClientes, name='salvarClientes'), #Salva novos clientes
]
