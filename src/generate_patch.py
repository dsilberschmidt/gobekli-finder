#!/usr/bin/env python3

"""
generate_patch.py
------------------

Generic Earth Observation utility for extracting and visualizing
local patches of multispectral and DEM data.

Designed for:
- Sentinel-2 (B02, B03, B04 or others)
- Copernicus DEM or other elevation models
- Any project requiring reproducible EO patch analysis

This script:
- Takes lon/lat center and extraction radius (meters)
- Generates NDVI-proxy (if NIR not provided), truecolor, hillshade-proxy, and TPI (if DEM provided)
- Saves all outputs into ./figures/

Fully general-purpose. No domain assumptions.
"""

import argparse
import os
import numpy as np
import rasterio
from rasterio.enums import Resampling
from rasterio.windows import Window
from pyproj import Transformer
import matplotlib.pyplot as plt

# ------------------------------
# Helpers
# ------------------------------

def extract_window(raster_path, lon, lat, radius_m):
    """Extract a square window centered at lon/lat with given radius in meters."""
    with rasterio.open(raster_path) as src:
        transformer = Transformer.from_crs("EPSG:4326", src.crs, always_xy=True)
        x, y = transformer.transform(lon, lat)
        px, py = src.index(x, y)
        r = int(radius_m / src.res[0])
        win = Window(px - r, py - r, 2*r, 2*r)
        data = src.read(1, window=win, resampling=Resampling.bilinear)
        return data


def save_fig(array, cmap, title, outfile):
    """Utility to save a matplotlib figure."""
    plt.figure(figsize=(6,6))
    plt.imshow(array, cmap=cmap)
    plt.title(title)
    plt.axis("off")
    plt.savefig(outfile, dpi=300, bbox_inches="tight")
    plt.close()


# ------------------------------
# Main
# ------------------------------

def main():
    parser = argparse.ArgumentParser(description="Generate EO patch (truecolor, NDVI-proxy, hillshade, TPI).")

    parser.add_argument("--id", required=True, help="Identifier for output naming")
    parser.add_argument("--lon", type=float, required=True)
    parser.add_argument("--lat", type=float, required=True)
    parser.add_argument("--radius", type=int, default=300, help="Half-size of extracted window (meters)")

    parser.add_argument("--b02", required=True, help="Path to Sentinel-2 B02")
    parser.add_argument("--b03", required=True, help="Path to Sentinel-2 B03")
    parser.add_argument("--b04", required=True, help="Path to Sentinel-2 B04")
    parser.add_argument("--dem", required=False, help="DEM file (optional)")

    args = parser.parse_args()

    outdir = "figures"
    os.makedirs(outdir, exist_ok=True)

    id_tag = args.id

    # --------------------------
    # NDVI-proxy (B03 vs B04)
    # --------------------------
    b04 = extract_window(args.b04, args.lon, args.lat, args.radius)
    b03 = extract_window(args.b03, args.lon, args.lat, args.radius)

    num = (b03.astype(float) - b04.astype(float))
    den = (b03.astype(float) + b04.astype(float) + 1e-6)
    ndvi_proxy = num / den

    save_fig(ndvi_proxy, "RdYlGn", f"{id_tag} – NDVI-proxy", f"{outdir}/{id_tag}_NDVIproxy.png")

    # --------------------------
    # TRUECOLOR
    # --------------------------
    b02 = extract_window(args.b02, args.lon, args.lat, args.radius)
    rgb = np.dstack([b04, b03, b02])
    rgb = rgb / np.percentile(rgb, 98)
    rgb = np.clip(rgb, 0, 1)

    plt.figure(figsize=(6,6))
    plt.imshow(rgb)
    plt.title(f"{id_tag} – Truecolor")
    plt.axis("off")
    plt.savefig(f"{outdir}/{id_tag}_TRUECOLOR.png", dpi=300, bbox_inches="tight")
    plt.close()

    # --------------------------
    # DEM-based layers (optional)
    # --------------------------
    if args.dem:
        dem = extract_window(args.dem, args.lon, args.lat, args.radius)

        # Hillshade-proxy via gradient magnitude
        gy, gx = np.gradient(dem.astype(float))
        slope = np.sqrt(gx*gx + gy*gy)
        save_fig(slope, "gray", f"{id_tag} – Hillshade-proxy", f"{outdir}/{id_tag}_HILLSHADE.png")

        # TPI (7×7)
        kernel = np.ones((7,7), dtype=float)
        mean_local = (
            np.convolve(dem.flatten(), kernel.flatten(), mode="same")
            .reshape(dem.shape) / 49.0
        )
        tpi = dem.astype(float) - mean_local
        save_fig(tpi, "coolwarm", f"{id_tag} – TPI (7×7)", f"{outdir}/{id_tag}_TPI.png")

    print(f"Done. Outputs written to: {outdir}/")

if __name__ == "__main__":
    main()

