# Göbekli Finder (Public)

Open-source pipeline to detect circular mounds / ritual enclosures (Göbekli-style) using DEM + NDVI + SAR.

## Quickstart (no BS)

```bash
# 1) Create env
conda env create -f environment.yml && conda activate gobekli-finder
#    or:  pip install -r requirements.txt

# 2) Put datasets (GeoTIFF) in ./examples/demo_area/
#    Required: dem.tif
#    Optional: ndvi.tif, s1_vv.tif

# 3) Run
python src/gobekli_finder_plus.py   --dem examples/demo_area/dem.tif   --ndvi examples/demo_area/ndvi.tif   --sar examples/demo_area/s1_vv.tif   --out results/candidates.geojson   --min_diam 30 --max_diam 400 --min_height 2 --max_height 30   --flood_slope_max 2.5 --flood_frac_min 0.6   --hough_low 0.8 --hough_high 1.2 --hough_step 0.05
```

**Outputs:** GeoJSON sorted by `score_final` with fields: circularity, height_m, ring_score, floodplain_penalty, etc.

> ⚠️ **Do not include sensitive coordinates in this repo.** Use the private repository for real data.

## Repo layout
```
src/                     # core scripts
docs/                    # concept note / thesis proposal
examples/                # non-sensitive demo area (placeholders)
results/                 # generated outputs (gitignored)
```

## Citation
Silberschmidt, D. (2025). *Göbekli Finder – Remote detection of pre-agricultural megalithic enclosures (v0.1).* MIT License.

---

# Current Status of the Göbekli Finder Project

This repository hosts the **public-facing tools, documentation, and concept notes**
for the Göbekli Finder project — an exploration of remote-sensing methods for 
detecting small archaeological mounds.

Göbekli Finder is **not** a finished system.  
It is a **proof-of-concept series**, each iteration evaluating whether specific 
datasets and methods can reveal faint geomorphological or vegetation signatures 
around known archaeological sites.

## PoC 1 (Dec 2025)
**Region:** Kazanlak Valley (Bulgaria)  
**Period:** ~2 ka  
**Data used:** Sentinel-2 (10–20 m), Copernicus DEM 30 m  
**Objective:** Determine whether publicly available Earth Observation data can 
detect or hint at Thracian burial mounds (túmulos) known from archaeology.

### Summary of findings
- DEM 30 m is **too coarse** to express the microtopography of 10–20 m mounds.  
- Hillshade and TPI (7×7 window) produce **no detectable signal**.  
- NDVI sometimes shows **weak vegetation anomalies**, but these are **not 
diagnostic** and produce many false positives.  
- A practical detection pipeline would require:
  - DEM ≤ 2 m (LIDAR),  
  - or RGB imagery ≤ 1 m (e.g., Maxar, Google),  
  - or high-resolution SAR.

This negative result is **scientifically valuable**:  
it shows the real limits of open EO datasets and prevents unrealistic expectations.

## About the private PoC repository
Development occurs in a private repository where:
- real coordinates are stored (never published here),  
- full rasters are processed,  
- experiments and intermediate failures are documented.

Periodic **sanitized public releases** will be exported here, containing:
- methodology,  
- scripts,  
- synthetic or jittered examples,  
- insights and lessons learned.

## Next public release planned
- **PoC 1 sanitized release** containing:
  - pipeline description,  
  - reproducible code (no real coordinates),  
  - summary of analyses T001–T007,  
  - limitations and recommended next steps.

