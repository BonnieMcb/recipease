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

        let filter = '';

        let values = $('#allergen_name').val();
        // strip spaces and make string lowercase
        for (let i in values) {
            // code adapted from:
            // https://stackoverflow.com/a/43208537/14135937
            filter += values[i].toLowerCase().replace(/\s/g, '') + '-';
        }
        // remove trailing dash
        filter = filter.slice(0, -1);
        
        applyFilter(filter);
    });

    $('#clear-filters').on("click", function() {

        applyFilter("");
    });
})
