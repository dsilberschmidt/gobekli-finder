# PoC 1 Pipeline Overview (sanitized)

This document describes the **structure and logic** of the PoC 1 processing
pipeline, without tying it to any specific AOI or coordinates.

The real implementation lives in a private repository; this overview is designed
to be reproducible by anyone with access to Sentinel-2 and DEM data.

---

## 1. Inputs (conceptual)

- Sentinel-2 L2A surface reflectance (10–20 m)
- Copernicus DEM (DSM) 30 m

Typical steps:

1. Clip S2 and DEM to POSITIVE and NEGATIVE AOIs.
2. Reproject to a consistent projected CRS (e.g. UTM zone of the area).
3. Store the results in a structured folder tree:

   - `processed/POS_MULTI/S2/`
   - `processed/POS_MULTI/DEM/`
   - `processed/NEG_NEAR/S2/`
   - `processed/NEG_NEAR/DEM/`

AOI definitions and exact paths are implementation-specific and not part of this
public package.

---

## 2. Stage 1 — Optical indices (S2)

From Sentinel-2 bands (B02, B03, B04, red-edge), the pipeline computes:

- Truecolor / RGB composites (B04–B03–B02)
- NDVI
- NDWI
- SAVI
- Red-edge NDVI
- Local NDVI standard deviation
- NDVI local contrast (e.g. 7×7 window)

Each product is saved as a GeoTIFF with proper CRS and metadata.

---

## 3. Stage 2 — DEM derivatives (30 m)

From Copernicus DEM 30 m (clipped AOIs), the pipeline computes:

- Hillshade (single azimuth)
- Multi-hillshade (e.g. 45, 135, 225, 315 degrees)
- Slope
- Topographic Position Index (TPI) with fixed window (e.g. 7×7)

These products are used to evaluate whether small mounds leave any detectable
geomorphic signature at this resolution.

---

## 4. Stage 3 — Textures

For a subset of products (NDVI, DEM-based):

- Local standard deviation
- Local contrast (e.g. 7×7)

These help characterize heterogeneity rather than absolute values.

---

## 5. POS / NEG catalogues

The core idea is **catalog-driven analysis**:

- POS catalog: known mounds (id, label, lon, lat, confidence, source, set, notes)
- NEG catalog: carefully chosen negative points in nearby similar terrain

In the private PoC, 8 tumuli were catalogued (4 conceptual TRAIN, 4 conceptual
TEST). Here we only include a **sanitized** example table (`catalog_public.csv`),
without real coordinates.

---

## 6. Standardized figure generation

For each TRAIN tumulus, the pipeline:

1. Transforms its lon/lat to the raster CRS.
2. Extracts a 1000 × 1000 m window centered on the site.
3. Generates 4 figures:
   - NDVI
   - Truecolor
   - Hillshade (30 m)
   - TPI (7×7)

All figures share the same spatial extent and include a marker at the center.

In the private repo these figures are stored under `figures/` and used for
qualitative inspection.

---

## 7. Why the pipeline stops before ML

Although the code base is ready to feed features into a classifier, PoC 1 is
explicitly stopped **before** machine learning because:

- too few positive examples (4 TRAIN),
- no fully populated NEG catalog yet,
- DEM 30 m + S2 10 m do not show a strong, diagnostic signature.

Running ML at this stage would mostly measure noise or overfit, without adding
real insight.

