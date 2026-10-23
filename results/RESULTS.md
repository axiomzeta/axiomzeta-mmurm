# MMURM Foundation — Re-performance Results

Independent re-run of the 38 tracked items in `tests/TEST_CENSUS.md` (source: *MMURM_LHC_Foundation*, Anthony Castro / Julius AI, data circa Sep 2025). Generated 2026-10-23.

**Honesty labels.** REPRODUCTION = recomputed from inputs fully specified in the document. RECONSTRUCTION = the document publishes summaries (distributions, correlation matrix) but not the raw dataset; the dataset was regenerated from those summaries under fixed seed 20250922 and the tests run on that. If the original dataset is dropped in at `data/ensemble22_original.csv`, the S/E groups upgrade to REPRODUCTION automatically. SYMBOLIC / PROTOCOL items are recorded, not re-run.

**Provenance.** The source document's 'weighted confidence' scores (84.6% → 89.3%) are a self-assigned rubric, not a statistical test; they are recorded here and are **not** re-issued as findings.

## Verdict summary

| ID | Test | Verdict |
|----|------|---------|
| D1 | Recursion depth N | AGREES |
| D2 | DM cross-section sigma | AGREES |
| D3 | Mass hierarchy m_i | AGREES |
| D4 | Entanglement decay P(t) | AGREES |
| D5 | Cosmological constant Lambda | AGREES |
| D6 | Resonance energy E_res | AGREES |
| C1 | Energy-Momentum conservation | RECORDED (not re-run) |
| C2 | Angular Momentum conservation | RECORDED (not re-run) |
| C3 | Charge conservation | RECORDED (not re-run) |
| C4 | Baryon Number conservation | RECORDED (not re-run) |
| C5 | Lepton Number conservation | RECORDED (not re-run) |
| C6 | CPT symmetry | RECORDED (not re-run) |
| L1 | Higgs mass (GeV) | AGREES |
| L2 | H -> gamma gamma (fb) | AGREES |
| L3 | H -> ZZ -> 4l (fb) | AGREES |
| L4 | Top quark mass (GeV) | AGREES |
| L5 | W boson mass (GeV) | AGREES |
| L6 | Z boson mass (GeV) | AGREES |
| L7 | ttbar cross-section 13 TeV (pb) | AGREES |
| L8 | Dijet mass spectrum 13 TeV (pb/GeV) | AGREES |
| L9 | Missing ET > 1 TeV (events/fb) | AGREES |
| L10 | High-mass dilepton 2 TeV (events/fb) | AGREES |
| S1 | Eigenvalue spectrum of the 5x5 correlation matrix | DIFFERS |
| S2 | PCA explained variance | DIFFERS |
| S3 | Bootstrap correlation sin^2(theta_W) vs M_Amat, 800 resamples | DIFFERS |
| S4 | Correlation matrix, n = 22 realities | AGREES |
| S5 | Partial correlation sin^2(theta_W) <-> DM_sigma controlling M_Amat | AGREES |
| S6 | Deviation-band detection (5.0-7.5%) vs nulls, co-occurrence | DIFFERS |
| S7 | PC1 clustering of flagged realities + 10,000-resample bootstrap | CANNOT AGREE |
| E1 | URM full ensemble, N = 1,000 realities | DIFFERS |

Group R (URM-1..URM-8) is a PROTOCOL registry — see `data/claims_registry.json`; statuses are as published, not re-tested.

## Group D — Dimensional analysis (REPRODUCTION)

### D1 — Recursion depth N

- **Label:** REPRODUCTION
- **Published:** PASS (Julius: 6/6 PASS)
- **Recomputed:** PASS
- **Verdict: AGREES**
- Notes: Dimensional consistency is necessary, not sufficient: passing shows the formula is unit-coherent, not that it is correct.

### D2 — DM cross-section sigma

- **Label:** REPRODUCTION
- **Published:** PASS (Julius: 6/6 PASS)
- **Recomputed:** PASS
- **Verdict: AGREES**
- Notes: Dimensional consistency is necessary, not sufficient: passing shows the formula is unit-coherent, not that it is correct.

### D3 — Mass hierarchy m_i

- **Label:** REPRODUCTION
- **Published:** PASS (Julius: 6/6 PASS)
- **Recomputed:** PASS
- **Verdict: AGREES**
- Notes: Dimensional consistency is necessary, not sufficient: passing shows the formula is unit-coherent, not that it is correct.

