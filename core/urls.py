from django.urls import path
from .views import index, contatos, produtos, clientes

urlpatterns = [
    path('', index, name="index"),                    # Página inicial
    path('contatos/', contatos, name="contatos"),    # Contatos
    path('produtos/', produtos, name="produtos"),    # Lista de produtos
    path('clientes/', clientes, name="clientes"),    # Lista de clientes
]
