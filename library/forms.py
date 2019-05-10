from django.forms import ModelForm, DateInput
from .models import Category, Book


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        widgets = {
            'publication_date': DateInput(attrs={'type': 'date'})
        }