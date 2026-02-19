from django.contrib import admin

from .models import Produto
from .models import Cliente

class ProdutoAdm(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'descricao', 'quantidade', 'data_de_validade')

admin.site.register(Produto, ProdutoAdm)


class ClienteAdm(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'data_nascimento', 'cpf',
'telefone', 'email')

admin.site.register(Cliente, ClienteAdm)