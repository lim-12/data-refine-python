$(document).ready(function() {
    $('#output').click(function() {
        var url = $('#url').val();
        var type = $('#type').val();
        var bundle_unit = $('#bundle_unit').val();

        $.ajax({
            url: '/refine',
            type: 'POST',
            data: {'url':url, 'type':type,'bundle_unit':bundle_unit},
            dataType: 'json',
            success: function(res){
                $('#quotient').empty();
                $('#remainder').empty();
                $('#quotient').append(res['quotient']);
                $('#remainder').append(res['remainder']);
            },
            error: function(error){
                console.log(error);
            }
        });
    });
});