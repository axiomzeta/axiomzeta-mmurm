# MMURM — Multi-Modal Unified Recursive Multiverse

*From Interplayed Field Theory to Perennial Allness.*

Cleaned manuscript plus a 38-test reproducibility suite (dimensional, conservation, LHC, ensemble statistics) with published-vs-recomputed results, data, figures, and a claims registry for open assessment.

**Author:** Anthony Rene Castro (Axiom Zeta Innovations LLC)
**Status:** Working manuscript and independent re-analysis. Claims are labeled throughout as **[simulated]**, **[asserted]**, **[externally checkable]**, or **[postulated]**. Nothing in this repository is presented as established physics; it is presented so that anyone can check the mathematics and the numbers for themselves.

## Contents

| Path | What it is |
|------|------------|
| `paper/MMURM_clean.md` | The cleaned, deduplicated manuscript: IFT (10 coupled PDEs on a genus-12 manifold) → Unified Scale Theory → URM/MMURM → APQS roadmap → Constrained Trajectory Topology. All conflicts found in the source draft are resolved in **Appendix R** (R1–R14), in the open. |
| `paper/Draft-C_original.pdf` | The source draft, unmodified, for provenance. |
| `tests/TEST_CENSUS.md` | The census of all **38 tests** (D1–D6, C1–C6, L1–L10, S1–S7, E1, URM-1–URM-8) with method and honesty label for each. |
| `tests/*.py` | The runnable suite (`dimensional.py`, `lhc_compare.py`, `stats_suite.py`, `ensemble.py`, `figures.py`, `run_all.py`). |
| `tests/Foundation_original.pdf` | The source test report (Anthony Castro / Julius AI analyses, data circa Sep 2025), unmodified. |
| `data/` | The published 5×5 correlation matrix, the reconstructed 22-reality ensemble (seed-fixed; see below), and the claims registry (`claims_registry.json`). |
| `results/RESULTS.md`, `results/results.json` | Every test: published result, recomputed result, verdict (**AGREES / DIFFERS / CANNOT AGREE**) with reasons. |
| `results/figures/` | Counterpart figures generated from the same pipeline as the numbers. |

## Run it

```bash
python3 -m venv .venv && .venv/bin/pip install numpy scipy sympy pandas matplotlib
.venv/bin/python tests/run_all.py
```

Fixed seed `20250922` throughout: a run reproduces `results/results.json` exactly.

## Honesty labels (important)

- **REPRODUCTION** — recomputed from inputs fully specified in the source document (Groups D and L).
- **RECONSTRUCTION** — the source document publishes summaries (distributions, the correlation matrix) but not its raw 22×5 dataset, so the ensemble was regenerated from those summaries (Group S, E1). If the original dataset is supplied as `data/ensemble22_original.csv`, the suite uses it automatically and those groups upgrade to REPRODUCTION.
- **SYMBOLIC** — analytical claims verified by documented derivation, not numerical experiment (Group C).
- **PROTOCOL** — claims whose decisive test needs experimental facilities or datasets (URM-1–URM-8); the computable comparisons against published results are performed, the rest is a registered protocol.

## Headline findings of the re-analysis

- Dimensional analysis reproduces **6/6 PASS**; the LHC comparison table's arithmetic reproduces on all 10 rows; the partial correlation (0.694 vs 0.692 published) reproduces.
- The source report's eigenvalue spectrum is arithmetically impossible (sums to 5.40; a 5×5 correlation matrix's eigenvalues sum to exactly 5). Recomputed from the document's own matrix: 3.635 / 0.719 / 0.407 / 0.194 / 0.045.
- The published 5–7% deviation band is empty under the document's own ranges and nulls; the clustering result that presupposes it is recorded as CANNOT AGREE as stated.
- Four LHC "predictions" are the measured values copied exactly; several "measured" values are superseded (e.g., Higgs mass) or are Standard Model predictions rather than measurements. Each case is flagged per row in `results/RESULTS.md`.
- The 1,000-reality ensemble gives λ₁ = 3.659 (published 3.71 ± 0.04) on the reconstruction; the published "78% variance" belongs to a different object (the 12-layer modal decomposition), not the 5-observable ensemble.

## License

MIT — see `LICENSE`. The manuscript text and the test code are both covered; assess, reuse, and critique freely with attribution.
