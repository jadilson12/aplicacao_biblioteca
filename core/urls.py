
from django.urls import path
from core import views as v

urlpatterns = [
    path('', v.home, name='core_home'),
    path('livros/', v.livros, name='core_livros'),
]
