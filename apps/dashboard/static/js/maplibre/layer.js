export function addParcelSources(map, url) {
  map.addSource("parcels", {
    type: "geojson",
    data: url,
  });
}

export function addParcelLayer(map, lineWidth=3) {
  map.addLayer({
    id: "parcels-fill-layer",
    type: "fill",
    source: "parcels",
    paint: {
      "fill-color": "#000000",
      "fill-opacity": 0.0,
    },
  });

  map.addLayer({
    id: "parcels-layer",
    type: "line",
    source: "parcels",
    paint: { "line-color": "#ffa318", "line-width": lineWidth },
  });
}
