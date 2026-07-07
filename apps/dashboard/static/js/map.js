const BASE_URL =
  window.location.hostname === "127.0.0.1" ||
  window.location.hostname === "localhost"
    ? "http://127.0.0.1:8000"
    : "https://topmapsolutions.com";

const parcelUrl = `${BASE_URL}/parcels/show-parcels/`;

const map = new maplibregl.Map({
  container: "map",
  zoom: 12,
  center: [11.39085, 47.27574],
  pitch: 70,
  hash: true,
  style: {
    version: 8,
    sources: {
      osm: {
        type: "raster",
        tiles: ["https://a.tile.openstreetmap.org/{z}/{x}/{y}.png"],
        tileSize: 256,
        attribution: "&copy; OpenStreetMap Contributors",
        maxzoom: 19,
      },
      terrainSource: {
        type: "raster-dem",
        url: "https://tiles.mapterhorn.com/tilejson.json",
      },
      hillshadeSource: {
        type: "raster-dem",
        url: "https://tiles.mapterhorn.com/tilejson.json",
      },
    },
    layers: [
      {
        id: "osm",
        type: "raster",
        source: "osm",
      },
      {
        id: "hills",
        type: "hillshade",
        source: "hillshadeSource",
        layout: { visibility: "visible" },
        paint: { "hillshade-shadow-color": "#473B24" },
      },
    ],
    terrain: {
      source: "terrainSource",
      exaggeration: 2,
    },
    sky: {},
  },
  maxZoom: 18,
  maxPitch: 85,
});

map.addControl(
  new maplibregl.NavigationControl({
    visualizePitch: true,
    showZoom: true,
    showCompass: true,
  }),
);

map.addControl(
  new maplibregl.TerrainControl({
    source: "terrainSource",
    exaggeration: 2,
  }),
);

map.on("load", () => {
  map.addSource("parcels", {
    type: "geojson",
    data: parcelUrl,
  });

  // 1. ADD AN INVISIBLE FILL LAYER FOR CLICK INTERACTION
  map.addLayer({
    id: "parcels-fill-layer",
    type: "fill",
    source: "parcels",
    paint: {
      "fill-color": "#000000",
      "fill-opacity": 0.0, // 0.0 makes it completely invisible but still clickable
    },
  });

  // 2. KEEP YOUR VISIBLE OUTSIDE LINE LAYER
  map.addLayer({
    id: "parcels-layer",
    type: "line",
    source: "parcels",
    paint: { "line-color": "#f79400", "line-width": 3 },
  });

  // --- POPUP LOGIC START ---

  const popup = new maplibregl.Popup({
    closeButton: true,
    closeOnClick: true,
  });

  // TARGET THE FILL LAYER INSTEAD OF THE LINE LAYER
  map.on("click", "parcels-fill-layer", (e) => {
    if (!e.features || e.features.length === 0) return;

    const feature = e.features[0];
    const properties = feature.properties;

    let popupHTML = `<div style="font-family: sans-serif; padding: 5px; color: #333;">`;
    popupHTML += `<h3 style="margin-top: 0;">Parcel Details</h3>`;

    if (Object.keys(properties).length === 0) {
      popupHTML += `<p>No attributes available.</p>`;
    } else {
      for (const [key, value] of Object.entries(properties)) {
        popupHTML += `<p style="margin: 4px 0;"><strong>${key}:</strong> ${value}</p>`;
      }
    }
    popupHTML += `</div>`;

    popup.setLngLat(e.lngLat).setHTML(popupHTML).addTo(map);
  });

  // UPDATE HOVER CURSOR ON THE FILL LAYER
  map.on("mouseenter", "parcels-fill-layer", () => {
    map.getCanvas().style.cursor = "pointer";
  });

  map.on("mouseleave", "parcels-fill-layer", () => {
    map.getCanvas().style.cursor = "";
  });

  // --- POPUP LOGIC END ---

  // 3. Fetch the source data independently to calculate bounds and execute camera zoom
  fetch(parcelUrl)
    .then((response) => response.json())
    .then((geojson) => {
      const getCoordinates = (geom) => {
        if (!geom) return [];
        if (geom.type === "Point") return [geom.coordinates];
        if (geom.type === "LineString" || geom.type === "MultiPoint")
          return geom.coordinates;
        if (geom.type === "Polygon" || geom.type === "MultiLineString")
          return geom.coordinates.flat(1);
        if (geom.type === "MultiPolygon") return geom.coordinates.flat(2);
        return [];
      };

      let coords = [];

      if (geojson.type === "FeatureCollection") {
        geojson.features.forEach((f) =>
          coords.push(...getCoordinates(f.geometry)),
        );
      } else if (geojson.type === "Feature") {
        coords = getCoordinates(geojson.geometry);
      } else {
        coords = getCoordinates(geojson);
      }

      if (coords.length === 0) return;

      let minLng = Infinity,
        minLat = Infinity,
        maxLng = -Infinity,
        maxLat = -Infinity;

      coords.forEach((coord) => {
        if (coord && coord.length >= 2) {
          const lng = coord[0];
          const lat = coord[1];
          if (lng < minLng) minLng = lng;
          if (lat < minLat) minLat = lat;
          if (lng > maxLng) maxLng = lng;
          if (lat > maxLat) maxLat = lat;
        }
      });

      const bounds = [
        [minLng, minLat],
        [maxLng, maxLat],
      ];

      map.fitBounds(bounds, {
        padding: 40,
        maxZoom: 17,
        animate: false,
      });
    })
    .catch((err) => console.error("Error computing parcel zoom limits:", err));
});
