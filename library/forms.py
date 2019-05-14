from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, DateInput
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
    cpf = forms.IntegerField(help_text='Required')
    registration_id = forms.IntegerField(help_text='Required')
    phone = forms.IntegerField(help_text='Required')

    class Meta:
        model = User
        fields = ('username', 'email', 'cpf', 'phone', 'registration_id', 'password1', 'password2',)
        # fields = ('username', 'password1', 'email', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Paul'}),
            'email': forms.TextInput(attrs={'placeholder': 'youname@gmail.com'}),
        }

