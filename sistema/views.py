from django.http import HttpResponse, HttpResponseNotAllowed, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from sistema.forms import LivroForm
from sistema.models import Livro
from sistema.serializers import LivroSerializer


def home(resquest):
    return render(resquest, 'sistema/index.html')


def lista_livro(request):
    livros = Livro.objects.all()
    form = LivroForm()
    data = {'livros': livros, 'form': form}
    return render(request, 'sistema/livros_lista.html', data)


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

