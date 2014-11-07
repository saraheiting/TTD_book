/*global $ */

var initialize = function (navigator, user, token, urls) {
    /*  navigator.id.request() generates a signed assertion containing the 
    user's email address and passes that assertion to the onlogin callback 
    registered with navigator.id.watch(). */
    $('#id_login').on('click', function () {
        navigator.id.request();
    });

    navigator.id.watch({
        loggedInUser: user,
        onlogin: function (assertion) {
            $.post(
                urls.login,
                { assertion: assertion, csrfmiddlewaretoken: token }
            )
                .done(function () { window.location.reload(); })
                .fail(function () { navigator.id.logout(); });
        },
        onlogout: function () {}
    });
};

window.Superlists = {
    Accounts: {
        initialize: initialize
    }
};