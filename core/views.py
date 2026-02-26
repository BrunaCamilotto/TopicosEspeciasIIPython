from django.shortcuts import render, redirect 
from django.http import HttpResponse
from .models import Produto, Cliente
from django.urls import re_path
import re
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def index(request):
    if not request.user.is_authenticated:
        return redirect('naoLogado')
    context = {'curso': 'Desenvolvimento de Sistemas' } # Passa para o template
    return render(request, 'index.html', context)  # Renderiza o template


def contatos(request):
    if not request.user.is_authenticated:
        return redirect('naoLogado') 
    context = {'nome': 'Bruna' } # Passa para o template
    return render(request, 'contatos.html', context)  # Renderiza o template



def produtos(request):
    if not request.user.is_authenticated:
        return redirect('naoLogado') 

    produtos = Produto.objects.all()# Pega todos os produtos do banco
    context = {'prod': produtos}    # Passa para o template
    return render(request, 'produtos.html', context)    # Renderiza o template


def clientes(request):
    if not request.user.is_authenticated:
        return redirect('naoLogado')
    clientes = Cliente.objects.all()  # Pega todos os clientes do banco
    context = {'clientes': clientes}  # Passa para o template
    return render(request, 'clientes.html', context)  # Renderiza o template

def cadastraClientes(request):
     if not request.user.is_authenticated:
        return redirect('naoLogado')
     
     return render(request, 'cadastraClientes.html')  # Renderiza o template

def editaCliente(request, id):
    if not request.user.is_authenticated:
        return redirect('naoLogado')

    cliente = Cliente.objects.get(id=id)

    if request.method == "POST":
        cliente.nome = request.POST.get('nome')
        cliente.sobrenome = request.POST.get('sobrenome')
        cliente.email = request.POST.get('email')
        cliente.data_nascimento = request.POST.get('data_nascimento')

        # remove máscara antes de salvar
        cliente.cpf = re.sub(r'\D', '', request.POST.get('cpf'))
        cliente.telefone = re.sub(r'\D', '', request.POST.get('telefone'))

        cliente.save()
        return redirect('urlclientes')

    return render(request, 'editaCliente.html', {'cliente': cliente})

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

def deletaCliente(request, id):
    cliente = Cliente.objects.get(id=id)
    cliente.delete()
    return redirect ('urlclientes')



def loginTela(request):
    if request.method == "GET":
        return render(request, "loginTela.html")

    elif request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("index")
        else:
            messages.error(request, "Usuário ou senha inválidos 😢")

    return render(request, "loginTela.html")

def logoutTela(request):
    logout(request)
    return redirect('loginTela')

def naoLogado(request):
    return render(request, 'naoLogado.html')