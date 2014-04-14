/**
 * Created by paul on 3/31/14.
 */
var geocoder;
var map;
var start_marker;
var end_marker;
var dummy_data;
var dummy_index;

function initialize() {
    "use strict";

    var mapOptions = {
        center: new google.maps.LatLng(37.7749295, -122.41941550000001),
        zoom: 13,
        mapTypeControl: false
    };
    map = new google.maps.Map(document.getElementById("map-canvas"),
        mapOptions);

    dummy_data = [
        [
            new google.maps.LatLng(37.7749295, -122.41941550000001),
            new google.maps.LatLng(37.754762, -122.42726049999999)
        ],
        [
            new google.maps.LatLng(37.7767709, -122.44457),
            new google.maps.LatLng(37.7749295, -122.41941550000001)
        ]
    ];
    dummy_index = 0;
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

function nextPickup() {
    "use strict";
    if (dummy_index < dummy_data.length) {
        // Clear any old markers
        if (typeof start_marker != 'undefined') {
            start_marker.setMap(null);
        }
        if (typeof end_marker != 'undefined') {
            end_marker.setMap(null);
        }

        var route = dummy_data[dummy_index];
        console.log('Getting next dummy data ' + route);

        start_marker = new google.maps.Marker({
            map: map,
            position: route[0]
        });
        console.log('Added new pickup location at ' + route[0]);
        end_marker = new google.maps.Marker({
            map: map,
            position: route[1]
        });
        console.log('Added new delivery destination at ' + route[1]);
        dummy_index++;
    }
    else {
        console.log('No more routes.');
        start_marker.setMap(null);
        end_marker.setMap(null);
    }
}

$("#pickup-button").click(nextPickup);