from django.shortcuts import render, redirect 
from django.http import HttpResponse
from .models import Produto, Cliente

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

def cadastraClientes(request):
     return render(request, 'cadastraClientes.html')  # Renderiza o template


def salvarClientes(request):
    #Recebe o POST do formulário e salva o cliente#
    if request.method == 'POST':
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        cpf = request.POST.get('cpf')
        data_nascimento = request.POST.get('data_nascimento')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')

        # Cria o cliente no banco
        Cliente.objects.create(
            nome=nome,
            sobrenome=sobrenome,
            cpf=cpf,
            data_nascimento=data_nascimento,
            email=email,
            telefone=telefone
        )

        # Redireciona para a lista de clientes após salvar
        return redirect('urlclientes')

    # Caso acesse via GET, apenas redireciona para o formulário
    return redirect('cadastraClientes')