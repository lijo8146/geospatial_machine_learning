# Geospatial and Machine Learning: a guided learning series

Nine lessons move from coordinate systems to image retrieval through a Colorado Front Range Fire & Water Explorer learning project. The aim is to explain and evaluate a workflow.

**Start here:** know Python variables, functions, arrays and DataFrames. No deep-learning background is required. Plan roughly 10–15 hours for worked lessons and exercises, plus 4–8 hours for the real-data capstone and downloads.

## Two learning paths

The **practice path** runs all nine notebooks without credentials or model downloads after installation. It uses explicitly synthetic points, polygons, rasters and vectors. These teach mechanics.

The **real-data labs** add TorchGeo pretrained inference, AlphaEarth/TESSERA extraction and RemoteCLIP retrieval. They require extra packages, public input data, model downloads and (for Earth Engine) your own registered project. Follow [the real-data guide](docs/REAL_DATA.md). They are optional for the practice path but required for a real-data capstone.

## Setup

Use Python 3.11 or 3.12 for practice; use 3.12 for the full optional stack. From the repository root:

```powershell
py -3.12 -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m ipykernel install --user --name geospatial-course --display-name "Geospatial course"
python -m jupyter lab
```

On macOS/Linux: `python3.12 -m venv .venv` then `source .venv/bin/activate`; remaining commands are the same. If PowerShell activation is blocked, call `.venv\Scripts\python.exe` directly. Select the **Geospatial course** kernel. Start Jupyter at the repo root; each lesson also works when launched from its own folder.

## Course sequence

| Lesson | Question | Evidence of learning |
|---|---|---|
| [1.1 Reprojection](01-foundations-pyproj-rtree/01_pyproj_reprojection.ipynb) | How can different coordinates describe the same place? | Round-trip assertion and aligned overlay |
| [1.2 R-tree](01-foundations-pyproj-rtree/02_rtree_spatial_index.ipynb) | Why isn't a bounding-box hit a match? | Hole counterexample and timing comparison |
| [2.1 TorchGeo](02-pytorch-torchgeo/01_torchgeo_intro.ipynb) | What connects a raster window to a model tensor? | CRS, pixel center and channel checks |
| [3.1 AlphaEarth](03-earth-embeddings/01_alphaearth_classifier.ipynb) | How do we test without leaking geography? | Spatial holdout, baseline and learning curve |
| [3.2 TESSERA](03-earth-embeddings/02_geotessera_comparison.ipynb) | What makes a comparison fair? | Aligned IDs and shared evaluation cohort |
| [4.1 H3](04-indexing-visualization/01_h3_binning.ipynb) | How does scale change a summary? | Conserved counts and weighted means |
| [4.2 pydeck](04-indexing-visualization/02_pydeck_hexlayer.ipynb) | What does a map actually claim? | H3 map with score/count tooltips |
| [4.3 Datashader](04-indexing-visualization/03_datashader_fullres.ipynb) | What can a pixel summarize? | One-million-record rendering and timing |
| [5.1 RemoteCLIP](05-semantic-search/01_remoteclip_retrieval.ipynb) | What does similarity prove? | Ranked results and relevance critique |

Each lesson includes objectives, concepts, runnable worked examples, an independent exercise, an expandable solution, a check-yourself prompt and a real-data extension. Predict outputs before running. Try the exercise before reading its solution. Record your own results and limitations.

## Finish the series

Use the [learner workbook](docs/WORKBOOK.md), [capstone brief and rubric](docs/CAPSTONE.md), and [instructor guide](docs/INSTRUCTOR.md). [Concept glossary](docs/GLOSSARY.md) and [source references](docs/REFERENCES.md) support review.

Generated practice products live in `data/generated/`; real observations stay in `data/real/`. Notebook code displays the core methods; `course.py` contains small shared fixtures and evaluation helpers worth reading.

## Verify your environment

```powershell
python -m unittest discover -s tests -v
python scripts/validate_course.py --kernel geospatial-course
```

The runner executes notebooks in their own directories and writes executed copies to ignored `runs/`. External labs remain disabled by default and are reported separately. See [validation notes](docs/VALIDATION.md) for the checks actually performed during development. Dependency ranges constrain major API changes; they are not a fully locked cross-platform environment. Save `python -m pip freeze` with your capstone.
