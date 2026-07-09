export function addParcelSources(map, url) {
  map.addSource("parcels", {
    type: "geojson",
    data: url,
  });
}

export function addParcelLayer(map, source="parcels", color="#ffa318", lineWidth = 3) {
  map.addLayer({
    id: "parcels-fill-layer",
    type: "fill",
    source: source,
    paint: {
      "fill-color": "#000000",
      "fill-opacity": 0.0,
    },
  });

  map.addLayer({
    id: "parcels-layer",
    type: "line",
    source: source,
    paint: {
      "line-color": [
        "case",
        ["boolean", ["feature-state", "selected"], false],
        "#2563eb",
        color,
      ],
      "line-width": [
        "case",
        ["boolean", ["feature-state", "selected"], false],
        lineWidth + 1,
        lineWidth,
      ],
    },
  });
}
