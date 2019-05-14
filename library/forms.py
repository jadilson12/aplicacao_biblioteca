from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, DateInput, forms
from .models import Category, Book
from django import forms


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


class SignUpForm(UserCreationForm):
    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')

    class Meta:
        model = User
        fields = ('username', 'birth_date', 'password1', 'password2', )