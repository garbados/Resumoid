function onLinkedInLogin() {
    IN.API.Profile("me").result(function (profiles) {
        console.log(profiles);
        var profile = profiles.values[0];
        var profHTML = $('#profile');
        profHTML.children('#firstname').text(profile['firstName']);
        profHTML.children('#lastname').text(profile['lastName']);
        profHTML.children('#pic').attr('src', profile['pictureUrl']);
        profHTML.children('#pic').css('display', 'inline');
        $.ajax({
            url : "/login",
            data : profile,
            success : function(data) {
                console.log("Successfully logged in!");
            },
        });
    });
}

function onLinkedInLoad() {
    IN.Event.on(IN, "auth", function() { onLinkedInLogin(); });
    IN.Event.on(IN, "logout", function() { onLinkedInLogout(); });
}
