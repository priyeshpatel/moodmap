/*
 * themoodmap.co.uk JS
 * Copyright (c) Priyesh Patel
 */

var map;
var tweets = [];
var tweetsVisible = true;
var govFusion;
var tweetInfo;
var db_name = "tweets";
var db, view, changes;

/*
 * Use rating to determine colour of tweet icon.
 */
function getTweetIcon(rating) {
    var png = "img/";

    if (rating > 7) {
        png += "happy.png";
    } else if (rating < 5) {
        png += "sad.png";
    } else {
        png += "neutral.png";
    }

    return png;
}

/*
 * Plot a point given a tweet object.
 */
function plot(tweet, animate) {
    var png = getTweetIcon(tweet.rating);

    var tweetMarker = new google.maps.Marker({
        position: new google.maps.LatLng(tweet.latitude, tweet.longitude),
        map: ((tweetsVisible) ? map : null),
        title: tweet.username + ": " + tweet.tweet,
        animation: (animate ? google.maps.Animation.DROP : null),
        icon: new google.maps.MarkerImage(png)
    });

    google.maps.event.addListener(tweetMarker, 'click', function() { 
        tweetInfo.setContent(tweet.username + ": " + tweet.tweet);
        tweetInfo.open(map, tweetMarker);
    });

    tweets.push(tweetMarker);
}

/*
 * Plot a point from the _changes API.
 */
function plotIncoming(data) {
    for (var i = 0; i < data.results.length; i++) {
        var tweet = data.results[i].doc;
        plot(tweet, true);
        //console.log("Plotted (polling) => " + tweet.id);
    }
}

/*
 * Plot a point from the history.
 */
function plotStatic(data) {
    for (var i = data.rows.length - 1; i > 0; i--) {
        var tweet = data.rows[i].doc;
        plot(tweet, false);
        //console.log("Plotted (static) => " + tweet.id);
    }
    
    // Enable the interface.
    $('#loader').remove();
    $('#govData').removeAttr('disabled');
    $('#tweetData').removeAttr('disabled');

    db.changes(data.total_rows, {include_docs:true}).onChange(plotIncoming);
}

$(document).ready( function() {
    // Disable the interface
    $('#govData').attr('disabled', true);
    $('#govData').attr('checked', false);
    $('#tweetData').attr('disabled', true);
    $('#tweetData').attr('checked', true);

    var mapOptions = {
        zoom: 6,
        center: new google.maps.LatLng(54.085173,-1.933594),
        mapTypeId: google.maps.MapTypeId.ROADMAP
    };
    map = new google.maps.Map(document.getElementById("map"), mapOptions);

    tweetInfo = new google.maps.InfoWindow({maxWidth:300});
            
    // Government data
    govFusion = new google.maps.FusionTablesLayer({
        query: {
            select: 'geometry',
            from: '1246211'
        },
        map: null
    });

    db = $.couch.db(db_name);
    // Request data from the history.
    db.view('moodmap_tweets/tweets', {
        limit: 750,
        include_docs: true,
        descending: true,
        success: plotStatic
    });

    // Adjust map size.
    calculateMapHeight();

    // Display the controls briefly.
    $('#keyimg').slideToggle();
    setTimeout(function() {
        if( $('#keyimg').is(":visible"))
            $('#keyimg').slideToggle();
    }, 1500);

    $('#about').click(function() {
        $('#about-text').slideToggle();
    });

    $('#key').click(function() {
        $('#keyimg').slideToggle();
    });

    // Toggle government data.
    $('#govData').click(function() {
        if ($("#govData").prop("checked"))
            govFusion.setMap(map);
        else
            govFusion.setMap(null);
    });

    // Toggle tweets.
    $("#tweetData").click(function() {
        if ($("#tweetData").prop("checked")) {
            tweetsVisible = true;
            for(i in tweets) {
                tweets[i].setMap(map);
            }
        } else {
            tweetsVisible = false;
            for(i in tweets) {
                tweets[i].setMap(null);
            }
        }
    });
});

/*
 * Recalculate map size.
 */
function calculateMapHeight() {
    var headingHeight = $('#heading').outerHeight();
    $('#map').height($(window).height() - headingHeight -2);
}

$(window).resize(function() {
    calculateMapHeight();
}).load(function() {
    calculateMapHeight();
});
