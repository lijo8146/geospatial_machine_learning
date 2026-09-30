# Active learning

[9.1 Which locations should we label next?](01_active_learning.ipynb)

A synthetic pool-based comparison of random and uncertainty sampling under a 50-label total budget. Includes a budgeted annotation oracle, five paired seeds, fixed buffered geographic holdout, coverage maps, hidden-truth audit, independent experiment and 10-point rubric. Base dependencies only; allow 90–120 minutes.

Validation (2026-09-28): all cells executed in a fresh kernel. Entropy, oracle rejection, paired starts, unique acquisitions, 50-label totals and geographic exclusion checks passed. Curves and maps were visually reviewed; course navigation links passed. Across five paired seeds at 50 labels, mean balanced accuracy was 0.822 for random sampling and 0.851 for uncertainty sampling on one synthetic eastern holdout. Seed ranges are descriptive, not confidence intervals. The initial-model audit found nine confidently wrong unqueried candidates. No real-data or full-course validation was performed.
