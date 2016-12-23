$('#img-trigger').click(function () {
    $('#info-div').addClass('in');
});

$('#go-back').click(function () {
    $('#info-div').removeClass('in');
});

/** Tags Search Bar **/
$.expr[":"].contains = $.expr.createPseudo(function (arg) {
    return function (elem) {
        return $(elem).text().toUpperCase().indexOf(arg.toUpperCase()) >= 0;
    };
});
$(document).ready(function () {
    $('#addTagBtn').click(function () {
        $('#tags option:selected').each(function () {
            $(this).appendTo($('#selectedTags'));
        });
    });
    $('#removeTagBtn').click(function () {
        $('#selectedTags option:selected').each(function (el) {
            $(this).appendTo($('#tags'));
        });
    });
    $('.tagRemove').click(function (event) {
        event.preventDefault();
        $(this).parent().remove();
    });
    $('ul.tags').click(function () {
        $('#search-field').focus();
    });
    $('#search-field').keypress(function (event) {
        if (event.which == '10' || event.which == '13') {
            if (($(this).val() != '') && ($(".tags .addedTag:contains('" + $(this).val() + "') ").length == 0)) {

                $('<li class="addedTag">' + $(this).val() + ' <a class="tagRemove" onclick="$(this).parent().remove();">[X]</a><input type="hidden" value="' + $(this).val() + '" name="tags"></li>').insertBefore('.tags .tagAdd');
                $(this).val('');

            } else {
                $(this).val('');

            }
            return (event.keyCode!=13);
        }
    });

});

/** Tags Search Bar **/
$.expr[":"].contains = $.expr.createPseudo(function (arg) {
    return function (elem) {
        return $(elem).text().toUpperCase().indexOf(arg.toUpperCase()) >= 0;
    };
});
$(document).ready(function () {
    $('#addTagBtn2').click(function () {
        $('#tags2 option:selected').each(function () {
            $(this).appendTo($('#selectedTags2'));
        });
    });
    $('#removeTagBtn2').click(function () {
        $('#selectedTags2 option:selected').each(function (el) {
            $(this).appendTo($('#tags2'));
        });
    });
    $('.tagRemove2').click(function (event) {
        event.preventDefault();
        $(this).parent().remove();
    });
    $('ul.tags2').click(function () {
        $('#search-field2').focus();
    });
    $('#search-field2').keypress(function (event) {
        if (event.which == '13') {
            if (($(this).val() != '') && ($(".tags2 .addedTag2:contains('" + $(this).val() + "') ").length == 0)) {

                $('<li class="addedTag2">' + $(this).val() + '<span class="tagRemove2" onclick="$(this).parent().remove();">x</span><input type="hidden" value="' + $(this).val() + '" name="tags[]"></li>').insertBefore('.tags2 .tagAdd2');
                $(this).val('');

            } else {
                $(this).val('');

            }
        }
    });

});


/** Rate Tags **/
var count_like1 = 105;
var count_dislike1 = 105;
$("body").on("click", "#like1", function () {
    $("#count_like1").html("<div>" + (++count_like1) + "</div>");
});
$("body").on("click", "#dislike1", function () {
    $("#count_like1").html("<div>" + (--count_like1) + "</div>");
});

var count_like2 = 32;
var count_dislike2 = 32;
$("body").on("click", "#like2", function () {
    $("#count_like2").html("<div>" + (++count_like2) + "</div>");
});
$("body").on("click", "#dislike2", function () {
    $("#count_like2").html("<div>" + (--count_like2) + "</div>");
});

var count_like3 = 54;
var count_dislike3 = 54;
$("body").on("click", "#like3", function () {
    $("#count_like3").html("<div>" + (++count_like3) + "</div>");
});
$("body").on("click", "#dislike3", function () {
    $("#count_like3").html("<div>" + (--count_like3) + "</div>");
});

var count_like4 = 10;
var count_dislike4 = 10;
$("body").on("click", "#like4", function () {
    $("#count_like4").html("<div>" + (++count_like4) + "</div>");
});
$("body").on("click", "#dislike4", function () {
    $("#count_like4").html("<div>" + (--count_like4) + "</div>");
});

/** Rate Preferences **/
var count_likea = 15;
var count_dislikea = 15;
$("body").on("click", "#likea", function () {
    $("#count_likea").html("<div>" + (++count_likea) + "</div>");
});
$("body").on("click", "#dislikea", function () {
    $("#count_likea").html("<div>" + (--count_likea) + "</div>");
});

var count_likeb = 15;
var count_dislikeb = 15;
$("body").on("click", "#likeb", function () {
    $("#count_likeb").html("<div>" + (++count_likeb) + "</div>");
});
$("body").on("click", "#dislikeb", function () {
    $("#count_likeb").html("<div>" + (--count_likeb) + "</div>");
});

var count_likec = 15;
var count_dislikec = 15;
$("body").on("click", "#likec", function () {
    $("#count_likec").html("<div>" + (++count_likec) + "</div>");
});
$("body").on("click", "#dislikec", function () {
    $("#count_likec").html("<div>" + (--count_likec) + "</div>");
});

var count_liked = 15;
var count_disliked = 15;
$("body").on("click", "#liked", function () {
    $("#count_liked").html("<div>" + (++count_liked) + "</div>");
});
$("body").on("click", "#disliked", function () {
    $("#count_liked").html("<div>" + (--count_liked) + "</div>");
});

var count_likee = 15;
var count_dislikee = 15;
$("body").on("click", "#likee", function () {
    $("#count_likee").html("<div>" + (++count_likee) + "</div>");
});
$("body").on("click", "#dislikee", function () {
    $("#count_likee").html("<div>" + (--count_likee) + "</div>");
});

var count_likef = 15;
var count_dislikef = 15;
$("body").on("click", "#likef", function () {
    $("#count_likef").html("<div>" + (++count_likef) + "</div>");
});
$("body").on("click", "#dislikef", function () {
    $("#count_likef").html("<div>" + (--count_likef) + "</div>");
});

