
// cadastrar  livros

$('#form_livro').submit(function(event) {
    event.preventDefault();
  var urlredirect = $(this).data('urlredirect');
  $.ajax({
    url: this.action,
    type: 'POST',
    data: $(this).serialize(),
    dataType: 'json',
    success: function(data){
        location.href = urlredirect;
    },
    error: function(error){
      console.error(error.toString());
    }
  });
});

// Preencher o formulário para editar

function editar(id){
       $.getJSON('/api/livros/' + id  + '/', function(livros) {
        //console.log(livros);
        $('#id').val(livros.id);
        $('#id_nome').val(livros.nome);
        $('#id_autor').val(livros.autor);
        $('#id_editora').val(livros.editora);
        $('#id_lancamento').val(livros.lancamento);
        $('#id_categoria').val(livros.categoria);
        $('#id_resumo').val(livros.resumo);
        $('#modal_livro_edit').modal('show');
    });
}

$("#modal_livro_edit").submit(function(event) {
    event.preventDefault();
    salvarLivro()
});

// Delete livro
function remover(id) {
    $.ajax({
        type: "DELETE",
        url: '/api/livros/' + id + '/',
        context: this,
        success: function() {
           // $("#modal_aviso_delete").modal('show');
            linhas = $("#tabela_livros>tbody>tr");
            e = linhas.filter( function(i, elemento) {
                return elemento.cells[0].textContent == id;
            });
            if (e)
                e.remove();
        },
        error: function(error) {
            console.log(error);
        }
    });
}
// Salvar livro apos editar
function salvarLivro() {
      livro = {
        id: $("#id").val(),
        nome: $("#id_nome").val(),
        autor: $("#id_autor").val(),
        editora: $("#id_editora").val(),
        lancamento: $("#id_lancamento").val(),
        categoria: $("#id_categoria").val(),
        resumo: $("#id_resumo").val(),

    };
    $.ajax({
        type: "POST",
        url: "/api/livros/update/" + livro.id + '/',
        context: this,
        data: livro,
        success:function(data, response,textStatus,){
            console.log('salvei', textStatus, response);
        },
        error: function(jqXHR,response, textStatus, errorThrown) {
           // console.log(response)
            console.error(error.toString());
        }
    })
}