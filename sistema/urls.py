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

    path('categoria/', v.categoria_list, name='categoria_list'),
    path('categoria/create', v.categoria_create, name='categoria_create'),
    path('categoria/<int:id>/update/', v.categoria_update, name='categoria_update'),
    path('categoria/<int:id>/delete/', v.categoria_delete, name='categoria_delete'),
]
