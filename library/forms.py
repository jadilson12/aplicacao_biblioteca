from django.forms import ModelForm
from .models import Categoria, Livro


class CategoriaForm(ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'


class LivroForm(ModelForm):
    class Meta:
        model = Livro
        fields = '__all__'
