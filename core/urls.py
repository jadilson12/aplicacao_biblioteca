from django.urls import path
from core import views as v

urlpatterns = [
    path('', v.home, name='core_home'),
    path('livros/', v.lista_livro, name='core_livros'),

    # api
    path('api/livros', v.livroApiList, name='livrosApiList'),
    path('api/livros/store', v.livro_store, name='livros_store'),
    path('api/livros/<int:id>/', v.livro_detail, name='livroApiDetail'),
    path('api/livros/update/<int:id>/', v.livro_update, name='livro_update'),

]
