from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=50)
    preco = models.DecimalField(decimal_places=2, max_digits=8)
    descricao = models.CharField(max_length=200)
    quantidade = models.PositiveIntegerField(default=0)
    data_de_validade = models.DateField(auto_now_add=True)
