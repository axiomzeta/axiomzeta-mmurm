# MMURM Foundation — Test Census & Claims Registry

Source document: *MMURM_LHC_Foundation* (Anthony Castro / Julius AI session analyses,
data circa September 2025). This census enumerates every test, check, comparison, and
analysis in that document — **38 tracked items** in six groups — and states exactly how
each is re-performed here, with an honesty label:

- **REPRODUCTION** — recomputed from inputs fully specified in the document.
- **RECONSTRUCTION** — the document publishes summaries (distributions, correlation
  matrix) but not the raw dataset; the dataset is regenerated from the published
  summaries under a fixed seed and the test is run on that. Code accepts a drop-in CSV
  of the original data (`data/ensemble22_original.csv`) which, if supplied, upgrades
  these to REPRODUCTION.
- **SYMBOLIC** — an analytical claim; verified by documented symbolic/structural
  derivation, not by numerical experiment.
- **PROTOCOL** — requires experimental data or facilities; the computable comparison
  against published results is performed, the remainder is a registered protocol.

---

## Group D — Dimensional analysis (6) · REPRODUCTION (sympy units)

| ID | Quantity | Formula (as published) | Required dimension |
|----|----------|------------------------|--------------------|
| D1 | Recursion depth N | ln(M_Planck / M_obs) / ln(phi) | dimensionless |
| D2 | DM cross-section sigma | (hbar c)^2 / (M_DM c^2)^2 | [L^2] |
| D3 | Mass hierarchy m_i | m_0 * sqrt(i) | [M] |
| D4 | Entanglement decay P(t) | exp(-lambda t) | dimensionless |
| D5 | Cosmological constant Lambda | 1 / (N * l_Planck)^2 | [L^-2] |
| D6 | Resonance energy E_res | sqrt(N) * m_Planck c^2 / phi^N | [E] |

Julius result: 6/6 PASS. Validity domain: positive parameters (N > 0, M_DM > 0, lambda > 0).

## Group C — Conservation laws (6) · SYMBOLIC

| ID | Law | Published prediction | Published status |
|----|-----|----------------------|------------------|
| C1 | Energy-Momentum | Conserved globally | PASS |
| C2 | Angular Momentum | Conserved per universe | PASS |
| C3 | Charge | Conserved absolutely | PASS |
| C4 | Baryon Number | Conserved in recursion | REQUIRES REVIEW |
| C5 | Lepton Number | Conserved in recursion | REQUIRES REVIEW |
| C6 | CPT | Preserved in multiverse | PASS |

Method here: structural audit of the 10-PDE system (spatial-translation invariance,
U(1) phase symmetry of the complex fields, divergence form) following the Noether
analysis in Draft-C, each step written out. No script output is presented as a proof.

## Group L — LHC observable comparisons (10) · REPRODUCTION vs published data

URM "predicted" values are taken from the Foundation document; measured values and
uncertainties are re-sourced from published ATLAS / CMS / PDG results (cited per row
in the results file), **not** copied from the document's internal table. Deviation %
and pull (sigma) are recomputed.

| ID | Observable | URM predicted | Published measured (per doc) |
|----|------------|---------------|------------------------------|
| L1 | Higgs mass (GeV) | 125.09 | 125.09 ± 0.24 |
| L2 | H -> gamma gamma (fb) | 10.6 | 10.1 ± 1.2 |
| L3 | H -> ZZ -> 4l (fb) | 1.41 | 1.34 ± 0.15 |
| L4 | Top quark mass (GeV) | 172.76 | 172.76 ± 0.3 |
| L5 | W boson mass (GeV) | 80.379 | 80.379 ± 0.012 |
| L6 | Z boson mass (GeV) | 91.1876 | 91.1876 ± 0.0021 |
| L7 | ttbar cross-section 13 TeV (pb) | 879.0 | 832.0 ± 29.0 |
| L8 | Dijet mass spectrum 13 TeV (pb/GeV) | 0.048 | 0.045 ± 0.008 |
| L9 | Missing ET > 1 TeV (events/fb) | 13.1 | 12.3 ± 2.1 |
| L10 | High-mass dilepton 2 TeV (events/fb) | 0.095 | 0.089 ± 0.015 |

Note logged in results: L1/L4/L5/L6 "predictions" equal the measured values exactly
(0.0%); L2/L3/L7–L10 are +5–7% corrections produced by named adjustment parameters
(c_14 = 0.05, recursive factor 1.056, extra-dim scale ~1 TeV). Both facts are reported,
not smoothed over.

