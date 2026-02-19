from django.shortcuts import render
from .models import Produto
from .models import Cliente

def index(request):
    context = {'curso': 'Desenvolvimento de Sistemas' } # Passa para o template
    return render(request, 'index.html', context)  # Renderiza o template

def contatos(request):
    context = {'nome': 'Bruna' } # Passa para o template
    return render(request, 'contatos.html', context)  # Renderiza o template

def produtos(request):
    produtos = Produto.objects.all()# Pega todos os produtos do banco
    context = {'prod': produtos}    # Passa para o template
    return render(request, 'produtos.html', context)    # Renderiza o template

def clientes(request):
    clientes = Cliente.objects.all()  # Pega todos os clientes do banco
    context = {'clientes': clientes}  # Passa para o template
    return render(request, 'clientes.html', context)  # Renderiza o template
