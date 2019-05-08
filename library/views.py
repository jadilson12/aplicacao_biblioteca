from django.http import HttpResponse, HttpResponseNotAllowed, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from .forms import LivroForm, CategoriaForm
from .models import Livro, Categoria
from .serializers import LivroSerializer


def home(resquest): 
    return render(resquest, 'index.html')


def lista_livro(request):
    livros = Livro.objects.all()
    form = LivroForm()
    data = {'livros': livros, 'form': form}
    return render(request, 'livros_lista.html', data)


class JSONResponse(HttpResponse):
    """
    O HttpResponse que renderiza seu conteúdo em JSON.

    """

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

    class JSONResponse(object):
        pass


@csrf_exempt
def livroApiList(request):
    """
    Lista de livros e criar novo livro

    """
    if request.method == 'GET':
        livro = Livro.objects.all()
        serializer = LivroSerializer(livro, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':

        data = JSONParser().parse(request)
        serializer = LivroSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)


@csrf_exempt
def livro_store(request):
    """
    Salvar livro usando api

    """
    # abort if request is not made via POST
    if request.method != 'POST':
        return HttpResponseNotAllowed(['POST'])

    # abort if request is not made via ajax
    if not request.is_ajax():
        error = {'error': 'This resource requires ajax requests.'}
        return JsonResponse(error, status=422)

    # abort if posted data is not valid
    form = LivroForm(request.POST)
    if not form.is_valid():
        error = {'error': form.errors}
        return JsonResponse(error, status=422)

    nome = form.cleaned_data.get('nome')
    autor = form.cleaned_data.get('autor')
    editora = form.cleaned_data.get('editora')
    categoria = form.cleaned_data.get('categoria')
    lancamento = form.cleaned_data.get('lancamento')
    resumo = form.cleaned_data.get('resumo')
    Livro.objects.create(
        nome=nome,
        autor=autor,
        editora=editora,
        categoria=categoria,
        lancamento=lancamento,
        resumo=resumo,

    )
    message = 'salvo.'
    return JsonResponse({'message': message})


def livro_detail(request, id):
    """
    Visualiza, atualiza e exclui livro

    """
    try:
        livro = Livro.objects.get(id=id)
    except Livro.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = LivroSerializer(livro)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = LivroSerializer(livro, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        livro.delete()
        return HttpResponse(status=204)


def livro_update(request, id):
    if request.method == 'POST':
        id = request.POST.get('livro_id')
        livro = get_object_or_404(Livro, id=id)
        form = LivroForm(request.POST, instance=livro)

        if form.is_valid():
            form.save()
            response = {'status': 'atualizado'}
            return JsonResponse(response)

        error = {'error': form.errors}
        return JsonResponse(error, status=422)
    else:
        response = ''
        return JsonResponse(response, )


def categoria_list(request):
    categorias = Categoria.objects.all()
    data = {'categorias': categorias}
    return render(request, 'categoria_list.html', data)


def categoria_create(request):
    form = CategoriaForm(request.POST)
    if not request.method == 'POST':
        form = CategoriaForm()
    return categoria_store(request, form, 'categoria_create.html')


def categoria_store(request, form, template_name):

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


def categoria_update(request, id):

    # Localiza o objeto a ser atualizado
    categoria = get_object_or_404(Categoria, id=id)
    if request.method == 'POST':
        # atualiza
        form = CategoriaForm(request.POST, instance=categoria)
    else:
        # Não atualiza
        form = CategoriaForm(instance=categoria)
    return categoria_store(request, form, 'categoria_update.html')


def categoria_delete(request, id):
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