### D4 — Entanglement decay P(t)

- **Label:** REPRODUCTION
- **Published:** PASS (Julius: 6/6 PASS)
- **Recomputed:** PASS
- **Verdict: AGREES**
- Notes: Dimensional consistency is necessary, not sufficient: passing shows the formula is unit-coherent, not that it is correct.

### D5 — Cosmological constant Lambda

- **Label:** REPRODUCTION
- **Published:** PASS (Julius: 6/6 PASS)
- **Recomputed:** PASS
- **Verdict: AGREES**
- Notes: Dimensional consistency is necessary, not sufficient: passing shows the formula is unit-coherent, not that it is correct.

### D6 — Resonance energy E_res

- **Label:** REPRODUCTION
- **Published:** PASS (Julius: 6/6 PASS)
- **Recomputed:** PASS
- **Verdict: AGREES**
- Notes: Dimensional consistency is necessary, not sufficient: passing shows the formula is unit-coherent, not that it is correct.

## Group C — Conservation laws (SYMBOLIC, recorded)

### C1 — Energy-Momentum conservation

- **Label:** SYMBOLIC
- **Published:** PASS (conserved globally)
- **Recomputed:** Not re-performed: structural/Noether audit item per TEST_CENSUS.md; no script output is presented as a proof.
- **Verdict: RECORDED (not re-run)**

### C2 — Angular Momentum conservation

- **Label:** SYMBOLIC
- **Published:** PASS (conserved per universe)
- **Recomputed:** Not re-performed: structural/Noether audit item per TEST_CENSUS.md; no script output is presented as a proof.
- **Verdict: RECORDED (not re-run)**

### C3 — Charge conservation

- **Label:** SYMBOLIC
- **Published:** PASS (conserved absolutely)
- **Recomputed:** Not re-performed: structural/Noether audit item per TEST_CENSUS.md; no script output is presented as a proof.
- **Verdict: RECORDED (not re-run)**

### C4 — Baryon Number conservation

- **Label:** SYMBOLIC
- **Published:** REQUIRES REVIEW (conserved in recursion)
- **Recomputed:** Not re-performed: structural/Noether audit item per TEST_CENSUS.md; no script output is presented as a proof.
- **Verdict: RECORDED (not re-run)**

### C5 — Lepton Number conservation

- **Label:** SYMBOLIC
- **Published:** REQUIRES REVIEW (conserved in recursion)
- **Recomputed:** Not re-performed: structural/Noether audit item per TEST_CENSUS.md; no script output is presented as a proof.
- **Verdict: RECORDED (not re-run)**

### C6 — CPT symmetry

- **Label:** SYMBOLIC
- **Published:** PASS (preserved in multiverse)
- **Recomputed:** Not re-performed: structural/Noether audit item per TEST_CENSUS.md; no script output is presented as a proof.
- **Verdict: RECORDED (not re-run)**

## Group L — LHC comparisons (REPRODUCTION)

The recomputed deviation % and pull reproduce the document's table exactly — the arithmetic is right. The flags are the substance: four 'predictions' are digit-for-digit copies of the measured values, and the other six are the measured values scaled by named adjustment knobs.

### L1 — Higgs mass (GeV)

- **Label:** REPRODUCTION
- **Published:** deviation 0.00%, pull 0.00 sigma (per source document table)
- **Recomputed:** None
- **Verdict: AGREES**
- Scope: The document's internal arithmetic (deviation % and pull) reproduces exactly. See flags: agreement of arithmetic is not validation of the 'prediction'.
- ⚠️ EXACT MATCH: the URM 'predicted' value is identical to the measured value to every quoted digit (deviation 0.0%). This is an identity, not a prediction: the value was taken from the measurement.
- ⚠️ PROVENANCE: Document's 'measured' 125.09 +/- 0.24 is the superseded 2015 ATLAS+CMS Run-1 combination, not the current PDG 2024 average.
- Spot check: PDG 2024 average m_H = 125.20 +/- 0.11 GeV → URM value deviates -0.088% (-1.0 sigma). Document's 'measured' 125.09 +/- 0.24 is the superseded 2015 ATLAS+CMS Run-1 combination, not the current PDG 2024 average.

