$(document).ready(function(){ 

    function applyFilter(filter) {

        // change URL Query Parameters
        // code adapted from:
        // https://usefulangle.com/post/81/javascript-change-url-parameters
        var url = new URL(window.location.href);
        url.searchParams.set('filter', filter);

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

        url.searchParams.delete('filter');
    });
})
