var map;
var Start_Marker;
var Goal_Marker;
var Current_Marker;

function initMap() {

  map = new google.maps.Map(document.getElementById("map"), {
    center: { lat: 40.472059, lng: -79.964419},
    zoom: 18,
    mapTypeId: 'satellite'
  });

  map.setTilt(0);

  Start_Marker = new google.maps.Marker({
    position: {
      lat: 40.472147,
      lng: -79.965038
    },
    map: map,
    title: 'Start',
    icon: {
      url: "http://maps.google.com/mapfiles/ms/icons/green-dot.png"
    }
  });

  Current_Marker = new google.maps.Marker({
	position: {
	  lat: 40.472147,
	  lng: -79.965038
	},
	map: map,
	title: 'Current'
  });

  Goal_Marker = new google.maps.Marker({
    position: {
      lat: 40.475365,
      lng: -79.964020
    },
    map: map,
    title: 'Goal',
    icon: {
      url: "http://maps.google.com/mapfiles/ms/icons/blue-dot.png"
    }
  });

  start_gps()

}

function start_gps(){

	var socket = null;
	var websocket_server_url = "https://example.com"

	var server_url = websocket_server_url +"?username=carmap"
	socket = io(server_url, {'forceNew':true })

	socket.on('connect', function(){
		console.log('Connected to Car Control GPS Server!')
	})

	socket.on('disconnect', function(){
		console.log('Disconnected from Car Control GPS Server!')
	})

	socket.on('reconnecting', function(attemptNumber){
		console.log('Reconnecting to Car Control GPS - Attempt: ' +attemptNumber)
	});

	socket.on('rpi_car_gps', function(msg){

		console.log("rpi_car_gps: " +JSON.stringify(msg))

		Current_Marker.setMap(null)

		var pos = {
			lat: parseFloat(msg.latitude),
		    lng: parseFloat(msg.longitude)
		};

	  	Current_Marker = new google.maps.Marker({
	  		position: pos,
	  		map: map,
	  		title: 'Current'
	    });

		map.setCenter(pos);

	});
}
