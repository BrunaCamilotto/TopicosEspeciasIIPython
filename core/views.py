from django.shortcuts import render

def index(request):
    context = {'curso': 'Desenvolvimento de Sistemas' }
    return render(request, 'index.html', context)

def contatos(request):
    context = {'nome': 'Bruna' }
    return render(request, 'contatos.html', context)

