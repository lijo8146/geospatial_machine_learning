# Instructor guide

For a Director-facing introduction, use [the teaching showcase](FOR_EDUCATORS.md). Each lesson should end with an independent decision and observable evidence of learning.

Suggested schedule: six two-hour meetings plus independent exercises and a capstone session. Pair learners so one predicts while the other runs; switch roles each example. Install and execute the default path before class. Provision real-data accounts/checkpoints before scheduling external labs.

1. **Foundations:** ask learners to diagnose a deliberately mislabeled CRS. Use the hole and shared-edge examples to distinguish indexing from topology. Exit evidence: a correct round trip and exact-match explanation.
2. **Raster learning:** draw row/column -> map coordinate -> channel tensor on a board. Have learners predict channel errors before enabling the optional TorchGeo cell. Accept a mechanics-only completion when GPU/download access is unavailable, but do not describe it as pretrained inference.
3. **Representations:** ask what the held-out geography represents. Compare the two synthetic feature sets only as workflow practice. Emphasize independent labels, annual temporal support and a shared missing-data cohort.
4. **Communication:** assign different H3 and canvas resolutions to pairs. Compare maps with the same scale and explain sampling density. Do not conclude Datashader is faster from incomparable timings.
5. **Retrieval:** collect relevance criteria before viewing results. Include absent-content queries and ask why every ranking still has a winner.

6. **Change detection:** use lesson 6.1 to separate actual injected changes from cloud, seasonal and registration artifacts. Use its 10-point rubric; assess coverage accounting and interpretation rather than the best fixture score. See lesson 5.2 for a companion exercise checking whether retrieved evidence supports a generated claim.

Solutions are expandable markdown in each notebook. Ask learners to submit their attempt and explanation before opening them. The exercise cells intentionally remain learner workspaces; worked examples are complete.

Assess reasoning and reproducibility rather than attractive maps or high scores. A well-documented coverage failure can meet a learning objective; it cannot count as a completed real-model comparison. Offer a practice capstone for learners without accounts and label it as such. Use the same rubric, with scientific claims confined to synthetic demonstrations.


**Decision-tree option (lesson 7.1, 75–90 minutes):** suitable before embeddings. Ask learners to trace one row through the plotted tree before showing its prediction. Require validation-only complexity selection and an independent predictor/leaf-size experiment. Use the notebook’s 10-point rubric; distinguish interpretable splits from causal explanations.


**Simple ANN option (lesson 8.1, 75–90 minutes):** trace a forward pass before training. Separate the concepts of loss, gradient and parameter update. Ask students to change one factor and interpret validation curves; keep test data out of model selection. The NumPy implementation has only 33 trainable parameters and needs no GPU.


**CNN option (lesson 8.2, 90 minutes):** begin with equal-brightness patterns and ask what the mean cannot reveal. Work one convolution by hand; inspect trained feature maps and compare original versus shuffled inputs. Assess scene-group separation and describe shuffling as a perturbation diagnostic, not a new labeled test benchmark.


**LSTM option (lesson 8.3, 90–120 minutes):** install CPU PyTorch before class. Draw a past-only input window and its next-step target; audit raw timestamp separation before training. Assess gates, baseline comparisons and the difference between rolling observed-history evaluation and multi-step forecasting. A simpler model winning is a valid learning outcome.


**Attention option (lesson 8.4, 90–120 minutes):** calculate three-token attention before showing the learned heatmap. Contrast permutation-invariant pooling without positions with a positional model. Assess chronological integrity and baseline interpretation; attention weights are mixing coefficients, not causal attributions.


**Active-learning option (lesson 9.1, 90–120 minutes):** ask learners to allocate a 50-label budget. Audit that acquisition never sees unqueried labels or test results. Compare five paired seeds and geographic coverage, then assess a justified sampling recommendation. Distinguish simulator-only error audits from information available to field sampling.
