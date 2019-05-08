$(document).ready(function(){
	var MostaForm = function(){
		var btn = $(this);
		$.ajax({
			url: btn.attr("data-url"),
			type: 'get',
			dataType:'json',
			beforeSend: function(){
				$('#modal-categoria').modal('show');
			},
			success: function(data){
				$('#modal-categoria .modal-content').html(data.html_form);
			}
		});
	};

	/**
	 * @return {boolean}
	 */
	var SalvaForm =  function(){
		var form = $(this);
		$.ajax({
			url: form.attr('data-url'),
			data: form.serialize(),
			type: form.attr('method'),
			dataType: 'json',
			success: function(data){
				if(data.form_is_valid){
					$('#table-categoria>tbody').html(data.categoria_list);
					$('#modal-categoria').modal('hide');
				} else {
					$('#modal-categoria .modal-content').html(data.html_form)
				}
			},
		});
		return false;
	};

	// create
	$(".show-form").click(MostaForm);
	$("#modal-categoria").on("submit",".create-form",SalvaForm);

	//update
	$('#table-categoria').on("click",".show-form-update",MostaForm);
	$('#modal-categoria').on("submit",".update-form",SalvaForm);

	//delete
	$('#table-categoria').on("click",".show-form-delete",MostaForm);
	$('#modal-categoria').on("submit",".delete-form",SalvaForm);

});