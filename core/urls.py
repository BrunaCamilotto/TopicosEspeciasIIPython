from django.urls import path
from .views import index
from .views import contatos
from .views import produtos

urlpatterns = [
    path('', index, name="urlindex"),
    path('contatos', contatos, name="urlcontatos" ),
    path('produtos', produtos, name="urlprodutos" ),
]