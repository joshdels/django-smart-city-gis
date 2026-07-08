const BASE_URL =
  window.location.hostname === "127.0.0.1" ||
  window.location.hostname === "localhost"
    ? "http://127.0.0.1:8000"
    : "https://topmapsolutions.com";

const parcelUrl = `${BASE_URL}/parcels/parcel-detail/${parcelId}/`;

const map = new maplibregl.Map({
  container: "map",
  zoom: 12,
  center: [0, 0],
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


  // 2. KEEP YOUR VISIBLE OUTSIDE LINE LAYER
  map.addLayer({
    id: "parcels-layer",
    type: "line",
    source: "parcels",
    paint: { "line-color": "#ffa318", "line-width": 5 },
  });


  // i might separate this stuff
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
        padding: 50,
        maxZoom: 18,
        animate: false,
      });
    })
    .catch((err) => console.error("Error computing parcel zoom limits:", err));
});
