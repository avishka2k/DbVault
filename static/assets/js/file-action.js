$(document).ready(function(){

    $('.card_click').on('click', function(){
        $(".selected-file-details").removeClass("d-none");
        var tablename = $(this).data('tablename');
        var tablesize = $(this).data('tablesize');

        $(".file-details-title").text(tablename);
        $(".file-details-size").text(tablesize);
    });

    $('.card_click').on('dblclick', function(){
        window.location.replace("/file/table");
    });


    $('.btn_delete').on('click', function(){
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
                    'Your file has been deleted.',
                    'success'
                )
                element.parentElement.parentElement.remove()
                i = document.querySelectorAll(".btn-delete").length
                if (i < 1) {
                    document.getElementById("cart-container-delete").remove()
                    document.getElementById("cart-empty-cart").classList.remove("d-none")
                }
            }
        })
    });

    $('.files-type').click(function() {
        $('.files-type').removeClass('active');
        $(this).addClass('active');
        var index = $(this).index();
        sessionStorage.setItem('activeTabIndex', index);
      });
      var activeTabIndex = sessionStorage.getItem('activeTabIndex');

      if (activeTabIndex !== null) {
        $('.files-type').eq(activeTabIndex).addClass('active');
      }

    $('.table-row-active').click(function() {
        $('.table-row-active').removeClass('table-active');
        $(this).addClass('table-active');
    });
});

