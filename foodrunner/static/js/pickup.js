/**
 * Created by paul on 3/31/14.
 */
var geocoder;
var map;
var pickups;
var destination;

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
        success: function(data) {
            console.log('Got pickup-list: ');
            console.dir(data);
            pickups = data;
            maybeDrawPickups();
        },
        error: function(xhr, textStatus) {
            console.log('Failed to load pickup list. Error:' + textStatus);
        }
    });

    $.ajax({
        url: '/api/recipients',
        success: function(data) {
            console.log('Got recipient list: ');
            console.dir(data);
            if (data.length > 0) {
                destination = data[0];
                maybeDrawPickups();
            }

        },
        error: function(xhr, textStatus) {
            console.log('Failed to load destination. Error:' + textStatus);
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
                map.fitBounds(results[0].geometry.viewport);

            }
        });
    }
    // Prevent the form submit from happening.
    event.preventDefault();
}

$("#map-search-form").submit(locationSearch);

// Draw the pickups, if we have got pickups and a destination.
function maybeDrawPickups() {
    "use strict";
    var pickupsIsDefined = typeof pickups != 'undefined';
    var destinationIsDefined = typeof destination != 'undefined';
    if (pickupsIsDefined && destinationIsDefined) {
        for (var i=0; i < pickups.length; i++) {
            var pickup = pickups[i];
            console.log('Drawing pickup');
            console.dir(pickup);

            var position = new google.maps.LatLng(pickup.location_lat, pickup.location_lng);
            var marker = new google.maps.Marker({
                map: map,
                position: position
            });

            console.log('Added new pickup location at ' + position);
            attachPickupInfo(marker, pickup)
        }
        new google.maps.Marker({
            map: map,
            position: new google.maps.LatLng(destination.location_lat, destination.location_lng),
            icon: 'http://mt.googleapis.com/vt/icon/name=icons/spotlight/spotlight-waypoint-a.png',
            text: 'Z'
        });
        console.log('Added destination location');
    }
    else {
        console.log('Pickups is defined? ' + pickupsIsDefined);
        console.log('Destination is defined? ' + destinationIsDefined);
    }
}

function attachPickupInfo(marker, pickup) {
    "use strict";
    console.log('Click. Displaying info on pickup.');
    console.dir(pickup);

    var content = 'Description: ' + pickup.description + '<br/>' +
        'Weight: ' + pickup.weight + '<br/>' +
        'Available: ' + pickup.available_time + '<br/>' +
        'Expires: ' + pickup.expire_time + '<br/>';

    var marker_info = new google.maps.InfoWindow({
        content: content
    });
    google.maps.event.addListener(marker, 'click', function() {
        marker_info.open(map, marker);
    });
}

$("#pickup-button").click(maybeDrawPickups);