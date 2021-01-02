  $(document).ready(function(){

    $('.sidenav').sidenav();
    $(".dropdown-trigger").dropdown({
        "coverTrigger": false
    });

    // select must come after dropdown, due to this bug in materialize:
    // https://github.com/Dogfalo/materialize/issues/6073
    $('select').formSelect();
    $('.modal').modal();
    $('.tooltipped').tooltip();

    $('.pushpin').pushpin({
        top: 128,
        offset: 0
    });

    // Add margin to content when filter is pinned
    $(document).on('scroll', function() {
        let isPinned = $('#filter-row').hasClass('pinned');
        if (isPinned) {
            $("#content-row").addClass('filter-margin-top');
        }
        else {
            $("#content-row").removeClass('filter-margin-top');
        }
    });

    validateMaterializeSelect();

    function validateMaterializeSelect() {
        let classValid = { "border-bottom": "1px solid #4caf50", "box-shadow": "0 1px 0 0 #4caf50" };
        let classInvalid = { "border-bottom": "1px solid #f44336", "box-shadow": "0 1px 0 0 #f44336" };
        if ($("select.validate").prop("required")) {
            $("select.validate").css({ "display": "block", "height": "0", "padding": "0", "width": "0", "position": "absolute" });
        }
        $(".select-wrapper input.select-dropdown").on("focusin", function () {
            $(this).parent(".select-wrapper").on("change", function () {
                if ($(this).children("ul").children("li.selected:not(.disabled)").on("click", function () { })) {
                    $(this).children("input").css(classValid);
                }
            });
        }).on("click", function () {
            if ($(this).parent(".select-wrapper").children("ul").children("li.selected:not(.disabled)").css("background-color") === "rgba(0, 0, 0, 0.03)") {
                $(this).parent(".select-wrapper").children("input").css(classValid);
            } else {
                $(".select-wrapper input.select-dropdown").on("focusout", function () {
                    if ($(this).parent(".select-wrapper").children("select").prop("required")) {
                        if ($(this).css("border-bottom") != "1px solid rgb(76, 175, 80)") {
                            $(this).parent(".select-wrapper").children("input").css(classInvalid);
                        }
                    }
                });
            }
        });
    }
  });