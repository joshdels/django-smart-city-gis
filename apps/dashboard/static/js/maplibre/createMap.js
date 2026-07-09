export function createMap(container = "map") {
  return new maplibregl.Map({
    container: container,
    zoom: 12,
    center: [11.39085, 47.27574],
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
      ],
      sky: {},
    },
    maxZoom: 19,
    maxPitch: 85,
  });
}
