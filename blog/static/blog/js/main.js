$(document).on('submit','#myModel',function(event){    
    event.preventDefault()
    var formData = $(this).serialize();
    console.log(formData);
    $.ajax({
        url: "", 
        data: formData,
        datatype: "json",
        type: "POST",
        success: function(data) {}
   });
});
