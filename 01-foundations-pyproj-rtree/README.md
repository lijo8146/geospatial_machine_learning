# Phase 1 · Foundations — pyproj + rtree

Low time investment, do this first. These are "necessary correctness" tools —
the plumbing everything else (geopandas, TorchGeo, H3) sits on top of.

- `01_pyproj_reprojection.ipynb` — reproject two mismatched Colorado datasets
  by hand
- `02_rtree_spatial_index.ipynb` — build a spatial index over watershed
  boundaries and query it

Goal for this phase: recognize a CRS mismatch or a slow spatial join when you
see one later, even if a higher-level library is usually handling it for you.
