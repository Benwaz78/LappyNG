$('#reviewForm').submit( function(event) {
    event.preventDefault();
    var form = $(this);
    // console.log(form.serialize());

$.ajax({
  url: form.attr("data-review-url"),
  data: form.serialize(),
  type: 'POST',
  dataType: 'json',
  success: function (data) {
    if (data.success) {
      console.log(data.success);
      // alert(data.success);
      $("#reviewSuccess").html("<div class='alert alert-success'>"+data.success+"</div>");
      $("#reviewsData").html(data.html_data);
    }else{
        $("#reviewSuccess").html("<div class='alert alert-danger'>"+data.error+"</div>");
    }
    
  }
});
return false;
});


$('#emailForm').submit( function(event) {
  event.preventDefault();
  var form = $(this);
  $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.success) {
          $("#reviewSuccess").html("<div class='alert alert-success'>"+data.success+"</div>");
        }else{
          $("#reviewSuccess").html("<div class='alert alert-danger'>"+data.error_message+"</div>");
        }
        
      }
  });
return false;
});