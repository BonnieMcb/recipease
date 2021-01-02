$(document).ready(function(){ 

    function applyFilter(filter) {

        // change URL Query Parameters
        // code adapted from:
        // https://usefulangle.com/post/81/javascript-change-url-parameters
        var url = new URL(window.location.href);
        if (filter)
            url.searchParams.set('filter', filter);
        else
            url.searchParams.delete('filter');

        window.location.assign(url);
    }

    $('#apply-filters').on("click", function() {

        let active = [];
        // With help from:
        // https://stackoverflow.com/a/2950163/14135937
        $('#allergen_name > option:selected').each(function() {
            active.push($(this).val());
        });

        let filter = active.join('-');
        
        applyFilter(filter);
    });

    $('#clear-filters').on("click", function() {

        applyFilter(null);
    });

    $('#safe-search').on("click", function(e) {
        
        let isChecked = $(this).prop('checked');
        // keep hidden form input in sync with switch
        $('#safe-search-enabled').prop('checked', isChecked);

        if (!isChecked) {

            e.preventDefault();
            $('.modal').modal('open');
        }
        else {

            $('#safe-search-form').submit();
        }
    });
});
