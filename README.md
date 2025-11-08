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
