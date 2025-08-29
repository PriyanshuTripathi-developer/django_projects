document.addEventListener("DOMContentLoaded", function () {
    const latInput = document.getElementById("id_latitude");
    const lngInput = document.getElementById("id_longitude");

    // Create map div
    let mapDiv = document.createElement("div");
    mapDiv.id = "map";
    mapDiv.style.height = "400px";
    mapDiv.style.marginTop = "10px";
    latInput.parentNode.appendChild(mapDiv);

    // Default location (India)
    let center = { lat: 22.9734, lng: 78.6569 };

    if (latInput.value && lngInput.value) {
        center = { lat: parseFloat(latInput.value), lng: parseFloat(lngInput.value) };
    }

    let map = new google.maps.Map(mapDiv, {
        center: center,
        zoom: 5,
    });

    let marker = new google.maps.Marker({
        position: center,
        map: map,
        draggable: true,
    });

    // Update fields when marker moves
    google.maps.event.addListener(marker, "dragend", function (event) {
        latInput.value = event.latLng.lat().toFixed(6);
        lngInput.value = event.latLng.lng().toFixed(6);
    });

    // Update marker when clicking map
    google.maps.event.addListener(map, "click", function (event) {
        marker.setPosition(event.latLng);
        latInput.value = event.latLng.lat().toFixed(6);
        lngInput.value = event.latLng.lng().toFixed(6);
    });
});
