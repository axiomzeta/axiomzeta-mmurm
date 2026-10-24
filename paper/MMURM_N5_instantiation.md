# MMURM — The N = 5 Instantiation

**Status:** instantiation document, 2026-10-23. The framework's seed
architecture is a one-parameter family (Section 1). The cleaned manuscript
(`MMURM_clean.md`) as published is the text of the **N = 12 instantiation**;
that line is frozen in this repository at the tag `n12-legacy`. This
document defines the **N = 5 instantiation**: every seed-dependent object
recomputed at N = 5, every branch-invariant object identified as such, and
everything that does not yet exist on this branch stated plainly.
Recomputation: `tests/architecture.py` (Group A) and
`tests/inverse_solver.py` (Group I). Companion: the framework's time
layer, restated in this parameterized form with the N = 5 instantiation
substituted, is `Time_Governing_Equations_parameterized.md` (source as
supplied: `Time_Governing_Equations_source_2026-10-23.md`).

## 1. The parameterized seed

Bridge relations (author's inverse-solver report, 2026-10-23):

$$
g = N, \qquad D = N, \qquad T = N + 2, \qquad \chi = 2 - 2N, \qquad
R = -\chi = 2N - 2,
$$

with Euler closure $\chi = D - (T \cdot B) + R$, forcing

$$
B = \frac{5N - 4}{N + 2} = 5 - \frac{14}{N + 2}.
$$

Positive-integer $B$ over $N = 2 \dots 64$ leaves exactly two admissible
branches, since $N + 2$ must divide 14:

| Quantity | N = 5 (this instantiation) | N = 12 (legacy) |
|---|---|---|
| Realities $R$ | 8 | 22 |
| Timelines $T$ | 7 | 14 |
| Branches/timeline $B$ | 3 | 4 |
| Branched channels $T \times B$ | 21 | 56 |
| Spatial dimensions $D$ | 5 | 12 |
| Genus $g$ | 5 | 12 |
| Euler characteristic $\chi$ | −8 | −22 |
| Closure $D - TB + R$ | 5 − 21 + 8 = −8 ✓ | 12 − 56 + 22 = −22 ✓ |

Selection between the branches currently rests on a topology free-energy
sweep reported as F(5) = −9.2023 vs F(12) = −0.6029 (**reported-only** —
the sweep is not deposited; Group I, item I3) and on the bridge
relations' provenance (flagged in I2). The stated discriminator is an
independent Hawking observable $H(N)$, which does not yet exist (I4).

## 2. Branch-invariant (carries over unchanged)

- The ten IFT field equations and their single-action Lagrangian — the
  field count (10) is not an architecture count.
- The Lindblad master equation form and the decoherence formalism,
  including Group X's audit: the 800–1600-year interval is not derivable
  from stated parameters on *either* branch, and the identified
  requirement (Δτ ≈ 2,170 yr/step, or a protected-sector leak
  ε ≈ 1.2×10⁻²⁴/step) is branch-invariant because it rests on γ = 0.94
  and the phonon timescale, not on N.
- The WFB layer forms ($T_{ijk}$, $m_{ijk}$ Eq. 5.2, bridge strength,
  hybridization) and the graphene G-band claim's form — subject to
  re-derivation of its Fibonacci indices (Section 3).
- The CTT / trajectory-class material and the Reality Anchor argument.

## 3. Rescaled at N = 5 (recomputed; `tests/architecture.py`)

- **Shadow projection.** $P_{\mathrm{shadow}} =
  \frac{\Gamma(R)}{\Gamma(D)} \oint_{\partial\mathcal{D}}
  \left(\sum_{f=1}^{R} \mathcal{F}_f\right) \cdot \prod_{d=1}^{D} \xi_d$
  with prefactor $\Gamma(8)/\Gamma(5) = 210$ (legacy: $\Gamma(22)/
  \Gamma(12) = 21!/11! \approx 1.28\times10^{12}$).
- **System state (Eq. 12.1 form).** Products read $\prod_{f=1}^{D}
  \mathcal{F}_f \cdot \prod_{i=1}^{R} S_i$ → $\prod_{f=1}^{5}
  \mathcal{F}_f \cdot \prod_{i=1}^{8} S_i$ under the natural reading of
  the legacy limits (12 = D, 22 = R); flagged as an interpretation of
  the printed limits, not a silent edit.
- **Master equation (Eq. 11.1 form).** $\sum_{i=1}^{R} S_i$ → 8 terms;
  the evaluated form's factor $\cdot 22$ → $\cdot 8$. The prefactor
  $\Gamma(5)/\zeta(2) = 14.59$ is the subject of the open identification
  in Section 5 — it is **not** rescaled here.
- **Modal system.** $K = N = 5$ modes; $\omega_k = \omega_0 / F_k$,
  $k = 1 \dots 5$; $\gamma_k = 0.94\,(1 - \delta_{k1})$ as stated;
  $C_{\mathrm{modal}}$ sums to 5. Stated-coupling drift spectrum
  (Group A): max real eigenvalue +2.92/step, slowest decay 0.021/step,
  core mode intrinsically undamped — qualitatively the legacy branch's
  structure at smaller size. Full modal specification, including the
  n = 8 ensemble, is `MMURM_N5_modal.md` (Group M, 2026-10-24).
- **String modes.** Phases $\phi_i = 2\pi i / R$ → $2\pi i / 8$.
- **Three-body display.** $\sum_{r=1}^{R} R_r \otimes
  \Psi_{\mathrm{gravity}}$ → sum to 8.
- **Topology.** Genus-5 manifold, $\chi = -8$. The "twelve handles"
  epigraph and dodecagonal language of the manuscript are N = 12-branch
  artifacts and are retained there as such.

## 4. What does not exist on this branch (yet)

- **Ensemble statistics (simulated, not empirical — Group M,
  2026-10-24).** Groups S and E, the correlation matrix, the
  bootstrap, the eigenvalue spectrum, and λ₁ = 3.71 are **N = 12-branch
  objects**, computed (by Julius, and in re-performance) at n = 22.
  Nothing from the 12-branch statistics transfers — but the 5-branch
  statistical chapter is now simulated rather than missing
  (`MMURM_N5_modal.md`): λ₁^obs(5) median 3.6928 and λ₁^mod(5) null
  median 2.1525 (null p95 2.7415, MP edge 3.2061) from 1,000-draw
  n = 8 simulations with published raw data. What is still missing is
  an *empirical* 8 × 5 dataset: until one exists, λ₁(5) is a
  simulation statistic with a stated falsifiable threshold, not a
  measurement.
- **The topology free-energy sweep** F(g) — reported-only (I3).
- **H(N)** — the independent Hawking observable that would discriminate
  the branches — not derived (I4).

## 5. Open identifications (recorded, not decided)

1. **Γ(5)/ζ(2) = 14.59 (Group A, item A4).** If the Eq. 11.1 prefactor's
   argument is the structural N, the printed value is consistent only
   with N = 5 (at N = 12, Γ(N)/ζ(2) ≈ 2.43×10⁷). If it is an independent
   constant, the match at N = 5 is coincidence. The supplied material
   does not decide; the prefactor is carried unchanged on both branches
   until it does.
2. **Core-dimension count 8.** $\Omega_{\mathrm{foam}}$ and
   $\Psi_{\mathrm{gravity}}$ sum over 8 core dimensions on the legacy
   branch, where 8 is an independent constant. It numerically equals
   R(5). No derivation in the supplied material identifies core count
   with R; it is **not** identified here.
3. **"22 strings" (UST layer).** Readable as R strings (→ 8 at N = 5) or
   as a fixed string count. Recorded as an interpretation question for
   the UST layer's next revision.

## 6. Completion path for this instantiation

1. ~~An n = 8 ensemble simulation with **published raw data**~~ —
   **done as simulation (Group M, 2026-10-24):** raw data published
   (`data/modal8_observables.csv`, `data/modal_eigenvalues.csv`),
   λ₁(5) defined as ensemble statistics with a falsifiable threshold
   (URM-11). The remaining step on this item is an *empirical* 8 × 5
   dataset, which would upgrade the simulation to measurement.
2. Deposit of the topology sweep → I3 upgrades to REPRODUCTION and the
   branch selection becomes auditable.
3. Derivation of an independent H(N) → the branches become empirically
   discriminable in principle.

Until (2)–(3) land, this instantiation is exactly what the solver
labeled it: a **provisional structural candidate**, now with its
seed, time, and statistical layers specified, with its remaining
missing pieces named rather than papered over.
