$(document).ready(function(){
    $('.switch').click(function(){
        var op = $(this).attr('data-op');
        $('#operation').val(op);
        $('#switch').submit();
    });
});