### L2 — H -> gamma gamma (fb)

- **Label:** REPRODUCTION
- **Published:** deviation 4.95%, pull 0.42 sigma (per source document table)
- **Recomputed:** None
- **Verdict: AGREES**
- Scope: The document's internal arithmetic (deviation % and pull) reproduces exactly. See flags: agreement of arithmetic is not validation of the 'prediction'.
- ⚠️ KNOB-DRIVEN: the +5-7% correction is produced by a named adjustment parameter (Gravity-EM coupling c_14 = 0.05 ('5% Higgs enhancement')), applied to the measured value; it is not derived from the framework's equations.

### L3 — H -> ZZ -> 4l (fb)

- **Label:** REPRODUCTION
- **Published:** deviation 5.22%, pull 0.47 sigma (per source document table)
- **Recomputed:** None
- **Verdict: AGREES**
- Scope: The document's internal arithmetic (deviation % and pull) reproduces exactly. See flags: agreement of arithmetic is not validation of the 'prediction'.
- ⚠️ KNOB-DRIVEN: the +5-7% correction is produced by a named adjustment parameter (Gravity-EM coupling c_14 = 0.05 (same Higgs-sector mechanism as L2)), applied to the measured value; it is not derived from the framework's equations.

### L4 — Top quark mass (GeV)

- **Label:** REPRODUCTION
- **Published:** deviation 0.00%, pull 0.00 sigma (per source document table)
- **Recomputed:** None
- **Verdict: AGREES**
- Scope: The document's internal arithmetic (deviation % and pull) reproduces exactly. See flags: agreement of arithmetic is not validation of the 'prediction'.
- ⚠️ EXACT MATCH: the URM 'predicted' value is identical to the measured value to every quoted digit (deviation 0.0%). This is an identity, not a prediction: the value was taken from the measurement.

### L5 — W boson mass (GeV)

- **Label:** REPRODUCTION
- **Published:** deviation 0.00%, pull 0.00 sigma (per source document table)
- **Recomputed:** None
- **Verdict: AGREES**
- Scope: The document's internal arithmetic (deviation % and pull) reproduces exactly. See flags: agreement of arithmetic is not validation of the 'prediction'.
- ⚠️ EXACT MATCH: the URM 'predicted' value is identical to the measured value to every quoted digit (deviation 0.0%). This is an identity, not a prediction: the value was taken from the measurement.
- ⚠️ PROVENANCE: Document's 80.379 +/- 0.012 is an older average; the URM value equals the document's number exactly, not the current PDG value.
- Spot check: PDG 2024/2025 m_W = 80.3692 +/- 0.0133 GeV → URM value deviates 0.012% (0.737 sigma). Document's 80.379 +/- 0.012 is an older average; the URM value equals the document's number exactly, not the current PDG value.

### L6 — Z boson mass (GeV)

- **Label:** REPRODUCTION
- **Published:** deviation 0.00%, pull 0.00 sigma (per source document table)
- **Recomputed:** None
- **Verdict: AGREES**
- Scope: The document's internal arithmetic (deviation % and pull) reproduces exactly. See flags: agreement of arithmetic is not validation of the 'prediction'.
- ⚠️ EXACT MATCH: the URM 'predicted' value is identical to the measured value to every quoted digit (deviation 0.0%). This is an identity, not a prediction: the value was taken from the measurement.
- ⚠️ PROVENANCE: Document's 91.1876 +/- 0.0021 is the LEP-era value; close to, but not, the current PDG average.
- Spot check: PDG 2024/2025 m_Z = 91.1880 +/- 0.0020 GeV → URM value deviates -0.0% (-0.2 sigma). Document's 91.1876 +/- 0.0021 is the LEP-era value; close to, but not, the current PDG average.

### L7 — ttbar cross-section 13 TeV (pb)

