import { createMap } from "./maplibre/createMap.js";
import { addMapControls } from "./maplibre/controls.js";
import { addParcelLayer, addParcelSources } from "./maplibre/layer.js";
import { addPopupParcel } from "./maplibre/popup.js";
import { enablePointerCursor } from "./maplibre/cursor.js";
import { zoomToFit } from "./maplibre/zoomFit.js";

const parcelUrl = `/parcels/show-parcels/`;

const map = createMap("map");

addMapControls(map, parcelUrl);

map.on("load", () => {
  addParcelSources(map, parcelUrl);
  addParcelLayer(map);
  addPopupParcel(map, "parcels-fill-layer");
  enablePointerCursor(map, "parcels-fill-layer");
  zoomToFit(map, parcelUrl);
});
