from django.shortcuts import render, redirect
from library.forms import *
from library.models import *


def list(request):
    books = Book.objects.all()
    form = BookForm()
    data = {'books': books, 'form': form}
    return render(request, 'book/book_list.html', data)


def create(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('book.list')
    else:
        form = BookForm()
        return render(request, 'book/book_update.html', {'form': form})


def update(request, id):
    data = {}
    book = Book.objects.get(id=id)
    form = BookForm(request.POST, request.FILES, instance=book)
    data['book'] = book
    data['form'] = form
    data['category'] = Category.objects.all()
    print(data)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('book.list')
    else:
        return render(request, 'book/book_update.html', data)


def delete(request, id):
    book = Book.objects.get(id=id)
    if request.method == 'POST':
        book.delete()
        return redirect('book.list')
    else:
        return render(request, 'book/book_create.html')
