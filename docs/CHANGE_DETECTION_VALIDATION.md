# Lesson 6.1 validation

Validated on 2026-09-28 on Windows using the existing `tribal-water` Python environment, with its Conda DLL directory available on PATH. No package changes were made.

- Notebook format validation passed.
- All default cells executed in a fresh Jupyter kernel from the lesson directory.
- Assertions checked grid-offset rejection, undefined NDVI masking, exclusion of invalid pixels, fixed evaluation cohorts, detected injected change and apparent change from displacement.
- The generated six-panel figure was visually reviewed; the educator overview includes a copy.
- Observed fixture results: 19,200 pixels; 90.2% observable coverage; 1,395 naive flags on excluded cloud pixels; 80 injected-change pixels obscured by cloud; 190 apparent changes from a one-pixel displacement. These are synthetic mechanics checks, not real-scene performance estimates.
- The existing four-test course suite was attempted: three passed; the H3 test could not run because `h3` is absent from this validation environment. It remains listed in the course requirements. This is not a passing full-suite result.

No real satellite imagery, model inference or classroom learning outcomes were validated. The complete eleven-notebook course runner was not run for this addition. The repository's intended environment is installed from `requirements.txt`; activate it before running the standard checks in the README.
