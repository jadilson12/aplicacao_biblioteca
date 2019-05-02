from django.urls import path
from core import views as v

urlpatterns = [
    path('', v.home, name='core_home'),
    path('livros/', v.lista_livro, name='core_livros'),
    path('livros/novo', v.novo_livro, name='core_novo_livro'),
]
