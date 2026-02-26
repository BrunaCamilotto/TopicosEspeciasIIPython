from django.db import models
from localflavor.br.models import BRCPFField


class Produto(models.Model):
    nome = models.CharField(max_length=50)
    preco = models.DecimalField(decimal_places=2, max_digits=8)
    descricao = models.CharField(max_length=200)
    quantidade = models.PositiveIntegerField(default=0)
    data_de_validade = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.nome


class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    data_nascimento = models.DateField(null=True, blank=True)
    cpf = models.CharField(max_length=11)
    
    #cpf = BRCPFField(unique=True)
    telefone = models.CharField(max_length=14)
    email = models.EmailField(max_length=254)
    def __str__(self):
        return self.nome
