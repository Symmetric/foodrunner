/**
 * Created by paul on 3/31/14.
 */
var geocoder;
var map;
var start_marker;
var end_marker;
var pickups;

function initialize() {
    "use strict";
    var mapOptions = {
        center: new google.maps.LatLng(37.7749295, -122.41941550000001),
        zoom: 13,
        mapTypeControl: false
    };
    map = new google.maps.Map(document.getElementById("map-canvas"),
        mapOptions);

    $.ajax({
        url: '/api/donations',
        success: function(data, textStatus, xhr) {
            console.log('Got pickup-list: ');
            console.dir(data);
            pickups = data;
            drawPickups();
        },
        error: function(xhr, textStatus) {
            console.log('Failed to load pickup list. Error:' + textStatus);
        }
    });

}

google.maps.event.addDomListener(window, 'load', initialize);

function locationSearch() {
    "use strict";
    var search = $("#map-search").val().trim();
    // Don't do a search if the input was empty.
    if (search) {
        console.log("Searching for " + search);
        // Send a geocode request and provide a callback.
        geocoder.geocode({address: search}, function(results, status) {
            if (status === google.maps.GeocoderStatus.OK) {
                // Got results so recenter on the first one, and
                // set the zoom level appropriately for this location.
//                var ne = results[0].geometry.viewport.getNorthEast();
//                var sw = results[0].geometry.viewport.getSouthWest();
                map.fitBounds(results[0].geometry.viewport);

            }
        });
    }
    // Prevent the form submit from happening.
    event.preventDefault();
}

$("#map-search-form").submit(locationSearch);

function drawPickups() {
    "use strict";
    for (var i=0; i < pickups.length; i++) {
        var pickup = pickups[i];
        console.log('Drawing pickup');
        console.dir(pickup);
        var location = new google.maps.LatLng(pickup.location_lat, pickup.location_lng);

        start_marker = new google.maps.Marker({
            map: map,
            position: location
        });
        console.log('Added new pickup location at ' + location);
    }
}

$("#pickup-button").click(drawPickups);