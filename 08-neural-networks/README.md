# Simple artificial neural network

[8.1 How does a small ANN learn?](01_simple_ann.ipynb)

A NumPy implementation of a 2 → 8 → 1 network with forward propagation, stable binary cross-entropy, backpropagation and gradient descent. Includes training-only scaling, validation checkpoint selection, held-out evaluation, visual learning curves and boundaries, an independent experiment and a 10-point rubric. Synthetic data only; no downloads or extra dependencies. Allow 75–90 minutes.

Validation (2026-09-28): all default cells executed in a fresh kernel; numerical gradient checks passed for both weight matrices and both bias arrays; local navigation links passed; learning-curve and boundary figures were visually reviewed. Synthetic held-out balanced accuracy was 0.887 for the ANN and 0.500 for both baselines. These results illustrate the intentionally nonlinear fixture, not general model superiority. No full-course rerun or real-data validation was performed.


## Convolutional neural network

[8.2 What can a CNN learn from pixel arrangement?](02_simple_cnn.ipynb)

A fully trainable NumPy CNN with six shared convolution kernels, ReLU, global average pooling and a three-class output. Includes hand convolution, grouped synthetic scenes, a mean-pixel baseline, shuffle diagnostic, learned feature maps and a 10-point rubric. No additional dependencies. Allow 90 minutes.

CNN validation (2026-09-28): all seven code cells executed in a fresh kernel. Shape, numerical-gradient, scene-separation, learned-filter and pixel-permutation checks passed. Feature-map and loss figures were visually reviewed. Balanced accuracy was 1.000 on the deliberately simple original synthetic test scenes and 0.333 for the mean baseline; agreement with original labels after shuffling was 0.333. The shuffle result is a perturbation diagnostic, not an independent labeled benchmark. No real imagery or full-course rerun was evaluated.


## Long short-term memory network

[8.3 Does remembering a sequence improve the next prediction?](03_simple_lstm.ipynb)

A small CPU PyTorch LSTM with a scalar gate demonstration, strictly separated chronological windows, training-only scaling, validation checkpoint selection and persistence/lagged-ridge baselines. Includes a random-walk counterexample, an independent experiment and a 10-point rubric. Allow 90–120 minutes. Unlike the ANN/CNN lessons, this requires PyTorch; follow the notebook setup or install `requirements-lstm.txt`.

LSTM validation (2026-09-28): all cells executed in a fresh CPU kernel using PyTorch 2.14.0+cpu installed only in the task scratch directory. Tensor shape, parameter count, chronological window, split disjointness, finite prediction and persistence-alignment checks passed. Forecast and learning-curve figures were visually reviewed. Test RMSE in arbitrary synthetic units: persistence 0.136, lagged ridge 0.116, LSTM 0.120. The simpler ridge model outperformed the LSTM on this fixture; this is an intended opportunity to discuss model complexity. No real-data or full-course validation was performed.


## Attention and a small Transformer-style block

[8.4 Which earlier observations does attention combine?](04_simple_attention.ipynb)

A worked Q/K/V calculation, one-head PyTorch encoder-style block, positional ablation and matched persistence/ridge/LSTM comparisons. Includes an attention heatmap, order-invariance check, independent exercise and rubric. Uses exactly the LSTM fixture/protocol without requiring its saved outputs. Same PyTorch dependency; allow 90–120 minutes.

Attention validation (2026-09-28): complete fresh-kernel execution passed using PyTorch 2.14.0+cpu. Checks covered hand attention, normalized nonnegative weights, tensor shapes, disjoint past-only windows, persistence alignment and reversal invariance without positions. Heatmap and forecast plots were visually reviewed; local links passed. Test RMSE: persistence 0.136, ridge 0.116, LSTM 0.120, positional attention 0.110. These are one synthetic run, not general model rankings. No-position attention was evaluated as a validation-only ablation. No real-data or full-course validation was performed.
