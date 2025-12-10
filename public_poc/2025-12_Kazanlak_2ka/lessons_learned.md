# PoC 1 — Lessons Learned (public summary)

This document summarizes the main technical and scientific lessons from
Göbekli Finder PoC 1, in a way that is safe to share publicly.

---

## 1. Resolution dominates everything

Small mounds (tens of meters across, < 20 m high) are effectively invisible at:

- DEM 30 m,
- optical 10–20 m, in terms of shape or convexity.

No choice of hillshade parameters or TPI windowing can compensate for a DEM that
does not resolve the target.

**Takeaway:** before thinking about algorithms, check that the spatial resolution
is even capable of seeing the object of interest.

---

## 2. DEM 30 m provides contextual, not object-level information

At 30 m:

- valley vs. ridge vs. slope can be distinguished,
- microtopography such as individual tumuli cannot.

The tumuli in PoC 1 tend to occupy:

- slope shoulders,
- gentle interfluves,
- near minor drainage lines.

This is a **contextual pattern**, not a unique geomorphic signature.

---

## 3. NDVI anomalies are weak and non-diagnostic

NDVI occasionally shows:

- slightly different vegetation patches over or near mounds,
- subtle texture or greenness differences.

However:

- similar patches appear across the landscape,
- the signal is not uniquely tied to tumuli,
- season and land use strongly affect visibility.

**Takeaway:** NDVI alone is not a reliable “tumulus detector” at this scale.

---

## 4. Negative results are still results

PoC 1 provides a robust, well-documented **negative result**:

> With DEM 30 m and Sentinel-2, small Thracian mounds do not show a strong
> separable signal suitable for automatic detection.

This is useful because it:

- prevents overpromising,
- guides future data acquisition (e.g. DEM 1–2 m, RGB ≤ 1 m),
- clarifies realistic expectations for open EO datasets.

---

## 5. Reproducible scripts outperform ad-hoc desktop workflows

An initial attempt to use QGIS for visualization encountered repeated issues
with raster loading and dependencies. Migrating to:

- pure Python,
- rasterio + GDAL + NumPy,
- scripted figure generation,

resulted in a fully reproducible setup:

- same figures for every run,
- no manual layout or zoom decisions,
- easier to share and review.

**Takeaway:** for scientific PoCs, scripts should be the primary interface;
desktop GIS tools are optional and secondary.

