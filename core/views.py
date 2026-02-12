from django.shortcuts import render
from .models import Produto

def index(request):
    context = {'curso': 'Desenvolvimento de Sistemas' }
    return render(request, 'index.html', context)

def contatos(request):
    context = {'nome': 'Bruna' }
    return render(request, 'contatos.html', context)

def produtos(request):
    produtos = Produto.objects.all()
    context = {'prod': produtos}
    return render(request, 'produtos.html', context)

