$(document).ready(function(){
	var MostaForm = function(){
		var btn = $(this);
		$.ajax({
			url: btn.attr("data-url"),
			type: 'get',
			dataType:'json',
			beforeSend: function(){
				$('#modal-category').modal('show');
			},
			success: function(data){
				$('#modal-category .modal-content').html(data.html_form);
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
					$('#table-category>tbody').html(data.category_list);
					$('#modal-category').modal('hide');
				} else {
					$('#modal-category .modal-content').html(data.html_form)
				}
			},
		});
		return false;
	};

	// create
	$(".show-form").click(MostaForm);
	$("#modal-category").on("submit",".create-form",SalvaForm);

	//update
	$('#table-category').on("click",".show-form-update",MostaForm);
	$('#modal-category').on("submit",".update-form",SalvaForm);

	//delete
	$('#table-category').on("click",".show-form-delete",MostaForm);
	$('#modal-category').on("submit",".delete-form",SalvaForm);

});