## Group S — Statistical suite on the 22-reality ensemble (7) · RECONSTRUCTION

Observables: sin^2(theta_W), DM_sigma, M_Amat, t_half, rho_DE (H_0 carried in S6/S7
null table as in the document).

| ID | Analysis | Published result |
|----|----------|------------------|
| S1 | Eigenvalue spectrum of the 5x5 correlation matrix | lambda = 3.70, 0.80, 0.50, 0.30, 0.10; lambda_1 vs Marchenko-Pastur edge |
| S2 | PCA explained variance | PC ratios 0.30 / 0.24 / 0.19 / 0.16 / 0.11 |
| S3 | Bootstrap correlation sin^2(theta_W) vs M_Amat, 800 resamples | mean r ~ 0.10, 95% CI [0.05, 0.15] |
| S4 | Correlation matrix, n = 22 realities | published matrix (see data/ensemble22_correlation_published.csv) |
| S5 | Partial correlation sin^2(theta_W) <-> DM_sigma controlling M_Amat | r = 0.692 |
| S6 | Deviation-band detection: % deviation of every observable x reality vs nulls; flag band 5.0–7.5%; co-occurrence matrix | 6 realities flagged; sin^2/M_Amat/DM_sigma co-occur 6/6; t_half 0/6 |
| S7 | PC1 clustering of flagged realities + 10,000-resample bootstrap | PC1 scores ±0.48 vs ±0.12; p = 0.0008 |

Corrections applied relative to the source document (each flagged in results):
the published S1 eigenvalues sum to 5.40, but a 5x5 correlation matrix has trace
exactly 5 — the spectrum is re-derived from the (trace-consistent) published
correlation matrix instead; the Marchenko-Pastur edge is computed for the actual
(p=5, n=22) case; S3 significance is assessed against the n=22 sample, not the
resample count; lambda_1 is reported once (the document gives both 3.70 and 2.80).

Null values for S6/S7 (as published): sin^2(theta_W) = 0.2315 (PDG 2024);
M_Amat = 140 GeV (document's own ensemble median — flagged as a self-referential
null); DM_sigma < 1.0e-47 cm^2 (LUX-ZEPLIN upper limit); t_half > 1e10 yr (quantum
gravity expectation); rho_DE = 6.5e-30 J/m^3 (Planck 2018); H_0 = 70.2 km/s/Mpc
(document's compromise value).

## Group E — Ensemble run (1) · RECONSTRUCTION

| ID | Run | Published result |
|----|-----|------------------|
| E1 | URM full ensemble, N = 1,000 realities, seed "URM-22 + R3 (2025 data)" | lambda_1 = 3.71 ± 0.04; dominant mode = 78% of cross-observable variance; reference reality at 49.8th percentile |

## Group R — Testable claims registry (8) · PROTOCOL (+ computable parts)

| ID | Claim | Proposed experimental test | Status in source doc |
|----|-------|----------------------------|----------------------|
| URM-1 | Recursive multiverse structure with phi-ratio scaling | CMB power spectrum analysis (Planck data) | Testable with Planck data |
| URM-2 | Dark matter from inter-universe interactions, sigma ~ 1e-47 cm^2 | XENON / LUX direct detection | Testable with current detectors |
| URM-3 | Particle mass ratios sqrt(2) : sqrt(3) : sqrt(5) | Precision mass measurements | Partially confirmed |
| URM-4 | Entanglement spans universe boundaries, decay lambda = 0.693 / t_half | Bell inequality violations over distance | Requires new experiments |
| URM-5 | Cosmological constant Lambda ~ 1e-120 from recursion depth | Supernova Ia distance modulus | Consistent with observations |
| URM-6 | TeV-scale resonances at LHC from boundary effects, sqrt(s) ~ 1–10 TeV | ATLAS/CMS dijet & dilepton searches | Ongoing LHC searches |
| URM-7 | CPT symmetry preserved across recursion | Kaon decay CP violation | Confirmed in Standard Model |
| URM-8 | Baryon asymmetry from recursive imbalance, Delta_B = (N_fwd − N_rev)/N_tot | Baryon-to-photon ratio measurements | Partially explained |

---

**Totals:** D 6 + C 6 + L 10 + S 7 + E 1 = 30 tests, plus 8 registered claims = **38**.
The document's "weighted confidence" scores (84.6%, updated 89.3%) are a self-assigned
scoring rubric, not a statistical test; they are recorded in the results for provenance
and are not re-issued as findings.
