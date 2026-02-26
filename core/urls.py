from django.urls import path
from .views import index, contatos, produtos, clientes, cadastraClientes, salvarClientes, editaCliente, deletaCliente, loginTela, logoutTela, naoLogado

urlpatterns = [
    path('', index, name="index"),                    # Página inicial
    path('contatos/', contatos, name="contatos"),    # Contatos
    path('produtos/', produtos, name="produtos"),    # Lista de produtos
    path('clientes/', clientes, name="urlclientes"),    # Lista de clientes
    path('cadastraClientes/', cadastraClientes, name="cadastraClientes"),   #Cadastro de clientes
    path('salvarClientes/', salvarClientes, name='salvarClientes'), #Salva novos clientes
    path('editaCliente/<int:id>', editaCliente, name='editaCliente'), # Altera clientes
    path('deletaCliente/<int:id>/', deletaCliente, name='deletaCliente'), #Deleta clientes
    path('loginTela/', loginTela, name='loginTela'), # login de usuarios
    path('logoutTela/', logoutTela, name='logoutTela'), #Logout de usuarios
    path('naoLogado/', naoLogado, name='naoLogado'),
]
