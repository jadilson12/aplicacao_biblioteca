from django.shortcuts import render, redirect
from core.forms import LivroForm
from core.models import Livro


def home(resquest):
    return render(resquest, 'core/index.html')


def lista_livro(request):
    livros = Livro.objects.all()
    form = LivroForm()
    data = {'livros': livros, 'form': form}
    return render(request, 'core/livros.html', data)


def novo_livro(request):
    form = LivroForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_livros')
