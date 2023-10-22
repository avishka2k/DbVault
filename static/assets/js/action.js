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
    $(".column-name").click(function(){
        var value = $(this).text();
        $("#column_name").val(value);

        $("#editColName").modal('show');
    });
});

$(document).ready(function(){
    $(".insertRow").click(function(){
        $("#insertRowModal").modal('show');
    });
});

$(document).ready(function(){
    $(".insertCol").click(function(){
        $("#insertColModal").modal('show');
    });
});

$(document).ready(function(){
    $(".column-name").click(function(){
        $("#editColName").modal('show');
    });
});

function updateValue() {
    var cell_id = $("#edit_id").val();
    var field = $("#edit_field").val();
    var value = $("#edit_value").val();

    $.post("/edit_cell/" + cell_id, {
        field: field,
        value: value
    }, function(data){
        $("#editModal").modal('hide');
        location.reload();
    });
}

function updateColName() {
    var col_name = $("#column_name").val();

    $.post("/updateColName", {
        value: col_name
    }, function(data){
        $("#editColName").modal('hide');
        location.reload();
    });
}

$("#addNewTable").submit(function(event){
    event.preventDefault();
    var table_name = $("#new_table_name").val();
    var initial_column = $("#initial_column").val();
    var relationship = $("#relationship").val();

    $.post("/new_table", {
        table_name: table_name,
        initial_column: initial_column,
        relationship: relationship,
    }, function(){
        location.reload();
    });
});

$('#insertRowForm').submit(function(e) {
    e.preventDefault();
    var formData = $(this).serialize();
    console.log(formData);
    $.post("/insert_row", {
        form_data: formData,
    }, function(){
        location.reload();
    });
});

$("#insertColForm").submit(function(event){
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
    $(".dropColumn-confirm").click(function(){
        var columnName = $(this).data('field');
        Swal.fire({
            title: 'Are you sure?',
            text: "You won't be able to revert this!",
            icon: 'warning',
            showCancelButton: true,
            confirmButtonColor: '#3085d6',
            cancelButtonColor: '#d33',
            confirmButtonText: 'Yes, delete it!'
        }).then((result) => {
            if (result.isConfirmed) {
                Swal.fire(
                    'Deleted!',
                    'Your record has been deleted.',
                    'success'
                )
                $.post("/dropCol", {
                    column_name: columnName,
                }, function(){
                    location.reload();
                });
            }
        })
    });
});

$(document).ready(function(){
    $(".dropRow").click(function(){
        var rowid = $(this).data('field');

        Swal.fire({
            title: 'Are you sure?',
            text: "You won't be able to revert this!",
            icon: 'warning',
            showCancelButton: true,
            confirmButtonColor: '#3085d6',
            cancelButtonColor: '#d33',
            confirmButtonText: 'Yes, delete it!'
        }).then((result) => {
            if (result.isConfirmed) {
                Swal.fire(
                    'Deleted!',
                    'Your record has been deleted.',
                    'success'
                )
                $.post("/dropRow", {
                    rowid: rowid,
                }, function(){
                    location.reload();
                });
            }
        })
    });
});

$(document).ready(function(){
    $(".dropTable-confirm").click(function(){
        var tableName = $(this).data('drop_table');
        Swal.fire({
            title: 'Are you sure?',
            text: "You won't be able to revert this!",
            icon: 'warning',
            showCancelButton: true,
            confirmButtonColor: '#3085d6',
            cancelButtonColor: '#d33',
            confirmButtonText: 'Yes, delete it!'
        }).then((result) => {
            if (result.isConfirmed) {
                Swal.fire(
                    'Deleted!',
                    'Your Table has been deleted.',
                    'success'
                )
                $.post("/drop_table", {
                    table_name: tableName,
                }, function(data){
                    location.reload();
                });
            }
        })
    });
});


$(document).ready(function(){
    $(".deleteAllRecent").click(function(){
        Swal.fire({
            title: 'Are you sure?',
            text: "You won't be able to revert this!",
            icon: 'warning',
            showCancelButton: true,
            confirmButtonColor: '#3085d6',
            cancelButtonColor: '#d33',
            confirmButtonText: 'Yes, delete it!'
        }).then((result) => {
            if (result.isConfirmed) {
                Swal.fire(
                    'Deleted!',
                    'Your all recent has been deleted.',
                    'success'
                )
                $.post("/deleteAllRecent", function(){
                    location.reload();
                });
            }
        })
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