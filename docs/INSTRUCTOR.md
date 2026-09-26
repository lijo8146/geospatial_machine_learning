# Instructor guide

Suggested schedule: five two-hour meetings plus independent exercises and a capstone session. Pair learners so one predicts while the other runs; switch roles each example. Install and execute the default path before class. Provision real-data accounts/checkpoints before scheduling external labs.

1. **Foundations:** ask learners to diagnose a deliberately mislabeled CRS. Use the hole and shared-edge examples to distinguish indexing from topology. Exit evidence: a correct round trip and exact-match explanation.
2. **Raster learning:** draw row/column → map coordinate → channel tensor on a board. Have learners predict channel errors before enabling the optional TorchGeo cell. Accept a mechanics-only completion when GPU/download access is unavailable, but do not describe it as pretrained inference.
3. **Representations:** ask what the held-out geography represents. Compare the two synthetic feature sets only as workflow practice. Emphasize independent labels, annual temporal support and a shared missing-data cohort.
4. **Communication:** assign different H3 and canvas resolutions to pairs. Compare maps with the same scale and explain sampling density. Do not conclude Datashader is faster from incomparable timings.
5. **Retrieval:** collect relevance criteria before viewing results. Include absent-content queries and ask why every ranking still has a winner.

Solutions are expandable markdown in each notebook. Ask learners to submit their attempt and explanation before opening them. The exercise cells intentionally remain learner workspaces; worked examples are complete.

Assess reasoning and reproducibility rather than attractive maps or high scores. A well-documented coverage failure can meet a learning objective; it cannot count as a completed real-model comparison. Offer a practice capstone for learners without accounts and label it as such. Use the same rubric, with scientific claims confined to synthetic demonstrations.
