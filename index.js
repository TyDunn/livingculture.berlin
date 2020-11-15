// thanks for digging into my guts ... send me an email to say hi@tydunn.com :)

// This example creates a simple polygon representing the Bermuda Triangle.
function initMap() {
  const map = new google.maps.Map(document.getElementById("map"), {
    zoom: 12,
    center: { lat: 52.5200, lng: 13.4050 }, // 52.5200° N, 13.4050° E
    mapTypeId: "roadmap",
  });
  // Define the LatLng coordinates for the polygon's path.
  const triangleCoords = [
    { lat: 52.5111, lng: 13.4429 }, // 52.5111° N, 13.4429° E
    { lat: 52.5163, lng: 13.3777 }, // 52.5163° N, 13.3777° E
    { lat: 52.4754, lng: 13.4019 }, // 52.4754° N, 13.4019° E
    { lat: 52.5111, lng: 13.4429 }, // return
  ];
  // Construct the polygon.
  const bermudaTriangle = new google.maps.Polygon({
    paths: triangleCoords,
    strokeColor: "#1a0000",
    strokeOpacity: 0.8,
    strokeWeight: 2,
    fillColor: "#1a0000",
    fillOpacity: 0.5,
  });
  bermudaTriangle.setMap(map);
}
