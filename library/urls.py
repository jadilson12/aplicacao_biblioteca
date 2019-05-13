from django.urls import path
from library import views as v

urlpatterns = [
    path('', v.page_home, name='home'),
    # path('livros/', v.page_book, name='books'),
    # path('categoria/', v.category_list, name='category'),

    # book
    path('livros/', v.book_list, name='book.list'),
    path('api/livros/criar', v.book_create, name='book.create'),
    path('api/livros/atualizar/<int:id>', v.book_update, name='book.update'),
    path('api/livros/excluir/<int:id>', v.book_delete, name='book.delete'),

    # category
    path('categoria/', v.category_list, name='category.list'),
    path('categoria/criar', v.category_create, name='category.create'),
    path('categoria/atualizar/<int:id>', v.category_update, name='category.update'),
    path('categoria/excluir/<int:id>', v.category_delete, name='category.delete'),

    # user
    path('signup/', v.signup, name='signup'),

]
