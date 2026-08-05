# Phase 4 · Indexing + Visualization — H3, pydeck, Datashader

Turn Phase 3's embedding output into something you can actually look at and
demo, at two different scales of data.

- `01_h3_binning.ipynb` — bin embedding output into H3 cells at coarse and
  fine resolutions
- `02_pydeck_hexlayer.ipynb` — render the H3-binned output as an interactive
  map (the direct payoff of notebook 01)
- `03_datashader_fullres.ipynb` — render the *full-resolution*, un-binned
  data at scale, and compare against pydeck's behavior on the same data

Do 03 only once your data is genuinely large enough that pydeck starts to
struggle — otherwise you won't see the difference Datashader is for.
