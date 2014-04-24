/**
 * Created by paul on 3/31/14.
 */
var geocoder;
var map;
var marker;

function initialize() {
    "use strict";
    var mapOptions = {
        center: new google.maps.LatLng(37.7749295, -122.41941550000001),
        zoom: 13,
        mapTypeControl: false
    };
    map = new google.maps.Map(document.getElementById("map-canvas"),
        mapOptions);

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
                map.fitBounds(results[0].geometry.viewport);

                // Clear the old marker, if present
                if (typeof marker != 'undefined') {
                    console.log('Removing old marker')
                    marker.setMap(null);
                }

                // Create a marker for the search location.
                marker = new google.maps.Marker({
                    map: map,
                    position: results[0].geometry.location
                });
                console.log('Added new marker at ' + results[0].geometry.location);
                var lat = results[0].geometry.location.lat().toString()
                var lng = results[0].geometry.location.lng().toString()
                $("#id_location_lat").val(lat);
                $("#id_location_lng").val(lng);
                $("#donation-menu").show();
            }
        });
    }
    // Prevent the form submit from happening.
    event.preventDefault();
}

$("#map-search-form").submit(locationSearch);