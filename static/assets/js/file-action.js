$(document).ready(function(){
    $(".card_click").click(function(){
        $(".selected-file-details").removeClass("d-none");
        var tablename = $(this).data('tablename');
        var tablesize = $(this).data('tablesize');


        $(".file-details-title").text(tablename);
        $(".file-details-size").text(tablesize);
        
    });

});