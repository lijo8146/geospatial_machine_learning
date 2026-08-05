# data/

Local scratch space for pulled imagery, embeddings, and labeled point sets.
Everything here except this file is gitignored raw pulls and large rasters
shouldn't go into version control.

If you want to share a specific labeled dataset (ex. your hand-labeled
burned/unburned points), commit it explicitly with `git add -f`, or move
small CSVs into a `labels/` subfolder and un-ignore that path in
`.gitignore`.
