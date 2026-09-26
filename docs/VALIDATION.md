# Validation record

All nine default notebooks executed successfully from their individual lesson folders using fresh Jupyter kernels. Executed copies and the machine-readable report are in ignored `runs/`.

Four unittest checks passed: group separation, missing-vector rejection, duplicate-ID rejection, and H3 count/weighted-mean conservation. Python source compilation and `git diff --check` also passed.

The execution environment was Windows, Python 3.11, with an isolated venv inheriting an existing scientific Python environment. Its conda PROJ/DLL paths needed explicit environment setup; this is not a clean installation test. The repository's recommended fresh Python 3.12 setup was not independently tested. Browser hover/render behavior was not interactively tested; HTML generation succeeded.

External Earth Engine/TESSERA downloads, TorchGeo model execution and RemoteCLIP checkpoints/inference were not executed. Those paths are provided as explicit optional labs with source references and prerequisites, not claimed as verified scientific results. Synthetic classification metrics cannot validate real-model performance.

## Versions exercised

- numpy: 2.4.6
- pandas: 2.3.3
- matplotlib: 3.11.1
- geopandas: 1.1.4
- shapely: 2.1.2
- pyproj: 3.7.2
- rtree: 1.4.1
- rasterio: 1.4.4
- scikit-learn: 1.8.0
- h3: 4.5.0
- pydeck: 0.9.3
- datashader: 0.19.1
- nbclient: 0.10.4
