# Working glossary

- **CRS:** the coordinate reference system defining how coordinates relate to Earth.
- **Reprojection:** computing new coordinates in a different CRS; assigning a CRS changes metadata only.
- **Spatial index:** a candidate-search structure; exact geometry still determines membership.
- **Raster transform:** a mapping from row/column positions to geographic or projected coordinates.
- **Embedding:** a learned numeric representation; individual dimensions usually lack physical interpretation.
- **Spatial leakage:** training and test data share location-dependent information, undermining evaluation.
- **Spatial block:** a geographic group held together during train/test partitioning.
- **Balanced accuracy:** mean recall across classes; useful when class frequencies differ.
- **Baseline:** a simple reference method that gives a score practical context.
- **H3:** a hierarchical geographic cell index; cell resolution is not model accuracy.
- **Aggregation:** combining observations into a statistic over an area or display pixel.
- **Cosine similarity:** dot product of unit-length vectors; a ranking score rather than calibrated probability.
- **Precision@k:** fraction of the top k retrieved candidates judged relevant under a stated rubric.
- **Provenance:** a record of data sources, dates, permissions and transformations.
