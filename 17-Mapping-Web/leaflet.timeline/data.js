// Store our API endpoint inside queryUrl
var queryUrl = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson";
d3.json(queryUrl, function(data){
    createFeatures(data.features);
});

function createFeatures(earthquakeData) {

    // Define a function we want to run once for each feature in the features array
    // Give each feature a popup describing the place and time of the earthquake
    function onEachFeature(feature, layer) {
      layer.bindPopup("<h3>" + feature.properties.place +
        "</h3><hr><p>" + new Date(feature.properties.time) + "</p>" + 
        "<p>Magnitude: " + feature.properties.mag + "</p>"
        );
    }
  
    // Create a GeoJSON layer containing the features array on the earthquakeData object
    // Run the onEachFeature function once for each piece of data in the array
    var earthquakes = L.geoJSON(earthquakeData, {
      onEachFeature: onEachFeature
    });
    // Define streetmap and darkmap layers
    var streetmap = L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/outdoors-v10/tiles/256/{z}/{x}/{y}?" +
      "access_token=pk.eyJ1Ijoia2pnMzEwIiwiYSI6ImNpdGRjbWhxdjAwNG0yb3A5b21jOXluZTUifQ." +
      "T6YbdDixkOBWH_k9GbS8JQ");
  
    // Define a baseMaps object to hold our base layers
    var baseMaps = {
      "Street Map": streetmap
    };
  
    // Create overlay object to hold our overlay layer
    var overlayMaps = {
      Earthquakes: earthquakes
    };
  
    // Create our map, giving it the streetmap and earthquakes layers to display on load
    var myMap = L.map("map", {
      center: [
        37.09, -95.71
      ],
      zoom: 5,
      layers: [streetmap, earthquakes]
    });
    // Create a layer control
    // Pass in our baseMaps and overlayMaps
    // Add the layer control to the map
    L.control.layers(baseMaps, overlayMaps, {
      collapsed: false
    }).addTo(myMap);
  }
  