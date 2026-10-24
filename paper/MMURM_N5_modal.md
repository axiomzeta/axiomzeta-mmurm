# MMURM — The N = 5 Modal System and n = 8 Ensemble

**Status:** construction + simulation, 2026-10-24. The author has not
developed these layers; at his direction ("you'll have to build those")
they are built here. Everything in this document that is the builder's
choice rather than the framework's is marked **[construction]**. Nothing
here is the author's canon, and nothing here is empirical data.
Computation: `tests/modal.py` (Group M). Raw data:
`data/modal8_observables.csv` (the single 8-reality dataset) and
`data/modal_eigenvalues.csv` (all 5,000 simulation draws). Companion to
`MMURM_N5_instantiation.md`.

## 1. What the legacy branch gives

Manuscript §6.4 (the N = 12 text): 12 modes with eigenvectors
$\vec{v}_k$ of an operator $\mathcal{U}$, weights $\lambda_k$ summing
to 1 (as printed 1.006, retained as printed); mode 1 ("22 Strings")
weight 0.780. Modal dynamics:

$$
\frac{d\Psi_k}{dt} = -i\omega_k \Psi_k + \sum_{j \ne k} c_{kj} \Psi_j
+ \gamma_k (\lambda_1 - 1) \Psi_k, \qquad
\omega_k = \omega_0 / F_k, \qquad
\gamma_k = 0.94\,(1 - \delta_{k1}),
$$

with $F_k$ the Fibonacci numbers, encompassing matrix
$(\mathcal{U}_{\mathrm{env}})_{ri} = R_r \cdot S_i$ ($r, i = 1\dots22$,
diagonal dominance $R_r \cdot S_r \propto F_r$), core scalar
$\mathcal{U}_{\mathrm{core}} = \lambda_1 = 3.71 \pm 0.04$ "[from] a
1,000-reality numerical simulation [simulated]", modal state
$|\Theta\rangle = \sum_k \Psi_k \vec{v}_k$, and constraint
$C_{\mathrm{modal}} = \sum_k \lambda_k (|\nabla\Psi_k|^2 +
|\partial_t\Psi_k|^2) = 0$.

Two legacy facts constrain everything built below. First, manuscript
Appendix R3 documents a three-way conflation in the draft: the modal
weight 0.780, "78% of cross-observable variance", and the ensemble
$\lambda_1 = 3.71$ are three distinct numbers that the draft merges.
Second, the stated-coupling modal drift on both branches is
growth-dominated with an undamped core (Group A: at N = 5, max real
eigenvalue +2.92/step, slowest decay 0.021/step, core intrinsic decay
exactly 0) — the dynamics form is carried, and its growth-dominated
character is not softened here.

## 2. The 5-mode system [construction]

$K = N = 5$ modes. Frequencies and damping follow the legacy formulas
with $F = (1, 1, 2, 3, 5)$:

| Mode k | $F_k$ | $\omega_k / \omega_0$ | $\gamma_k$ | Branch-invariant meaning |
|---|---|---|---|---|
| 1 | 1 | 1 | 0 | Core / fundamental resonance (by the $\gamma_1 = 0$ rule) |
| 2 | 1 | 1 | 0.94 | — (indexed only) |
| 3 | 2 | 1/2 | 0.94 | — (indexed only) |
| 4 | 3 | 1/3 | 0.94 | — (indexed only) |
| 5 | 5 | 1/5 | 0.94 | — (indexed only) |

Only ratios $\omega_k / \omega_0$ are used: $\omega_0$ is stated as
both 1.0 and $1.4 \times 10^{14}$ rad/s in the supplied material
(Group X flag), so no absolute frequency is asserted.

**Modal matrix, defined [construction].** The 5-branch modal matrix is
the $5 \times 5$ correlation matrix of modal amplitudes across the
$R = 8$ realities. Its eigenvalues $\lambda_k$ have trace exactly 5;
the modal weights are $w_k = \lambda_k / 5$, summing to 1. This
definition dissolves the R3 conflation by construction: on this branch
the modal weight of mode 1 and its variance share are the same number,
$w_1 = \lambda_1 / 5$, and can never diverge into two competing
"78%"-style claims again.

**Not specified, and not invented.** The 12 legacy layer names are
*not* mapped onto 5 modes: no rule for such a mapping is stated
anywhere in the supplied material, and any mapping would be
fabrication. Modes 2–5 therefore carry indices, frequencies, and
damping — but no layer names and no physical meanings — until the
author assigns them. The encompassing matrix is carried in form only:
$(\mathcal{U}_{\mathrm{env}})_{ri} = R_r \cdot S_i$ for $r, i = 1\dots8$
with $R_r \cdot S_r \propto F_r$, $F = (1, 1, 2, 3, 5, 8, 13, 21)$;
numerical entries are unspecified, exactly as on the legacy branch,
where they were never given either.

## 3. Two leading eigenvalues, kept distinct

| Symbol | Object | Legacy analogue |
|---|---|---|
| $\lambda_1^{\mathrm{obs}}(5)$ | Leading eigenvalue of the $5 \times 5$ correlation matrix of the five observables (sin²θ_W, DM σ, M_Amat, t_half, ρ_DE) across 8 realities | E1 / S1 at n = 22 |
| $\lambda_1^{\mathrm{mod}}(5)$ | Leading eigenvalue of the $5 \times 5$ correlation matrix of modal amplitudes across 8 realities | §6.4 modal decomposition at K = 12 |

The legacy text merges these (its $\lambda_1 = 3.71$ is attached to
both the ensemble and the modal core). They are different matrices
about different things, and they are never merged here.

