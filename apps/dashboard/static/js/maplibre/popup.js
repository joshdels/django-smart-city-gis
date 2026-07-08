export function addPopupParcel(map, layerId) {
  const popup = new maplibregl.Popup({
    closeButton: true,
    closeOnClick: true,
  });

  map.on("click", layerId, (e) => {
    if (!e.features || e.features.length === 0) return;

    const feature = e.features[0];
    const properties = feature.properties;
    const parcelId = feature.id;

    // Popup detail
    let popupHTML = `<h3 style="margin-top: 0;">Parcel Details</h3>`;

    if (Object.keys(properties).length === 0) {
      popupHTML += `<p>No attributes available.</p>`;
    } else {
      for (const [key, value] of Object.entries(properties)) {
        popupHTML += `<p style="margin: 4px 0;"><strong>${key}:</strong> ${value}</p>`;
      }

      popupHTML += `  
      <a class="btn-primary" href="/dashboard/parcel-detail/${parcelId}">
        View Details
      </a>`;
    }

    popup.setLngLat(e.lngLat).setHTML(popupHTML).addTo(map);
  });
}