- **Label:** REPRODUCTION
- **Published:** deviation 5.65%, pull 1.62 sigma (per source document table)
- **Recomputed:** None
- **Verdict: AGREES**
- Scope: The document's internal arithmetic (deviation % and pull) reproduces exactly. See flags: agreement of arithmetic is not validation of the 'prediction'.
- ⚠️ KNOB-DRIVEN: the +5-7% correction is produced by a named adjustment parameter (Recursive flux factor 1.056 (832.0 x 1.056 = 878.6 ~= 879)), applied to the measured value; it is not derived from the framework's equations.
- ⚠️ PROVENANCE: Document's 'measured' 832.0 +/- 29.0 pb coincides with the NNLO+NNLL Standard Model prediction (Top++), not with the ATLAS measurement it is attributed to.
- Spot check: ATLAS 13 TeV ttbar (36.1 fb^-1) = 826.4 pb, total unc ~ +/-20 pb → URM value deviates 6.365% (2.63 sigma). Document's 'measured' 832.0 +/- 29.0 pb coincides with the NNLO+NNLL Standard Model prediction (Top++), not with the ATLAS measurement it is attributed to.

### L8 — Dijet mass spectrum 13 TeV (pb/GeV)

- **Label:** REPRODUCTION
- **Published:** deviation 6.67%, pull 0.38 sigma (per source document table)
- **Recomputed:** None
- **Verdict: AGREES**
- Scope: The document's internal arithmetic (deviation % and pull) reproduces exactly. See flags: agreement of arithmetic is not validation of the 'prediction'.
- ⚠️ KNOB-DRIVEN: the +5-7% correction is produced by a named adjustment parameter (Higher-dimensional projections ('6-7% dijet/dilepton')), applied to the measured value; it is not derived from the framework's equations.

### L9 — Missing ET > 1 TeV (events/fb)

- **Label:** REPRODUCTION
- **Published:** deviation 6.50%, pull 0.38 sigma (per source document table)
- **Recomputed:** None
- **Verdict: AGREES**
- Scope: The document's internal arithmetic (deviation % and pull) reproduces exactly. See flags: agreement of arithmetic is not validation of the 'prediction'.
- ⚠️ KNOB-DRIVEN: the +5-7% correction is produced by a named adjustment parameter (Extra-dim energy loss ('6.5% missing ET'), extra-dim scale ~1 TeV), applied to the measured value; it is not derived from the framework's equations.

### L10 — High-mass dilepton 2 TeV (events/fb)

- **Label:** REPRODUCTION
- **Published:** deviation 6.74%, pull 0.40 sigma (per source document table)
- **Recomputed:** None
- **Verdict: AGREES**
- Scope: The document's internal arithmetic (deviation % and pull) reproduces exactly. See flags: agreement of arithmetic is not validation of the 'prediction'.
- ⚠️ KNOB-DRIVEN: the +5-7% correction is produced by a named adjustment parameter (Higher-dimensional projections ('6-7% dijet/dilepton')), applied to the measured value; it is not derived from the framework's equations.

## Group S — Statistical suite (RECONSTRUCTION)

### S1 — Eigenvalue spectrum of the 5x5 correlation matrix

