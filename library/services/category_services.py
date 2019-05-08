from django.shortcuts import get_object_or_404, render
from django.template.loader import render_to_string
from django.http import JsonResponse
from library.forms import *
from library.models import *


def list(request):
    categories = Category.objects.all()
    data = {'categories': categories}
    return render(request, 'category/category_list.html', data)


def create(request):
    form = CategoryForm(request.POST)
    if not request.method == 'POST':
        form = CategoryForm()
    return save(request, form, 'category/category_create.html')


def save(request, form, template_name):

    # create one dictionary for send to json
    data = dict()

    if request.method == 'POST':
        if form.is_valid():
            form.save()

            # send  feedback for notify to the user
            data['form_is_valid'] = True
            categories = Category.objects.all()

            # add the list  tr in the dictionary
            data['category_list'] = render_to_string('category/category_list_tr.html', {'categories': categories})
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
    categories = get_object_or_404(Category, id=id)
    if request.method == 'POST':
        # update
        form = CategoryForm(request.POST, instance=categories)
    else:
        # not updated
        form = CategoryForm(instance=categories)
    return save(request, form, 'category/category_update.html')


def delete(request, id):
    data = dict()

    # search the object to be deleted
    categories = get_object_or_404(Category, id=id)
    if request.method == "POST":
        categories.delete()
        # send  feedback for notify to the user
        data['form_is_valid'] = True

        categories = Category.objects.all()

        # return to front new list updated
        data['category_list'] = render_to_string('category/category_list_tr.html', {'categories': categories})
    else:
        context = {'categories': categories}
        data['html_form'] = render_to_string('category/category_delete.html', context, request=request)

    return JsonResponse(data)
