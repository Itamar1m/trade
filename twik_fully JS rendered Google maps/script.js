function mapDiv() {
    var mapDiv = document.createElement('div')
    mapDiv.setAttribute('id', 'map')
    mapDiv.setAttribute('class', 'hide-map')
    document.body.appendChild(mapDiv)
    return mapDiv
}
mapDiv = mapDiv()

function coordsDiv() {
    var coordsDiv = document.createElement('div')
    coordsDiv.setAttribute('id', 'latLng-fields-div')
    document.body.appendChild(coordsDiv)
    return coordsDiv
}
coordsDiv = coordsDiv()

function latlngDivs() {
    var latDiv = document.createElement('div')
    var lngDiv = document.createElement('div')
    latDiv.setAttribute('class', 'lat-div')
    lngDiv.setAttribute('class', 'long-div')

    var latField = document.createElement('INPUT')
    latField.setAttribute("type", "text");
    latField.setAttribute('value', 32.7003)
    latField.setAttribute('id', 'lat')

    var lngField = document.createElement('INPUT')
    lngField.setAttribute("type", 'text')
    lngField.setAttribute('value', 36.6825)
    lngField.setAttribute('id', 'long')

    coordsDiv.appendChild(latDiv)
    coordsDiv.appendChild(lngDiv)

    var latLabel = document.createElement('LABEL')
    latLabel.setAttribute('for', 'lat')
    latLabel.innerText = 'Latitude:'

    var lngLabel = document.createElement('LABEL')
    lngLabel.setAttribute('for', 'long')
    lngLabel.innerText = 'Longitude:'
  
    latDiv.appendChild(latLabel)
    lngDiv.appendChild(lngLabel)
    latDiv.appendChild(latField)
    lngDiv.appendChild(lngField)
}
latlngDivs()


function buttonDiv() {
    var buttonDiv = document.createElement('div')
    buttonDiv.setAttribute('class', 'buttons-div')
    coordsDiv.appendChild(buttonDiv)
    return buttonDiv
}
buttonDiv = buttonDiv()


function Buttons() {
    var markButton = document.createElement('button')
    markButton.innerText = 'Mark '
    buttonDiv.appendChild(markButton)
    var markedButton = document.createElement('button')
    markedButton.innerText = 'Hide Markers'
    buttonDiv.appendChild(markedButton)
    var deleteButton = document.createElement('button')
    deleteButton.innerText = 'Delete Markers'
    buttonDiv.appendChild(deleteButton)
    return {
        'markedButton': markedButton,
        'markButton': markButton,
        'deleteButton': deleteButton
    }
}
buttons = Buttons()