- **Label:** REPRODUCTION (published matrix is fully specified)
- **Published:** - eigenvalues_julius: 3.7, 0.8, 0.5, 0.3, 0.1
- julius_eigenvalue_sum: 5.4
- marchenko_pastur_bound_as_printed: 1.97
- plot_threshold_line: 1.0
- **Recomputed:** - eigenvalues_of_published_matrix: 3.6351, 0.7192, 0.4069, 0.1939, 0.0449
- eigenvalue_sum: 5.0
- matrix_trace: 5.0
- min_eigenvalue: 0.0449
- marchenko_pastur_edge_p5_n22: 2.1807
- lambda_1_above_mp_edge: True
- lambda_1_variance_share: 0.727
- **Verdict: DIFFERS**
- ⚠️ TRACE VIOLATION: the published eigenvalues (3.70, 0.80, 0.50, 0.30, 0.10) sum to 5.40, but every 5x5 correlation matrix has trace exactly 5, so its eigenvalues must sum to 5. The published spectrum is not the spectrum of the published matrix, nor of any 5x5 correlation matrix.
- ⚠️ The document also prints lambda_1 = 2.80 in its cascade section ('2.80 (report) or 3.70 (plot)') while using 3.70 elsewhere; the recomputed value from its own matrix is 3.635 — neither printed number.
- ⚠️ The Marchenko-Pastur edge for the actual case (p=5, n=22) is 2.18, not the printed 1.97 (and not the plot's 1.0 line). lambda_1 does exceed the correct edge, so the qualitative 'one dominant mode' reading survives; the printed numbers do not.
- Notes: Eigenvalues recomputed from data/ensemble22_correlation_published.csv. The published matrix itself is a valid correlation matrix (min eigenvalue > 0).

### S2 — PCA explained variance

- **Label:** RECONSTRUCTION
- **Published:** - ratios: 0.3, 0.24, 0.19, 0.16, 0.11
- basis_as_printed: covariance ('PCA is on covariance, not correlation')
- **Recomputed:** - covariance_pca_ratios_reconstructed: 0.9998, 0.0002, 0.0, 0.0, 0.0
- correlation_pca_ratios_reconstructed: 0.615, 0.2069, 0.11, 0.0592, 0.0088
- dominant_covariance_component: t_half (largest raw variance)
- **Verdict: DIFFERS**
- ⚠️ In natural units the covariance PCA is dominated by t_half (values 800-1600 yr; variance orders of magnitude larger than the other observables), giving PC1 ~= 100% — the published 0.30/0.24/0.19/0.16/0.11 profile cannot arise from the documented distributions in natural units.
- ⚠️ The correlation PCA gives yet another profile (~eigenvalues/5 of the sample correlation matrix). Neither recomputation matches the published ratios; the source simulation's variable scaling is undocumented, so the published PCA cannot be reproduced or audited (CANNOT AGREE on method, DIFFERS on numbers).
- Notes: The document's own resolution ('after standardization -> correlation PCA -> PC1 dominates') contradicts its printed covariance ratios, which show PC1 at only 30%.

### S3 — Bootstrap correlation sin^2(theta_W) vs M_Amat, 800 resamples

- **Label:** RECONSTRUCTION
- **Published:** - mean_r: 0.1
- ci_95: 0.05, 0.15
- claimed: p < 0.001, 'highly significant due to large n=22 realities'
- **Recomputed:** - sample_correlation_reconstructed: 0.8896
- bootstrap_mean_r: 0.8901
- bootstrap_ci_95: 0.7641, 0.9582
- fisher_z_ci_95: 0.7488, 0.9535
- t_statistic_n22: 8.709
- p_value_n22: 3.0649902113241934e-08
- published_pair_correlation_in_matrix: 0.926
- claimed_r_0.10_at_n22:   - t: 0.449
  - p: 0.658
- **Verdict: DIFFERS**
- ⚠️ INTERNAL CONTRADICTION: the document's bootstrap centres on r ~= 0.10 for sin^2(theta_W) vs M_Amat, but its own published correlation matrix gives r = 0.926 for the same pair. A bootstrap of data with correlation 0.926 cannot centre on 0.10. The reconstruction (built on the published matrix) bootstraps around r ~= 0.89. One of the two published artefacts does not describe the ensemble.
- ⚠️ SIGNIFICANCE ERROR: at n = 22, r = 0.10 gives t = 0.45, p = 0.66 — nowhere near significant. 800 bootstrap resamples of 22 points do not create significance the sample does not contain; 'large n' is the resample count, not the sample size.
- Notes: Resampling 22 fixed points measures the stability of the estimate for THIS ensemble; it is not independent evidence about physics.

### S4 — Correlation matrix, n = 22 realities

- **Label:** RECONSTRUCTION
- **Published:** matrix as in data/ensemble22_correlation_published.csv
- **Recomputed:** - matrix_is_valid_correlation_matrix: True
- min_eigenvalue: 0.0449
- reconstruction_sample_corr_max_abs_dev_vs_published: 0.338
- **Verdict: AGREES**
- Scope: The published matrix is internally valid (symmetric, unit diagonal, positive definite) and is used verbatim as the reconstruction target. The n=22 reconstruction's sample correlations deviate by up to 0.34, which is ordinary sampling noise at n=22 — the matrix is a summary the document asserts, not a result this suite can confirm.
- Notes: Strong positive block sin2/DM/M_Amat (r = 0.80-0.93) and negative t_half couplings (r ~= -0.62..-0.70) are properties asserted by the document; no independent dataset exists to check them against.

### S5 — Partial correlation sin^2(theta_W) <-> DM_sigma controlling M_Amat

- **Label:** REPRODUCTION (from published matrix) + RECONSTRUCTION (from data)
- **Published:** 0.692
- **Recomputed:** - from_published_matrix_formula: 0.694
- from_reconstructed_data: 0.7045
- **Verdict: AGREES**
- Notes: The one ensemble statistic that reproduces cleanly: (0.898 - 0.926*0.800) / sqrt((1-0.926^2)(1-0.800^2)) = 0.694 vs published 0.692 (rounding). Agreement is with the document's own matrix arithmetic; it does not validate the matrix itself.

### S6 — Deviation-band detection (5.0-7.5%) vs nulls, co-occurrence

- **Label:** RECONSTRUCTION
- **Published:** - flagged_realities: 6
- cooccurrence: sin2/M_Amat/DM_sigma 6/6; H_0 5/6; t_half 0/6
- fraction_with_ge3_hits: 27%
- **Recomputed:** - band_hits_per_observable:   - sin2_thetaW: 0
  - DM_sigma: 0
  - M_Amat: 0
  - t_half: 0
  - rho_DE: 0
- realities_with_ge1_hit: 0
- realities_with_ge3_hits: 0
- cooccurrence_among_ge3_flagged: none (no flagged realities)
- max_abs_deviation_pct_per_observable:   - sin2_thetaW: 2.46
  - DM_sigma: 231.455
  - M_Amat: 2.556
  - t_half: 100.0
  - rho_DE: 3.844
- arithmetic_caps_from_published_ranges:   - sin2_thetaW_max_possible_deviation_pct: 2.81
  - M_Amat_max_possible_deviation_pct: 2.86
- **Verdict: DIFFERS**
- ⚠️ ARITHMETICALLY IMPOSSIBLE AS PUBLISHED: the document's own ranges cap sin^2(theta_W) deviations at 2.8% (values 0.231-0.238 vs null 0.2315) and M_Amat at 2.9% (136-144 vs null 140) — both below the 5% band floor. No dataset consistent with the published distributions can put either observable in the 5-7.5% band, yet the document reports 6/6 co-occurrence for both.
- ⚠️ DM_sigma: the published distribution (peaks 1.5/2.5/3.0) vs the LUX-ZEPLIN upper-limit 'null' of 1.0 gives deviations of +50% to +200% — above the band, not in it.
- ⚠️ t_half 0/6 'agrees' only trivially: model values sit ~7 orders of magnitude below the >1e10 yr null (deviation ~-100%), not just outside a 5-7.5% band as a 'threshold effect'.
- ⚠️ H_0 cannot be checked at all: it is not in the ensemble and has no published per-reality values.
- Notes: Run on the RECONSTRUCTION, but the caps above are pure arithmetic on the document's published ranges and nulls — they hold for ANY dataset matching those summaries, including the original one.

### S7 — PC1 clustering of flagged realities + 10,000-resample bootstrap

- **Label:** RECONSTRUCTION
- **Published:** - flagged_mean_abs_pc1: 0.48
- others_mean_abs_pc1: 0.12
- p_value: 0.0008
- bootstrap: 99.92% rejection
- **Recomputed:** - status: NOT PERFORMABLE: under the published >=3-hit flag definition, zero realities are flagged in any dataset consistent with the published distributions and nulls (see S6), so there is no flagged group to cluster.
- published_definition_ge3_hits: None
- sensitivity_ge1_hit_definition_NOT_published: None
- n_flagged_ge3: 0
- n_flagged_ge1: 0
- **Verdict: CANNOT AGREE**
- ⚠️ The published p = 0.0008 clustering result presupposes 6 flagged realities whose band membership is arithmetically impossible under the document's own published ranges and nulls (S6). The clustering machinery is implemented here exactly as described (PC1 of the published correlation matrix; label-permutation bootstrap, 10,000 resamples) and runs the moment a dataset with flagged realities is supplied — on every dataset consistent with the published summaries, there is nothing to run it on.
- Notes: PC1 scores use the published matrix's dominant eigenvector applied to the standardised reconstruction.

## Group E — Ensemble run (RECONSTRUCTION)

### E1 — URM full ensemble, N = 1,000 realities

- **Label:** RECONSTRUCTION
- **Published:** lambda_1 = 3.71 +/- 0.04; dominant mode = 78% of cross-observable variance; reference reality at 49.8th percentile (seed 'URM-22 + R3 (2025 data)')
- **Recomputed:** - lambda_1_correlation_matrix: 3.6585
- eigenvalues: 3.6585, 0.6926, 0.4112, 0.1876, 0.0501
- dominant_mode_variance_share: 0.7317
- reference_reality_index: R618
- reference_reality_pc1_percentile: 20.1
- reference_vector:   - sin2_thetaW: 0.2315
  - DM_sigma: 2.5
  - M_Amat: 140.0
  - rho_DE: 6.5
- t_half_excluded_from_distance_because: model t_half = 800-1600 yr vs the only published reference >1e10 yr (quantum-gravity expectation): no measured t_half exists to locate a reality by, and including it would make the distance a pure t_half mismatch counter
- **Verdict: DIFFERS**
- Notes: Ensemble is a RECONSTRUCTION (same copula as the 22-reality set, seed 20250922); the document's seed string 'URM-22 + R3' is not a reproducible seed. Differences: lambda_1 = 3.658, outside the published 3.71 +/- 0.04; dominant-mode variance share = 73.2%, not 78% (note: even the published lambda_1 = 3.71 gives 3.71/5 = 74.2%, not 78%; the 78% figure matches the separate 12-layer modal decomposition in Draft-C, not this 5-observable correlation matrix); reference-reality PC1 percentile = 20.1, not 49.8

## Contradictions & flags (unsoftened)

- L1: EXACT MATCH: the URM 'predicted' value is identical to the measured value to every quoted digit (deviation 0.0%). This is an identity, not a prediction: the value was taken from the measurement.
- L1: PROVENANCE: Document's 'measured' 125.09 +/- 0.24 is the superseded 2015 ATLAS+CMS Run-1 combination, not the current PDG 2024 average.
- L2: KNOB-DRIVEN: the +5-7% correction is produced by a named adjustment parameter (Gravity-EM coupling c_14 = 0.05 ('5% Higgs enhancement')), applied to the measured value; it is not derived from the framework's equations.
- L3: KNOB-DRIVEN: the +5-7% correction is produced by a named adjustment parameter (Gravity-EM coupling c_14 = 0.05 (same Higgs-sector mechanism as L2)), applied to the measured value; it is not derived from the framework's equations.
- L4: EXACT MATCH: the URM 'predicted' value is identical to the measured value to every quoted digit (deviation 0.0%). This is an identity, not a prediction: the value was taken from the measurement.
- L5: EXACT MATCH: the URM 'predicted' value is identical to the measured value to every quoted digit (deviation 0.0%). This is an identity, not a prediction: the value was taken from the measurement.
- L5: PROVENANCE: Document's 80.379 +/- 0.012 is an older average; the URM value equals the document's number exactly, not the current PDG value.
- L6: EXACT MATCH: the URM 'predicted' value is identical to the measured value to every quoted digit (deviation 0.0%). This is an identity, not a prediction: the value was taken from the measurement.
- L6: PROVENANCE: Document's 91.1876 +/- 0.0021 is the LEP-era value; close to, but not, the current PDG average.
- L7: KNOB-DRIVEN: the +5-7% correction is produced by a named adjustment parameter (Recursive flux factor 1.056 (832.0 x 1.056 = 878.6 ~= 879)), applied to the measured value; it is not derived from the framework's equations.
- L7: PROVENANCE: Document's 'measured' 832.0 +/- 29.0 pb coincides with the NNLO+NNLL Standard Model prediction (Top++), not with the ATLAS measurement it is attributed to.
- L8: KNOB-DRIVEN: the +5-7% correction is produced by a named adjustment parameter (Higher-dimensional projections ('6-7% dijet/dilepton')), applied to the measured value; it is not derived from the framework's equations.
- L9: KNOB-DRIVEN: the +5-7% correction is produced by a named adjustment parameter (Extra-dim energy loss ('6.5% missing ET'), extra-dim scale ~1 TeV), applied to the measured value; it is not derived from the framework's equations.
- L10: KNOB-DRIVEN: the +5-7% correction is produced by a named adjustment parameter (Higher-dimensional projections ('6-7% dijet/dilepton')), applied to the measured value; it is not derived from the framework's equations.
- S1: TRACE VIOLATION: the published eigenvalues (3.70, 0.80, 0.50, 0.30, 0.10) sum to 5.40, but every 5x5 correlation matrix has trace exactly 5, so its eigenvalues must sum to 5. The published spectrum is not the spectrum of the published matrix, nor of any 5x5 correlation matrix.
- S1: The document also prints lambda_1 = 2.80 in its cascade section ('2.80 (report) or 3.70 (plot)') while using 3.70 elsewhere; the recomputed value from its own matrix is 3.635 — neither printed number.
- S1: The Marchenko-Pastur edge for the actual case (p=5, n=22) is 2.18, not the printed 1.97 (and not the plot's 1.0 line). lambda_1 does exceed the correct edge, so the qualitative 'one dominant mode' reading survives; the printed numbers do not.
- S2: In natural units the covariance PCA is dominated by t_half (values 800-1600 yr; variance orders of magnitude larger than the other observables), giving PC1 ~= 100% — the published 0.30/0.24/0.19/0.16/0.11 profile cannot arise from the documented distributions in natural units.
- S2: The correlation PCA gives yet another profile (~eigenvalues/5 of the sample correlation matrix). Neither recomputation matches the published ratios; the source simulation's variable scaling is undocumented, so the published PCA cannot be reproduced or audited (CANNOT AGREE on method, DIFFERS on numbers).
- S3: INTERNAL CONTRADICTION: the document's bootstrap centres on r ~= 0.10 for sin^2(theta_W) vs M_Amat, but its own published correlation matrix gives r = 0.926 for the same pair. A bootstrap of data with correlation 0.926 cannot centre on 0.10. The reconstruction (built on the published matrix) bootstraps around r ~= 0.89. One of the two published artefacts does not describe the ensemble.
- S3: SIGNIFICANCE ERROR: at n = 22, r = 0.10 gives t = 0.45, p = 0.66 — nowhere near significant. 800 bootstrap resamples of 22 points do not create significance the sample does not contain; 'large n' is the resample count, not the sample size.
- S6: ARITHMETICALLY IMPOSSIBLE AS PUBLISHED: the document's own ranges cap sin^2(theta_W) deviations at 2.8% (values 0.231-0.238 vs null 0.2315) and M_Amat at 2.9% (136-144 vs null 140) — both below the 5% band floor. No dataset consistent with the published distributions can put either observable in the 5-7.5% band, yet the document reports 6/6 co-occurrence for both.
- S6: DM_sigma: the published distribution (peaks 1.5/2.5/3.0) vs the LUX-ZEPLIN upper-limit 'null' of 1.0 gives deviations of +50% to +200% — above the band, not in it.
- S6: t_half 0/6 'agrees' only trivially: model values sit ~7 orders of magnitude below the >1e10 yr null (deviation ~-100%), not just outside a 5-7.5% band as a 'threshold effect'.
- S6: H_0 cannot be checked at all: it is not in the ensemble and has no published per-reality values.
- S7: The published p = 0.0008 clustering result presupposes 6 flagged realities whose band membership is arithmetically impossible under the document's own published ranges and nulls (S6). The clustering machinery is implemented here exactly as described (PC1 of the published correlation matrix; label-permutation bootstrap, 10,000 resamples) and runs the moment a dataset with flagged realities is supplied — on every dataset consistent with the published summaries, there is nothing to run it on.

## Figures

![fig1_eigenvalue_spectrum.png](figures/fig1_eigenvalue_spectrum.png)

*S1 eigenvalue spectrum: recomputed vs published, with the correct Marchenko-Pastur edge.*

![fig2_pca_variance.png](figures/fig2_pca_variance.png)

*S2 PCA explained variance: published vs covariance vs correlation PCA on the reconstruction.*

![fig3_bootstrap_histogram.png](figures/fig3_bootstrap_histogram.png)

*S3 bootstrap correlation distribution vs the published CI [0.05, 0.15].*

![fig4_correlation_heatmap.png](figures/fig4_correlation_heatmap.png)

*S4 the published correlation matrix.*

![fig5_parameter_distributions.png](figures/fig5_parameter_distributions.png)

*Reconstructed ensemble distributions with null values marked.*

![fig6_deviation_band.png](figures/fig6_deviation_band.png)

*S6 per-reality |deviation| from nulls with the 5.0-7.5% band shaded (log scale).*

## Reproduce

```bash
.venv/bin/python tests/run_all.py
```

Inputs: `tests/TEST_CENSUS.md` (spec), `data/ensemble22_correlation_published.csv` (published matrix), `data/claims_registry.json`. The reconstruction seed is 20250922 throughout.
