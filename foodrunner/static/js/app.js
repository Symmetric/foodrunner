/**
 * Created by paul on 3/31/14.
 */
var geocoder;
var map;

function initialize() {
    "use strict";
    var markers = [];
    var mapOptions = {
        center: new google.maps.LatLng(-34.397, 150.644),
        zoom: 8
    };
    map = new google.maps.Map(document.getElementById("map-canvas"),
        mapOptions);

    var defaultBounds = new google.maps.LatLngBounds(
        new google.maps.LatLng(-33.8902, 151.1759),
        new google.maps.LatLng(-33.8474, 151.2631));
    map.fitBounds(defaultBounds);

    geocoder = new google.maps.Geocoder();
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