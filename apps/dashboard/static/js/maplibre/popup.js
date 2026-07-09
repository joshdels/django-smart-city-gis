export function showParcelPopup(map, feature, lngLat) {
  const popup = new maplibregl.Popup({
    closeButton: true,
    closeOnClick: true,
  });

  const properties = feature.properties;
  const parcelId = feature.id;

  let popupHTML = `<h3>Parcel Details</h3>`;

  for (const [key, value] of Object.entries(properties)) {
    popupHTML += `<p><strong>${key}:</strong> ${value}</p>`;
  }

  popupHTML += `
    <a class="btn-primary" href="/dashboard/parcel-detail/${parcelId}">
      View Details
    </a>`;

  popup.setLngLat(lngLat).setHTML(popupHTML).addTo(map);
}
