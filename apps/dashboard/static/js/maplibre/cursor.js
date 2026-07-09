let selectedId = null;

export function enablePointerCursor(
  map,
  layerId,
  sourceId = "parcels",
  onClick = null,
) {
  map.on("mouseenter", layerId, () => {
    map.getCanvas().style.cursor = "pointer";
  });

  map.on("mouseleave", layerId, () => {
    map.getCanvas().style.cursor = "";
  });

  map.on("click", layerId, (e) => {
    const feature = e.features[0];

    if (selectedId !== null) {
      map.setFeatureState(
        { source: sourceId, id: selectedId },
        { selected: false },
      );
    }

    selectedId = feature.id;

    map.setFeatureState(
      { source: sourceId, id: selectedId },
      { selected: true },
    );

    if (onClick) {
      onClick(e, feature);
    }
  });

  map.on("click", (e) => {
    const features = map.queryRenderedFeatures(e.point, {
      layers: [layerId],
    });

    if (features.length) return;

    if (selectedId !== null) {
      map.setFeatureState(
        { source: sourceId, id: selectedId },
        { selected: false },
      );

      selectedId = null;
    }
  });
}
