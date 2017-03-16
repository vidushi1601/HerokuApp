$(function() {
    $('#btnshow').click(function() {
 
        $.ajax({
            url: '/api1',
            type: 'GET',
            success: function(response) {
                // here you do whatever you want with the response variable
              }
        });
    });
});