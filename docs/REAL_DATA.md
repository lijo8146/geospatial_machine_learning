# Real-data laboratory guide

Complete the practice path first. Use public, non-sensitive data for this course; do not transfer the workflow to governed community data without the relevant community's process.

## 1. Build an observation manifest

Choose a small Front Range study area, a year shared by both embedding products (start with 2022 or 2024), and a question such as vegetation versus built land cover. Annual representations cannot isolate a late-December fire event. Avoid calling a land-cover classifier a fire-impact model.

Use public sources: [NRCS SNOTEL](https://www.nrcs.usda.gov/resources/data-and-reports/snow-and-water-interactive-map), [USGS Watershed Boundary Dataset](https://www.usgs.gov/national-hydrography/watershed-boundary-dataset), and [USGS EarthExplorer](https://earthexplorer.usgs.gov/) for imagery discovery. Download through the provider interface and retain original metadata. Service-specific account and download requirements vary.

For every file record URL/product ID, access date, acquisition date/year, license/attribution, original CRS, band order, units, nodata, processing and checksum. Use `Get-FileHash filename` or `sha256sum filename`. Inspect CRS and bounds before combining layers. Do not use fabricated station or watershed names for the practice fixtures.

## 2. Independently label points

Create `data/real/labels.csv` using the header in `data/labels.example.csv`. Collect at least 60–100 independently interpreted points across several spatial blocks, with each class represented in train and test regions. The example file intentionally contains no invented real labels.

Columns: `point_id` (unique string), `longitude`, `latitude` (WGS84), `label` (0/1, define in your report), `block` (spatial group assigned before modeling), `year`, `label_source` (imagery/date/evidence). Spatial blocks should exceed the relevant autocorrelation scale; explore more than one block size. Nearby or duplicate pixels should not span train and test. Keep ambiguous labels separate and report exclusions.

## 3. Install and acquire embeddings

```powershell
python -m pip install -r requirements-models.txt
earthengine authenticate
python scripts/fetch_embeddings.py alphaearth --labels data/real/labels.csv --year 2022 --project YOUR_REGISTERED_PROJECT
python scripts/fetch_embeddings.py tessera --labels data/real/labels.csv --year 2022
python scripts/compare_embeddings.py
```

AlphaEarth uses the official annual collection and 10 m point sampling. Small-label `getInfo()` is deliberate here; use Earth Engine table exports for large studies. Masked samples remain missing. TESSERA loads registered covering tiles and samples after transformation into each tile CRS; tile downloads may be large. Check coverage and available disk space first. Network/authentication errors are surfaced, not replaced by synthetic results.

The comparison joins by point ID, verifies label/location/year agreement, uses the common finite cohort and holds out spatial blocks. Review class balance, confusion matrices and baseline, not only accuracy. `data/real/*_predictions.csv` records train/test membership; all-point predictions include training points and are not all independent evaluation. Class-1 probabilities are classifier scores, not automatically calibrated uncertainty. For model selection, add a separate group-held-out validation partition and preserve the final test set.

## 4. TorchGeo lab

Run notebook 2.1 with `RUN_TORCHGEO=True`. The course targets TorchGeo 0.9 sampler APIs; the optional requirements cap it below 0.10. Enable `PRETRAINED=True` for the actual weight download. Inspect `weights.meta` and the bundled transform. The fixture is noise: a successful forward pass establishes shape compatibility only. For real inference replace it with RGB Sentinel-2 reflectance using the documented band order/scaling and a valid-pixel mask; do not infer classes from the feature extractor without a trained head.

## 5. RemoteCLIP lab

Use public aerial/satellite RGB images. Export small, consistent ground-footprint tiles as PNG into `data/real/tiles/`. PNG loses georeferencing: save a manifest with tile filename, WGS84 bounds, CRS of source, acquisition date, source ID and processing. Exclude cloud/nodata tiles; avoid overlapping tiles across evaluation subsets.

Download the matching checkpoint explicitly (hundreds of MB or more):

```powershell
python -c "from huggingface_hub import hf_hub_download; hf_hub_download(repo_id='chendelong/RemoteCLIP', filename='RemoteCLIP-ViT-B-32.pt', local_dir='data/models')"
```

Set `RUN_REMOTECLIP=True` in notebook 5.1. Keep architecture and checkpoint matched. The lab uses the model's image transform and tokenizer, batches image encodings and normalizes both modalities. Do not feed AlphaEarth/TESSERA vectors to this text encoder. Inspect top results and include a query whose content is absent. Save manual relevance judgments and calculate precision@k. No universal similarity cutoff distinguishes true from false content.

## Troubleshooting

- Missing modules: confirm the notebook kernel uses the interpreter where packages were installed.
- Earth Engine project/auth errors: authenticate your account and enable/register the Cloud project; no credentials belong in Git.
- No coverage or all-missing vectors: check year, coordinate order, raster bounds and product masks; report the gap.
- Single-class split: gather additional geographically distributed labels; do not repeatedly choose splits until a score looks good.
- Blank map: open the generated HTML in a browser with JavaScript/network access. No basemap is configured by default.
- CUDA memory: use CPU or reduce the batch size. Optional labs may take substantially longer than the practice lessons.
