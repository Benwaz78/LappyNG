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


$('.brand-img').click( function(event) {
  event.preventDefault();
  const id = $(this).attr('id');
  var csrftoken = getCookie('csrftoken');
  $.ajax({
      url: "/",
      data: {id:id, csrfmiddlewaretoken:csrftoken},
      type: 'POST',
      dataType: "json",
      success: function (data) {
        console.log(data.html);
        $('#cont').html(data.html)
      }
  });
return false;
});

function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie !== '') {
      var cookies = document.cookie.split(';');
      for (var i = 0; i < cookies.length; i++) {
          var cookie = jQuery.trim(cookies[i]);
          // Does this cookie string begin with the name we want?
          if (cookie.substring(0, name.length + 1) === (name + '=')) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
          }
      }
  }
  return cookieValue;
}


