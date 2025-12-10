# Göbekli Finder — PoC 1 (Kazanlak, 2 ka, S2 + DEM 30 m)

## Scope of this public PoC package

This folder contains a **sanitized, public-facing summary** of the first
Göbekli Finder proof-of-concept:

- **Region:** Kazanlak valley (Bulgaria) — generalized, no exact coordinates.
- **Period of interest:** ~2 ka (Thracian tumuli).
- **Data types evaluated:**
  - Sentinel-2 optical (10–20 m)
  - Copernicus DEM (DSM) 30 m

No raw rasters or exact archaeological coordinates are included here.
This package is **method-focused**, not data-distribution–focused.

---

## Main question

> Can medium-resolution public datasets (S2 + DEM 30 m) provide a detectable,
> repeatable signature for known small burial mounds, such that the same signal
> could be used to suggest unknown candidates?

The answer, based on this PoC, is:

- **For microtopography / shape:** effectively **no** at 30 m DEM.
- **For vegetation contrast (NDVI):** only **weak, non-diagnostic signals**.

---

## What is included in this folder

- `README_PUBLIC_POC.md` — this document.
- `pipeline_overview.md` — description of the processing chain and scripts.
- `catalog_public.csv` — sanitized example of a POS catalog (schema + fake/jittered coordinates).
- `lessons_learned.md` — concise summary of technical and scientific lessons.

These files are enough to:

- understand the design of PoC 1,
- see why it stops before ML,
- reuse the methodology for other areas/datasets.

---

## What is explicitly not included

- No raw Sentinel-2 tiles.
- No DEM tiles.
- No hillshade / TPI rasters tied to real coordinates.
- No exact coordinates of archaeological sites.

Anyone wishing to replicate the study must:

1. Obtain their own data (S2, DEM or higher-resolution sources).
2. Apply the pipeline to their AOI.
3. Respect local archaeological and heritage guidelines.

---

## Status of PoC 1

PoC 1 is **frozen** at the stage of:

- fully documented AOIs (private),
- 8 real tumuli catalogued (private coordinates),
- standardized figure generation around 4 TRAIN tumuli,
- qualitative comparison of optical and DEM-derived products.

The PoC concludes that:

- DEM 30 m does not resolve the mounds as individual geomorphic objects.
- NDVI shows only weak, context-dependent anomalies.
- A meaningful ML detector would require:
  - more POS/NEG examples, and
  - finer spatial resolution (DEM ≤ 2–5 m, RGB ≤ 1–2 m).

