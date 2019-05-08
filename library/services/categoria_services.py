from django.shortcuts import get_object_or_404, render
from django.template.loader import render_to_string
from django.http import JsonResponse
from library.forms import *
from library.models import *


def list(request):
    categorias = Categoria.objects.all()
    data = {'categorias': categorias}
    return render(request, 'categoria_list.html', data)


def create(request):
    form = CategoriaForm(request.POST)
    if not request.method == 'POST':
        form = CategoriaForm()
    return save(request, form, 'categoria_create.html')


def save(request, form, template_name):
    # Cria um dicionário  para enviar para json
    data = dict()

    if request.method == 'POST':
        if form.is_valid():
            form.save()

            # enviar um feedback para notificar ao usuario
            data['form_is_valid'] = True
            categorias = Categoria.objects.all()

            # adiciona as tr da lista para dicionário
            data['categoria_list'] = render_to_string('categoria_list_tr.html', {'categorias': categorias})
        else:
            # enviar um feedback para notificar ao usuario
            data['form_is_valid'] = False

    # adiciona form validadado ou não
    context = {'form': form}

    # retorna para front o novo lista atualizada
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def update(request, id):
    # Localiza o objeto a ser atualizado
    categoria = get_object_or_404(Categoria, id=id)
    if request.method == 'POST':
        # atualiza
        form = CategoriaForm(request.POST, instance=categoria)
    else:
        # Não atualiza
        form = CategoriaForm(instance=categoria)
    return save(request, form, 'categoria_update.html')


def delete(request, id):
    data = dict()

    # Localiza o objeto a ser excluido
    categoria = get_object_or_404(Categoria, id=id)
    if request.method == "POST":
        categoria.delete()
        # enviar um feedback para notificar ao usuario
        data['form_is_valid'] = True

        categorias = Categoria.objects.all()

        # retorna para front o novo lista atualizada
        data['categoria_list'] = render_to_string('categoria_list_tr.html', {'categorias': categorias})
    else:
        context = {'categoria': categoria}
        data['html_form'] = render_to_string('categoria_delete.html', context, request=request)

    return JsonResponse(data)
