$(function () {
    $('button#start').click(function () {
        $.ajax({
            url: 'bot.py',
            success: function (response) {
                $('div#results').append(response);
            }
        });
    });
});