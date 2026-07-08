import { zoomToFit } from "./zoomFit.js";

class RezoomControl {
  constructor(parcelUrl) {
    this._parcelUrl = parcelUrl;
  }

  onAdd(map) {
    this._map = map;

    this._container = document.createElement("div");
    this._container.className = "maplibregl-ctrl maplibregl-ctrl-group";

    this._button = document.createElement("button");
    this._button.type = "button";
    this._button.className = "maplibregl-ctrl-icon";
    this._button.style.fontFamily = "sans-serif";
    this._button.style.fontSize = "11px";
    this._button.style.fontWeight = "bold";
    this._button.innerText = "FIT";
    this._button.title = "Zoom to Parcel";

    this._button.addEventListener("click", () => {
      if (this._parcelUrl) {
        zoomToFit(this._map, this._parcelUrl);
      }
    });

    this._container.appendChild(this._button);
    return this._container;
  }

  onRemove() {
    this._container.parentNode.removeChild(this._container);
    this._map = undefined;
  }
}

class Custom3DTerrainControl {
  onAdd(map) {
    this._map = map;
    this._is3D = false;

    this._container = document.createElement("div");
    this._container.className = "maplibregl-ctrl maplibregl-ctrl-group";

    this._button = document.createElement("button");
    this._button.type = "button";
    this._button.className = "maplibregl-ctrl-icon";
    this._button.style.fontFamily = "sans-serif";
    this._button.style.fontSize = "12px";
    this._button.style.fontWeight = "bold";
    this._button.innerText = "3D";
    this._button.title = "Toggle 3D View";

    this._button.addEventListener("click", () => this.toggle3D());
    this._container.appendChild(this._button);
    return this._container;
  }

  onRemove() {
    this._container.parentNode.removeChild(this._container);
    this._map = undefined;
  }

  toggle3D() {
    if (!this._is3D) {
      this._map.setTerrain({ source: "terrainSource", exaggeration: 2 });
      this._map.easeTo({
        pitch: 65,
        bearing: -15,
        duration: 1000,
      });
      this._button.innerText = "2D";
      this._button.style.color = "#f4530a";
      this._is3D = true;
    } else {
      this._map.setTerrain(null);
      this._map.easeTo({
        pitch: 0,
        bearing: 0,
        duration: 1000,
      });
      this._button.innerText = "3D";
      this._button.style.color = "";
      this._is3D = false;
    }
  }
}

// 2. NOW IT ONLY NEEDS THE MAP AND PARCEL URL
export function addMapControls(map, parcelUrl) {
  map.addControl(
    new maplibregl.NavigationControl({
      visualizePitch: true,
      showZoom: true,
      showCompass: true,
    }),
  );

  map.addControl(new Custom3DTerrainControl(), "top-right");

  // Passes the parcelUrl down cleanly
  map.addControl(new RezoomControl(parcelUrl), "top-right");
}
