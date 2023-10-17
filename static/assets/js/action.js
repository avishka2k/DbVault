$(document).ready(function(){
    $(".editable").click(function(){
        var id = $(this).data('id');
        var field = $(this).data('field');
        var value = $(this).text();

        $("#edit_id").val(id);
        $("#edit_field").val(field);
        $("#edit_value").val(value);

        $("#editModal").modal('show');
    });
});

$(document).ready(function(){
    $(".editablerow").click(function(){
        var value = $(this).text();

        $("#edit_value").val(value);

        $("#editRowModal").modal('show');
    });
});

function updateValue() {
    var cell_id = $("#edit_id").val();
    var field = $("#edit_field").val();
    var value = $("#edit_value").val();

    $.post("/edit/" + cell_id, {
        field: field,
        value: value
    }, function(data){
        $("#editModal").modal('hide');
        location.reload();
    });
}

//$("#insertForm").submit(function(event){
//    event.preventDefault();
//    var name = $("#new_name").val();
//    var age = $("#new_age").val();
//
//    $.post("/insert", {
//        new_name: name,
//        new_age: age
//    }, function(data){
//        location.reload();
//    });
//});

$('#insertForm').submit(function(e) {
    e.preventDefault(); // Prevent the form from submitting normally

    // Serialize the form data into a URL-encoded string
    var formData = $(this).serialize();
console.log(formData);
    $.post("/insert", {
        form_data: formData,
    }, function(data){
        location.reload();
    });
});

$("#addColumnForm").submit(function(event){
    event.preventDefault();
    var newColumnName = $("#new_column_name").val();
    var newColumnType = $("#new_column_type").val();

    $.post("/newCol", {
        new_column_name: newColumnName,
        new_column_type: newColumnType
    }, function(){
        location.reload();
    });
});

$(document).ready(function(){
    $(".dropColumn").click(function(){
        var columnName = $(this).data('field');

        $.post("/dropCol", {
            column_name: columnName,
        }, function(){
            location.reload();
        });
    });
});

$(document).ready(function(){
    $(".dropRow").click(function(){
        var rowid = $(this).data('field');

        $.post("/dropRow", {
            rowid: rowid,
        }, function(){
            location.reload();
        });
    });
});
// not work
$(document).ready(function(){

    $(".selectval").change(function(){
        var value = $('.selectval').val();
        $.get("/filter/" + value, function(data){
            tablelimit = value;
        });
    });
});