from django.urls import path
from sistema import views as v

urlpatterns = [
    path('', v.home, name='sistema_home'),
    path('livros/', v.lista_livro, name='sistema_livros'),

    # api
    path('api/livros', v.livroApiList, name='livrosApiList'),
    path('api/livros/store', v.livro_store, name='livros_store'),
    path('api/livros/<int:id>/', v.livro_detail, name='livroApiDetail'),
    path('api/livros/update/<int:id>/', v.livro_update, name='livro_update'),

]
