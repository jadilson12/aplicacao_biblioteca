from django.urls import path
from library import views as v

urlpatterns = [
    path('', v.page_home, name='home'),
    # path('livros/', v.page_book, name='books'),
    # path('categoria/', v.category_list, name='category'),

    # book
    path('livros/', v.book_list, name='book.list'),
    path('livros/criar', v.book_create, name='book.create'),
    path('livros/atualizar/<int:id>', v.book_update, name='book.update'),
    path('livros/excluir/<int:id>', v.book_delete, name='book.delete'),
    path('livros/visualizar/<int:id>', v.book_view, name='book.view'),
    path('livros/reserve', v.book_reserve, name='book.reserve'),

    # category
    path('categoria/', v.category_list, name='category.list'),
    path('categoria/criar', v.category_create, name='category.create'),
    path('categoria/atualizar/<int:id>', v.category_update, name='category.update'),
    path('categoria/excluir/<int:id>', v.category_delete, name='category.delete'),

    # reserve
    path('reserve/', v.reserve_list, name='reserve.list'),


    # user
    path('signup/', v.signup, name='signup'),
    path('profile/', v.profile, name='profile'),

]