function initMap() {
    const map = new google.maps.Map(mapDiv, {
        center: {
            lat: 32.0853,
            lng: 34.7609
        },
        zoom: 7,

    });
    // custom marker
    const myMarker = {
        path: "M10.453 14.016l6.563-6.609-1.406-1.406-5.156 5.203-2.063-2.109-1.406 1.406zM12 2.016q2.906 0 4.945 2.039t2.039 4.945q0 1.453-0.727 3.328t-1.758 3.516-2.039 3.070-1.711 2.273l-0.75 0.797q-0.281-0.328-0.75-0.867t-1.688-2.156-2.133-3.141-1.664-3.445-0.75-3.375q0-2.906 2.039-4.945t4.945-2.039z",
        fillColor: "green",
        fillOpacity: 0.4,
        strokeWeight: 0,
        rotation: 0,
        scale: 2.5,
        anchor: new google.maps.Point(15, 30),
    };

    function newMarker(latlng) {
        var newMarker = new google.maps.Marker({
            position: latlng,
            map,
        })
        return newMarker
    }

    const fixedMarker = newMarker({
        lat: 32.0853,
        lng: 34.7818
    })
    fixedMarker.setIcon("https://developers.google.com/maps/documentation/javascript/examples/full/images/beachflag.png")

    var dragMarker = newMarker({
        lat: 32.7003,
        lng: 36.6825
    })

    const infoWindow = new google.maps.InfoWindow({
        content: 'Drag me around to see the coordinates of where I am placed ,and mark the coordinates you want below!',
    })
    infoWindow.open(map, dragMarker)

    dragMarker.addListener('dragstart', function () {
        infoWindow.close()
        dragMarker.setAnimation(google.maps.Animation.BOUNCE)
    })

    // obtaining longitude and latitude from dragMarker
    let latText = document.getElementById('lat')
    let lngText = document.getElementById('long')

    function draggableMarkerAttrs(marker) {
        marker.setDraggable(true)
        google.maps.event.addListener(marker, 'dragend', function (evt) {
            latText.value = (evt.latLng.lat().toFixed(4));
            lngText.value = (evt.latLng.lng().toFixed(4));
            map.panTo(evt.latLng);
            marker.setAnimation(null)
        })
    };
    draggableMarkerAttrs(dragMarker)

    // storing ,viewing and creating markers
    function newDraggableMarker(dragmarker) {
        dragMarker.setMap(null)
        dragMarker = newMarker(latlng)
        // draggable marker function defined above line 54
        draggableMarkerAttrs(dragMarker)
    }

    let hidden;
    var markedPoints = ''
    var storedMarkers = []
    mark = buttons.markButton
    mark.addEventListener('click', addMarker)

    function addMarker() {
        latlng = {
            lat: parseFloat(latText.value),
            lng: parseFloat(lngText.value)
        }
        markedPoints = latlng
        // new marker function defined above line 11
        var marker = newMarker(latlng)
        marker.setAnimation(google.maps.Animation.DROP)
        marker.setIcon(myMarker)
        if (hidden == true) {
            marker.setMap(null)
        } else {
            marker.setMap(map)
        }
        storedMarkers.push(marker)
        newDraggableMarker(dragMarker)
        console.log(storedMarkers)
    }



    function displayMarkedPoints() {
        latlng = {
            lat: parseFloat(latText.value),
            lng: parseFloat(lngText.value)
        }
        markedButton.innerText = 'Display Markers'
        for (let i = 0; i < storedMarkers.length; i++) {
            setTimeout(function () {
                storedMarkers[i].setMap(null);
            }, i * 90);
            hidden = true
        }
    }


    function hideMarkedPoints() {
        latlng = {
            lat: parseFloat(latText.value),
            lng: parseFloat(lngText.value)
        }
        markedButton.innerText = 'Hide markers'
        for (let i = 0; i < storedMarkers.length; i++) {
            setTimeout(function () {
                storedMarkers[i].setMap(map);
                setTimeout(function () {newDraggableMarker(dragMarker)},20)
            }, i * 110);
        }
        
        hidden = false
    }


    markedButton = buttons.markedButton
    markedButton.addEventListener('click', myMarkedPoints)
    // showing and hiding marked points
    function myMarkedPoints() {
        if (hidden != true && storedMarkers.length > 0) {
            displayMarkedPoints()
        } else {
            hideMarkedPoints()
        }
        newDraggableMarker(dragMarker)
    }


    function okButton(confirmDiv) {
        var okButton = document.createElement('button')
        okButton.classList.add('ok-button')
        okButton.innerText = 'OK'
        confirmDiv.appendChild(okButton)
        return okButton
    }

    deleteButton = buttons.deleteButton
    deleteButton.addEventListener('click', deleteMarkers)

    function deleteMarkers() {
        var confirmDiv = document.createElement('div')
        confirmDiv.classList.add('confirm-div')
        document.body.appendChild(confirmDiv)

        function removeConfirm() {
            document.body.removeChild(confirmDiv)
        }
        let num = storedMarkers.length
        if (num > 1) {
            confirmDiv.innerText = 'Are you sure you want to delete all ' + num + ' of your markers ?'
        } else if (num == 1) {
            confirmDiv.innerText = 'Are you sure you want to delete your marker ?'
        } else {
            confirmDiv.innerText = 'You currently have no markers.'
        }
        if (num < 1) {
            okButton = okButton(confirmDiv)
            okButton.addEventListener('click', removeConfirm)

        } else {
            var yesButton = document.createElement('button')
            yesButton.classList.add('yes-button')
            var noButton = document.createElement('button')
            noButton.classList.add('no-button')
            noButton.innerText = 'No'
            yesButton.innerText = 'Yes'
            confirmDiv.appendChild(yesButton)
            confirmDiv.appendChild(noButton)
            noButton.addEventListener('click', removeConfirm)
            yesButton.addEventListener('click', function () {
                for (var i = 0; i < storedMarkers.length; i++) {
                    console.log(storedMarkers.length)
                    storedMarkers[i].setMap(null)
                }
                    markedPoints = []
                    storedMarkers = []
                    removeConfirm()

            })
        }

    }
}

function showMapButton() {
    var mapButton = document.createElement('button')
    mapButton.setAttribute('id', 'map-button')
    mapButton.innerText = 'Show Map'
    document.querySelector('header').appendChild(mapButton)
    return mapButton
}

mapButton = showMapButton()

function showMap() {
    var latLngFields = document.getElementById('latLng-fields-div')

    mapButton.addEventListener("click", function () {

        map.classList.toggle('hide-map');
        if (map.classList.contains('hide-map')) {
            map.style.display = 'none';
            latLngFields.style.display = 'none';
            console.log(latLngFields);
            mapButton.innerText = 'Show Map';
        } else {
            map.style.display = 'block';
            latLngFields.style.display = 'flex';
            mapButton.innerText = 'Hide Map';
        }
    })
}
showMap()

