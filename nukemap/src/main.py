import geopandas as gpd
from shapely.geometry import Point
import sys
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

INPUT_DIR = BASE_DIR / "input"
OUTPUT_DIR = BASE_DIR / "output"

EPICENTER_FILE = INPUT_DIR / "epicenter.txt"
POPU_MAP = INPUT_DIR / "HU-grid-popu-centroid_EOV.geojson"
RESULT_FILE = OUTPUT_DIR / "result.txt"


# ---- EPICENTRUM BEOLVASÁSA FÁJLBÓL ----
with open(EPICENTER_FILE, "r", encoding="utf-8") as f:
    line = f.readline().strip()
    lon, lat = map(float, line.split(","))

# ---- NÉPESSÉG ADAT BETÖLTÉS ----
pop_map = gpd.read_file(POPU_MAP)

# CRS biztosítás
if pop_map.crs is None:
    pop_map.set_crs(epsg=23700, inplace=True)

# ---- EPICENTRUM GEOMETRIA ----
epicenter = gpd.GeoSeries(
    [Point(lon, lat)],
    crs="EPSG:4326"
)

# ---- ÁTVETÍTÉS BUFFERELÉSHEZ ----
pop_map_proj = pop_map.to_crs(epsg=23700)
epicenter_proj = epicenter.to_crs(epsg=23700)

# ---- FIX NUKEMAP SUGARAK (m) ----
BUFFERS = {
    "Tűzgömb": 500,
    "Lökéshullám": 1500,
    "Hősugárzás": 3000
}

# ---- SZÁMÍTÁS ----
results = []

for name, radius in BUFFERS.items():
    buffer_geom = epicenter_proj.buffer(radius).iloc[0]
    affected = pop_map_proj[pop_map_proj.intersects(buffer_geom)]
    pop_sum = affected["T"].sum()

    results.append({
        "zona": name,
        "sugar": radius,
        "pontok": len(affected),
        "nepesseg": int(pop_sum)
    })

# ---- EREDMÉNY KIÍRÁSA ----
with open(RESULT_FILE, "w", encoding="utf-8") as f:
    f.write("NUKEMAP-SZERŰ NÉPESSÉGÉRINTETTSÉG\n")
    f.write("--------------------------------\n")
    f.write(f"Epicentrum (lon, lat): {lon}, {lat}\n\n")

    for r in results:
        f.write(f"{r['zona']}:\n")
        f.write(f"  Sugár: {r['sugar']} m\n")
        f.write(f"  Lefedett pontok: {r['pontok']}\n")
        f.write(f"  Érintett népesség: {r['nepesseg']}\n\n")

print("Számítás kész", RESULT_FILE)