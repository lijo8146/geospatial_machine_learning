# Phase 3 · Earth Embeddings AlphaEarth and GeoTessera

Test whether pretrained embeddings can get you a usable classifier with a
fraction of the labeling effort a from-scratch model would need and get
firsthand evidence on the open-weights-vs-proprietary question rather than an
abstract opinion about it.

- `01_alphaearth_classifier.ipynb` small classifier on AlphaEarth's 64-dim
  embeddings (Google Earth Engine)
- `02_geotessera_comparison.ipynb` the same exercise on TESSERA's 128-dim
  embeddings (open weights, Cambridge)

Run both on the *same* labeled points so the comparison is apples-to-apples.
Check GeoTessera's coverage for your area before starting notebook 02 
unlike AlphaEarth, coverage isn't automatically global.
