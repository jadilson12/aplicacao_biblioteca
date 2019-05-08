from django.shortcuts import get_object_or_404, render
from django.template.loader import render_to_string
from django.http import JsonResponse
from library.forms import *
from library.models import *


def list(request):
    books = Book.objects.all()
    data = {'books': books}
    return render(request, 'book/book_list.html', data)


def create(request):
    form = BookForm(request.POST)
    if not request.method == 'POST':
        form = BookForm()
    return save(request, form, 'book/book_create.html')


def save(request, form, template_name):

    # create one dictionary for send to json
    data = dict()

    if request.method == 'POST':
        if form.is_valid():
            form.save()

            # send  feedback for notify to the user
            data['form_is_valid'] = True
            books = Book.objects.all()

            # add the list  tr in the dictionary
            data['book_list'] = render_to_string('book/book_list_tr.html', {'books': books})
        else:
            # send  feedback for notify to the user
            data['form_is_valid'] = False

    # add form if is valid or not
    context = {'form': form}

    # return to front new list updated
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def update(request, id):
    # search the object to be updated
    books = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        # update
        form = BookForm(request.POST, instance=books)
    else:
        # not updated
        form = BookForm(instance=books)
    return save(request, form, 'book/book_update.html')


def delete(request, id):
    data = dict()
    # search the object to be deleted
    books = get_object_or_404(Book, id=id)
    if request.method == "DELETE":
        books.delete()

        # send  feedback for notify to the user
        data['form_is_valid'] = True
        books = Book.objects.all()

        # return to front new list updated
        data['book_list'] = render_to_string('book/book_list_tr.html', {'books': books})
    else:
        context = {'books': books}
        data['html_form'] = render_to_string('book/book_delete.html', context, request=request)

    return JsonResponse(data)