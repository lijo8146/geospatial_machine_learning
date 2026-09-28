# Capstone: Front Range Fire & Water Explorer

**Question:** What can your data and representation support, and where do they fail? Choose land-cover comparison, post-fire landscape description, or snow/water imagery retrieval. Avoid causal or hazard claims unsupported by the design.

Submit a reproducible notebook plus a 2-4 page learning report. Choose **practice** or **real-data** and state it on the first page. A practice submission uses synthetic examples and explains methods; it cannot claim to evaluate AlphaEarth, TESSERA or RemoteCLIP performance.

Required evidence:

1. Study question, spatial/temporal extent, data manifest, class definitions and provenance.
2. CRS round-trip/overlay checks and one exact spatial query with unmatched/boundary behavior explained.
3. Raster metadata, band order, pixel support and tensor dimensions; identify whether weights were pretrained or random.
4. Shared-cohort representation comparison with independent labels, spatial splits, baseline, confusion matrices and excluded samples. Practice submissions compare only simulated vectors.
5. Two H3 resolutions, sample counts, an interactive map and a full-point aggregation; explain the effect of scale.
6. Three retrieval queries plus one absent-content query. Real-data submissions show top-5 tiles and manual relevance judgments. Report precision@5 as relevant results/5 (or precision@k if fewer than five candidates), not model confidence.
7. Environment/package versions, random seeds, run instructions, limits, and one proposed follow-up experiment.

| Criterion | Points | Full-credit evidence |
|---|---:|---|
| Spatial correctness | 20 | CRS, units, resolution, exact predicates and boundary policy are justified |
| Evaluation design | 25 | Independent labels, no overlapping groups, baseline and fair cohort |
| Reproducibility | 20 | Provenance, environment and restart-and-run execution |
| Interpretation | 20 | Synthetic/real distinction, uncertainty, failure analysis and restrained claims |
| Communication | 15 | Readable maps, count/scale legends and clear explanation |

Mastery target: 80/100 with no unsupported real-world conclusions and no train/test spatial overlap. Before sharing, ask another learner to reproduce one result from a fresh kernel. End the report with what you learned, what remains unknown and the next observation needed to resolve it.
