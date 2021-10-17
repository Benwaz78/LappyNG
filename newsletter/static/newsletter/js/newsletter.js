$('#homeNewsLetter').submit( function(event) {
        event.preventDefault();
        var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.is_taken) {
           $("#successMessage").html("")
           $("#errorMessage").html("<div class='alert alert-danger'>"+data.error_message+"</div>")
            // document.getElementById("requestForm").reset();

        }
        else {
            $("#errorMessage").html("")
            $("#successMessage").html("<div class='alert alert-success'>"+data.success+"</div>")
        }
        
      }
    });
    return false;
});