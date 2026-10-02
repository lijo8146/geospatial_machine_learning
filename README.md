# Geospatial and Machine Learning: a guided learning series

Seventeen lessons move from coordinate systems to image retrieval and grounded text answers through a Colorado Front Range Fire & Water Explorer learning project. The aim is to explain and evaluate a workflow.

**For educators:** [Explore the teaching showcase](docs/FOR_EDUCATORS.md) for questions, student artifacts, suggested teaching times, and an assessable change-detection demonstration. These ideas can complement an existing curriculum.

**Start here:** know Python variables, functions, arrays and DataFrames. Plan roughly 23–30 hours for worked lessons and exercises, plus 4–8 hours for the real-data capstone and downloads.

## Two learning paths

The **practice path** uses synthetic data without credentials or model downloads. Fifteen notebooks use the base environment; lessons 8.3–8.4 additionally require PyTorch (see their setup cells or `requirements-lstm.txt`). All seventeen run offline once their packages are installed. It uses explicitly synthetic points, polygons, rasters and vectors. These teach mechanics.

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
| [5.2 Geospatial RAG](05-semantic-search/02_geospatial_rag.ipynb) | Can retrieved evidence support an answer? | Place/date filtering, retrieval metrics and citation review |
| [6.1 Change detection](06-change-detection/01_satellite_change_detection.ipynb) | What changed—and what only looks like change? | Masked change map, sensitivity table and artifact diagnosis |
| [7.1 Decision trees](07-decision-trees/01_geospatial_decision_tree.ipynb) | Can you explain a map prediction? | Tree diagram, traced path, validation comparison and held-out evaluation |
| [8.1 Simple ANN](08-neural-networks/01_simple_ann.ipynb) | How does a small neural network learn? | Forward pass, gradient check, learning curves and controlled experiment |
| [8.2 Simple CNN](08-neural-networks/02_simple_cnn.ipynb) | What does pixel arrangement reveal? | Manual convolution, learned feature maps, grouped evaluation and shuffle diagnostic |
| [8.3 Simple LSTM](08-neural-networks/03_simple_lstm.ipynb) | Does signal history improve the next prediction? | Gate demonstration, chronological windows, baseline comparison and validation experiment |
| [8.4 Simple attention](08-neural-networks/04_simple_attention.ipynb) | Which earlier observations does attention combine? | Worked attention, heatmap, positional ablation and matched forecasting baselines |
| [9.1 Active learning](09-active-learning/01_active_learning.ipynb) | Which locations should we label next? | Equal-budget learning curves, acquisition maps and sampling recommendation |

Each lesson includes objectives, concepts, runnable worked examples, an independent exercise, an expandable solution, a check-yourself prompt and a real-data extension. Predict outputs before running. Try the exercise before reading its solution. Record your own results and limitations.

## Finish the series

Use the [learner workbook](docs/WORKBOOK.md), [capstone brief and rubric](docs/CAPSTONE.md), and [instructor guide](docs/INSTRUCTOR.md). [Concept glossary](docs/GLOSSARY.md) and [source references](docs/REFERENCES.md) support review.

Generated practice products live in `data/generated/`; real observations stay in `data/real/`. Notebook code displays the core methods; `course.py` contains small shared fixtures and evaluation helpers worth reading.

## Verify your environment

```powershell
python -m unittest discover -s tests -v
python scripts/validate_course.py --kernel geospatial-course
```

Install the lessons 8.3–8.4 PyTorch dependency before running the complete course runner. The runner executes notebooks in their own directories and writes executed copies to ignored `runs/`. External labs remain disabled by default and are reported separately. See [change-detection validation notes](docs/CHANGE_DETECTION_VALIDATION.md) for the checks performed for lesson 6.1. Dependency ranges constrain major API changes; they are not a fully locked cross-platform environment. Save `python -m pip freeze` with your capstone.
