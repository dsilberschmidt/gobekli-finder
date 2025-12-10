# Public Example Figures (NEG_NEAR Demo)

This directory contains safe, non-sensitive example patches generated from the NEG_NEAR region.  
NEG_NEAR does not contain known archaeological features and serves exclusively as a demonstrative area.

Each patch is produced by the same preprocessing workflow used in the Göbekli Finder PoC:

- Sentinel-2 optical bands (B02, B03, B04)
- Copernicus DEM 30 m
- A fixed-radius window around a chosen coordinate
- A standard figure style for comparability
- A central magenta marker for orientation

## Figure Types

### NDVI (Normalized Difference Vegetation Index)
Highlights differences in vegetation density.  
Useful for qualitative anomaly inspection.

### Truecolor (RGB Composite)
Reconstructed from Sentinel-2 B04/B03/B02.  
Acts as a natural-color reference for land cover interpretation.

### Hillshade (DEM-derived)
Illumination model based on Copernicus DEM (30 m).  
Captures macro-relief, not micro-topography.

### Local TPI (Topographic Position Index, 7×7)
Measures local convexity/concavity.  
Useful as a geomorphological descriptor.

## Purpose
These examples demonstrate the pipeline capabilities without revealing any archaeological locations.  
All sensitive analyses are kept in the private repository.
