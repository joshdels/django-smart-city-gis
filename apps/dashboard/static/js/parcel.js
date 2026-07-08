import { createMap } from "./maplibre/createMap.js";
import { addMapControls } from "./maplibre/controls.js";
import { addParcelLayer, addParcelSources } from "./maplibre/layer.js";
import { zoomToFit } from "./maplibre/zoomFit.js";

const parcelUrl = `/parcels/parcel-detail/${parcelId}/`;

const map = createMap("map");
addMapControls(map, parcelUrl);

map.on("load", () => {
  addParcelSources(map, parcelUrl);
  addParcelLayer(map, 7);
  zoomToFit(map, parcelUrl);
});
