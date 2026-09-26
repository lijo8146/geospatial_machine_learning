# Primary references

Consulted while completing the course. Optional integrations may change independently of the default lessons.

- [pyproj Transformer](https://pyproj4.github.io/pyproj/stable/api/transformer.html): CRS transformation and axis order.
- [Rtree tutorial](https://rtree.readthedocs.io/en/stable/tutorial.html): bounding-box indexing.
- [TorchGeo pretrained weights](https://docs.torchgeo.org/en/stable/tutorials/pretrained_weights.html): model metadata and weight loading. Course optional environment targets 0.9; latest docs may use newer samplers.
- [TorchGeo custom raster datasets](https://docs.torchgeo.org/en/stable/tutorials/custom_raster_dataset.html): raster metadata and band configuration.
- [Google Satellite Embedding V1](https://developers.google.com/earth-engine/datasets/catalog/GOOGLE_SATELLITE_EMBEDDING_V1_ANNUAL): official annual collection and A00–A63 dimensions.
- [GeoTessera](https://github.com/ucam-eo/geotessera): coverage registry and tile retrieval.
- [H3 Python API](https://uber.github.io/h3-py/api_quick.html): `latlng_to_cell` and cell operations.
- [pydeck H3HexagonLayer](https://deckgl.readthedocs.io/en/latest/gallery/h3_hexagon_layer.html): render existing H3 cells.
- [Datashader pipeline](https://datashader.org/getting_started/Pipeline.html): aggregate and shade.
- [RemoteCLIP](https://github.com/ChenDelong1999/RemoteCLIP): matching OpenCLIP architectures and checkpoints.

The starter's `GOOGLE/ALPHAEARTH/FEATURES/V1` placeholder was replaced with the documented annual collection. Existing H3 indices are displayed with H3HexagonLayer rather than re-binned with HexagonLayer. Coverage must be checked per product/year rather than inferred from older descriptions.