**$\lambda_1(5)$ is defined as an ensemble statistic.** There is no
empirical 8-reality dataset. What exists is a simulation distribution,
and $\lambda_1(5)$ denotes its median. The single fixed-seed 8-reality
dataset is one draw of that distribution, reported as one draw.

## 4. The n = 8 observable ensemble (Group M3)

**Assumption, stated.** The observable arm reuses the published
$5 \times 5$ target correlation matrix via the same Gaussian copula
and published marginal summaries as the legacy reconstruction
(`tests/ensemble.py`). That matrix is the only published correlation
structure; nothing derives it for the 5-branch, and reusing it is an
assumption, not a derivation. t_half's marginal is carried as
published; its null-status problem (no measured t_half exists) is
unchanged.

- Single dataset (`data/modal8_observables.csv`, seed 20250922):
  eigenvalues $[3.1386,\ 0.9997,\ 0.6115,\ 0.2385,\ 0.0117]$,
  $\lambda_1^{\mathrm{obs}} = 3.1386$ — **one draw**, below the
  simulation median, above the null 95th percentile, below the MP edge.
  The near-zero fifth eigenvalue (0.0117) is typical small-n behaviour
  for five strongly correlated observables, not a finding.
- 1,000-draw simulation at n = 8: median **3.6928**, mean 3.6608,
  sd 0.4732, p5 2.7943, p95 4.3706; 83.5% of draws above the MP edge.
  The median sits near the legacy reconstruction's 3.659 because the
  target correlation matrix is the same — the population eigenvalue
  of the published matrix is ≈ 3.635, and n = 8 vs n = 22 changes the
  sampling noise around it, not the target.

## 5. The modal-amplitude ensembles (Groups M4–M5)

**Null (M4).** 1,000 draws of $8 \times 5$ i.i.d. standard normal
amplitudes: $\lambda_1^{\mathrm{mod}}$ median **2.1525**, mean 2.1855,
sd 0.3151, p5 1.7225, p95 **2.7415**; only 0.6% of null draws exceed
the MP edge 3.2061.

**Two bars, and their order.** For correlation matrices the
asymptotic Marchenko–Pastur edge $(1 + \sqrt{5/8})^2 = 3.2061$ sits
*above* the finite-sample null: the edge is a covariance asymptotic,
and the unit-diagonal constraint of a correlation matrix shrinks the
top eigenvalue. Verified with an independent seed: white-noise
correlation $\lambda_1$ medians 2.15 / 1.63 / 1.28 / 1.12 at
n = 8 / 22 / 100 / 500 against edges 3.21 / 2.18 / 1.50 / 1.21 — the
null approaches the edge from below as n grows. So the edge is the
*stricter* bar and the null p95 (2.7415) is the *operational* bar.
An earlier draft of this section had the direction backwards; the
simulation corrected it, and the correction is recorded here.

**One-factor sweep (M5).** Amplitudes $a \cdot f_i +
\sqrt{1 - a^2} \cdot \varepsilon_{ik}$ with a common factor $f$;
population $\lambda_1 = 1 + 4a^2$. Loadings are swept, not fitted —
no loading is claimed anywhere in the supplied material, so nothing
here bakes in a desired $\lambda_1$:

| Loading a | Population $\lambda_1$ | Simulated median | p95 | % > edge 3.21 | % > null p95 2.74 |
|---|---|---|---|---|---|
| 0.50 | 2.00 | 2.3809 | 3.2127 | 5.1% | 21.5% |
| 0.70 | 2.96 | 3.0824 | 3.9494 | 42.2% | 69.5% |
| 0.85 | 3.89 | 3.8966 | 4.5202 | 84.3% | 94.3% |

Reading: at n = 8, modal coherence must be strong to *typically*
clear the bars — loadings around 0.7 clear the operational bar in
about 7 draws in 10, and around 0.85 clear the strict bar in about
5 draws in 6. Even at a = 0.85, roughly 1 draw in 6 falls below the
edge. That is the small-n price, stated plainly in §6.

## 6. The falsifiable threshold (URM-11)

**Prediction [audit-derived, not author-stated].** A future empirical
dataset of 8 realities × 5 modes (or 5 observables) with
$\lambda_1$ above the null 95th percentile (2.7415) exceeds the
finite-sample random-matrix null at n = 8; above the MP edge
(3.2061) it clears the stricter asymptotic bar as well. Below 2.7415,
the modal-coherence claim has no support from that dataset.

**Small-n caveat.** At n = 8, p = 5 (ratio 0.625) the eigenvalue
distribution is wide — null p5–p95 spans 1.72–2.74, and the
one-factor arms span more than a full unit at every loading. This
test is weak: clearing the bar is necessary, not sufficient, for the
modal-coherence claim, and a single 8-row dataset can never carry
the weight the legacy text puts on its 1,000-reality run. A larger-n
modal dataset would be a stronger test than any n = 8 dataset can
be; the n = 8 bars exist because 8 is what this branch's reality
count gives, not because 8 is a good sample size.

## 7. Open items on this layer

1. Mode identities 2–5 (names, physical meanings) — the author's, when
   he assigns them; not derivable from the 12 legacy names.
2. Numerical $\mathcal{U}_{\mathrm{env}}$ entries (both branches).
3. Loadings: the sweep maps coherence strength to outcomes but
   claims no loading; a loading would have to come from the modal
   dynamics, not from fitting $\lambda_1$.
4. Empirical upgrade: a real 8 × 5 modal or observable dataset would
   upgrade M3/M4 from SIMULATION to measurement. Until one exists,
   $\lambda_1(5)$ is a simulation statistic with a stated threshold,
   and the 5-branch remains a provisional structural candidate —
   now with its statistical chapter simulated rather than missing.
