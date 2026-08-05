# Geospatial and Machine Learning Series

A five-phase, hands-on progression through a modern geospatial/ML tool stack,
coordinate systems and spatial indexing, geospatial deep learning, Earth
observation foundation models, spatial indexing/visualization, and
natural-language search over imagery.

## Practice project

**Colorado Front Range Fire & Water Explorer** public, non-Tribal data
throughout, so this is a clean sandbox to build skill before deciding whether
or how any of it ports back to CARE-governed work later. Suggested data:

- Marshall Fire (Dec 2021, Boulder County) burn scar and recovery
- Front Range snowpack/drought (SNOTEL stations, Colorado River headwaters)
- USGS stream gauges for a Front Range watershed of your choice

## Structure

| Phase | Folder | Tools | What you build |
|---|---|---|---|
| 1 | `01-foundations-pyproj-rtree/` | pyproj, rtree | Reproject two mismatched CO datasets by hand; build a spatial index over watershed boundaries |
| 2 | `02-pytorch-torchgeo/` | PyTorch, TorchGeo | Load a CRS-aware raster dataset and run a pretrained model on it |
| 3 | `03-earth-embeddings/` | AlphaEarth, GeoTessera | Train a small classifier on embeddings with a handful of hand-labeled points; compare open vs. proprietary embeddings on the same task |
| 4 | `04-indexing-visualization/` | H3, pydeck, Datashader | Bin embedding output into hex cells, render it interactively, then render full-resolution data at scale |
| 5 | `05-semantic-search/` | OpenCLIP / RemoteCLIP | Query your imagery in plain language |

Each notebook has a **Goal**, an **Exercise/Milestone**, and a
**Check yourself** prompt at the end. The code cells are stubs (`# TODO`)
for you to fill in, not solutions.

## Setup

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

Some phases need extra one-time setup:
- **Phase 3 (AlphaEarth):** requires a Google Earth Engine account 
  `ee.Authenticate()` before first use.
- **Phase 3 (GeoTessera):** check coverage for your chosen area/year before
  pulling embeddings as coverage isn't automatically global.
- **Phase 5 (RemoteCLIP):** download the pretrained checkpoint from the
  [RemoteCLIP repo](https://github.com/ChenDelong1999/RemoteCLIP), it loads
  directly into an OpenCLIP model.

## Suggested sequencing

1. Foundations (pyproj, rtree)
2. PyTorch and TorchGeo
3. Earth embeddings (AlphaEarth, then GeoTessera for comparison)
4. Indexing and visualization (H3 to pydeck, then Datashader once data is large)
5. Semantic search (OpenCLIP/RemoteCLIP) capstone

