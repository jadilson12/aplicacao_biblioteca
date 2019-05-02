from django.shortcuts import render


def home(resquest):
    return render(resquest, 'core/index.html')


def livros(resquest):
    return render(resquest, 'core/livros.html')
