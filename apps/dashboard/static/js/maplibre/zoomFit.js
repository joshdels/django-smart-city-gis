export function zoomToFit(map, parcelUrl) {
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
        padding: 100,
        animate: false,
        linear: true,
      });
    })
    .catch((err) => console.error("Error computing parcel zoom limits:", err));
}
