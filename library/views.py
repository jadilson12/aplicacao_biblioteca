from django.shortcuts import render
from library.services import (
    category_services,
    book_services
)


def page_home(resquest):
    return render(resquest, 'index.html')


def page_book(resquest):
    return render(resquest, 'livros_lista.html')


# Category
def category_list(request):
    data = category_services.list(request)
    return data


def category_create(request):
    data = category_services.create(request)
    return data


def category_update(request, id):
    data = category_services.update(request, id)
    return data


def category_delete(request, id):
    data = category_services.delete(request, id)
    return data


# book
def book_list(request):
    data = book_services.list(request)
    return data


def book_create(request):
    data = book_services.create(request)
    return data


def book_update(request, id):
    data = book_services.update(request, id)
    return data


def book_delete(request, id):
    data = book_services.delete(request, id)
    return data
