from django.shortcuts import render
from library.services import categoria_services


def home(resquest):
    return render(resquest, 'index.html')


def categoria_list(request):
    data = categoria_services.list(request)
    return data


def categoria_create(request):
    data = categoria_services.create(request)
    return data


def categoria_update(request, id):
    data = categoria_services.update(request, id)
    return data


def categoria_delete(request, id):
    data = categoria_services.delete(request, id)
    return data
