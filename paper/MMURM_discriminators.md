# MMURM — Branch Discriminators (Group V)

**Status:** construction + verdict, 2026-10-25. Built at the author's
direction to pin down one branch before a final paper, via the three
items named in the instantiation document's completion path: (1) the
deposited F(g) sweep, (2) an independent H(N), (3) a real 8 × 5 dataset
measured against URM-11. Computation: `tests/discriminators.py`
(Group V). Everything in this document that is the builder's choice
rather than the framework's is marked **[construction]**. Nothing here
is the author's canon, and nothing here is empirical data.

**Verdict first.** None of the three items pins down one branch —
for three different, specific reasons. The F sweep cannot be
deposited from the report (§1). H(N) can be derived, but as a curve
that satisfies the framework's recovery criteria at every N, so it
selects nothing without an anchor the material does not contain (§2).
The existing dataset's URM-11 verdict is operational-pass /
strict-fail on simulated data, and a single-branch test cannot select
between branches anyway (§3–§4). The final paper must therefore
present N = 5 as a provisional structural candidate with specified
layers, not as the selected branch — until at least one of the three
things in §5 lands.

## 1. The F(g) sweep: underdetermined, not depositable from the report

**What the report supplies, exhaustively.** The solver report gives
exactly four facts about F: the name ("topology free-energy"), two
values (F(5) = −9.2023, F(12) = −0.6029), the direction ("lower
wins"), and the unrestricted optimum (g = 1, rejected on
admissibility). The objective definition, the code, and the sweep
data were not supplied (Group I, item I3). A search of the Final
Draft text, the Julius Foundation text, all repository documents and
code, and the author's supplied files found no further definition:
no other mention of F exists anywhere in the material.

**The underdetermination proof.** Two explicit strictly increasing
functionals fit every stated fact:

| g | F_log (log-interpolation) | F_lin (linear) |
|---|---|---|
| 1 | −25.0112 | −14.1162 |
| 5 | −9.2023 | −9.2023 |
| 8 | −4.5856 | −5.5168 |
| 12 | −0.6029 | −0.6029 |

Both pass through the two reported points exactly, both are strictly
increasing (so both have their integer minimum at g = 1, as
reported), and both obey "lower wins" — yet they disagree by 0.9312
at g = 8. Any strictly increasing functional through the two points
does the same. Two points plus a monotonicity direction cannot
determine a functional, and reverse-engineering one from two points
would be numerology, not audit. Depositing either functional above
as "the sweep" would be invention.

**Deposit specification.** I3 upgrades from REPORTED-ONLY to
REPRODUCTION if and only if the following artifact arrives, from the
author or from Julius (the draft request to Julius already asks for
"how F is computed," which is this item):

1. The objective functional F(g) in closed form, with every constant
   stated and its topological meaning given (what "free energy" is
   being computed over what ensemble of genus-g configurations).
2. The code that evaluates it.
3. The full sweep table over the swept range (at minimum g = 1..64,
   showing F(1) minimal and F(5) < F(12)).
4. The admissibility-filter step as applied (the filter, not just
   its output).

Until then, I3 stays REPORTED-ONLY, and any constructed sweep built
in the future must be labeled [construction] with its functional
stated explicitly — never presented as the solver's sweep.

## 2. H(N): derived as [construction], anchorless, selects nothing

**Framework inputs (author's text, manuscript §9.9).** A.1: the
horizon ℋ is a nodal convergence region on the manifold where the
effective metric becomes null, with surface gravity κ. A.2: linearizing
modes near ℋ gives T_H = ħκ / (2πk_B c). A.3: S = (k_B c³ / 4Għ) A,
with trajectory-count Ω ∝ e^{A / 4ℓ_P²}. A.7 requires recovery of
T_H ∝ κ and S ∝ A; failure of the recovery falsifies the model.
Note what is missing: κ is introduced as a boundary parameter and
never derived from the manifold's structure. The recovered T_H, as
the solver report itself states, "contains no structural N."

**Construction assumptions [construction].**

- **C1:** horizon area is quantized by handles, A(g) = (g − 1) · A₁,
  for g ≥ 2. (One handle beyond the sphere adds one area quantum;
  the sphere itself carries no handle area in this counting.)
- **C2:** the Schwarzschild κ–area relation, κ = c²√(π/A), which the
  framework's A.7 requires it to recover — used here as the
  Hawking-side input, not as a framework derivation.
- **Minimal area quantum:** A₁ = 4ℓ_P², one Planck-area quantum per
  handle. This choice is the builder's, not the author's, and every
  absolute number below depends on it.

**Derivation.** From C1 + C2: κ(g) ∝ A(g)^{−1/2} ∝ (g − 1)^{−1/2},
so T_H(g) ∝ 1/√(g − 1). Define the independent Hawking observable

$$H(N) = \frac{T_H(N)}{T_H(5)} = \sqrt{\frac{4}{N-1}}.$$

| N | H(N) | T_H under C1 + minimal A₁ |
|---|---|---|
| 5 | 1.000 | ≈ 9.99 × 10³⁰ K |
| 12 | 0.603 | ≈ 6.03 × 10³⁰ K |

Ratio T_H(5)/T_H(12) = √(11/4) ≈ 1.6583; entropy ratio
S(12)/S(5) = 11/4 = 2.75.

**Why this selects nothing.** H(N) satisfies A.7's recovery criteria
at every N: T_H ∝ κ and S ∝ A hold by construction on both
branches. A curve that passes its own recovery test at every N
cannot rank N. The deeper problem is directional: the Hawking side
takes genus as an input (through A) and does not output it. Running
the identification the other way — a measured T_H implying a genus —
requires an absolute anchor fixing κ or A₁ independently, and no
such anchor exists in the supplied material. Note that even the
most natural candidate anchor would not suffice on its own: if the
lattice isomorphism identified the horizon temperature with the
phonon temperature from the G-band (≈ 2250 K), that gives one
equation in two unknowns (A₁, N) — N still does not follow without
A₁ fixed separately.

**Status of I4.** The derivation half is now met as [construction]:
H(N) exists, defined above, with its assumptions stated. The
empirical half remains open: without an anchor, no independent test
of N = 5 against Hawking physics can be performed. The absolute
temperatures in the table must never be quoted without C1 and the
minimal-A₁ choice — they are construction outputs, not framework
predictions and not measurements.

## 3. URM-11 verdict on the existing dataset (recomputed)

From `data/modal8_observables.csv` (5 observables × 8 realities:
sin²θ_W, DM σ, M_Amat, t_half, ρ_DE), recomputed correlation
eigenvalues: **[3.1386, 0.9997, 0.6115, 0.2385, 0.0117]**, sum 5.0,
λ₁^obs = **3.1386** — exactly Group M's number.

**Verdict: exceeds the operational bar (2.7415), does NOT clear the
strict bar (3.2061)** — margin below the strict bar: −0.0675.

**What this verdict does not show, stated plainly.**

- It is not empirical confirmation of anything. The dataset is a
  single simulated draw (seed 20250922, Group M stated-assumption
  construction), and its rows carry recognizable anchors (M_Amat ≈
  138–142, near the ~140 GeV Ameterasue; t_half ≈ 1203–1515, inside
  the 800–1600 range; sin²θ_W ≈ 0.233–0.236, near the measured
  0.23126) because it was constructed around them.
- It is not a branch selection. URM-11 tests N = 5 modal coherence on
  its own terms; there is no N = 12 dataset at the same n to compare
  against, and the bars are n-dependent, so cross-n comparisons of
  raw λ₁ are meaningless.
- The CSV itself is not measurement-ready: units for DM σ and ρ_DE
  are unstated, so the table cannot be re-measured as it stands.

## 4. Protocol for a real 8 × 5 dataset (pre-registered)

**Instrument.** The APQS polariton analog simulator (framework §7
program): 8 independent runs/sectors. This is not a preference but a
logical requirement: eight rows are realities, and only an analog
simulator instantiating 8 sectors can produce 8 rows. Collider or
astrophysical measurements give single-world values, not 8 rows.

**Observables, units declared before collection** (the CSV's
unstated units are not carried over): sin²θ_W (dimensionless, weak
mixing angle); DM σ (cm², dark-matter cross-section); M_Amat (GeV,
Ameterasue mass); t_half (yr, decoherence half-time); ρ_DE
(GeV/cm³, dark-energy density).

**Pre-registered bars (already fixed — no peeking problem for
future data).** Operational: λ₁ > 2.7415 exceeds the finite-sample
null. Strict: λ₁ > 3.2061 clears the asymptotic bar as well. At or
below 2.7415, the modal-coherence claim has no support from that
dataset.

**Comparative clause for branch selection.** A single-branch pass
supports that branch's coherence only. Selection needs a
pre-declared comparative statistic computed the same way on both
branches — for example, margin above one's own strict bar in units
of one's own null SD — declared before the data are seen, not
chosen after. For reference, the n = 22 bars by Group M's method
(1,000 draws, seed 20250922) are: null median 1.6216, null p95
1.9326, null SD 0.1737, MP edge 2.18. (The n = 8 null SD by the same
method is 0.3153.)

**Caveat carried over from Group M §6.** At n = 8 the test is weak
(null p5–p95 spans 1.72–2.74); clearing a bar is necessary, not
sufficient, for the modal-coherence claim, and a larger-n modal
dataset would be a stronger test than any n = 8 dataset can be.

## 5. Overall verdict and what would change it

| Item | Status after Group V |
|---|---|
| F(g) sweep | BLOCKED on definition; deposit specification delivered (§1) |
| H(N) | CONSTRUCTED as a curve; anchorless, selects nothing (§2) |
| Real 8 × 5 dataset | Existing verdict: operational-pass / strict-fail on simulated data (§3); real-data protocol registered (§4) |
| Branch pinned down? | **No.** N = 5 remains a provisional structural candidate with specified layers. |

What would change this verdict, in order:

1. **The F definition** (objective, code, full sweep table) from the
   author or Julius — the same "how F is computed" already
   requested in the draft to Julius. This alone would make branch
   selection auditable, though the selection itself would still
   rest on the sweep's own merits.
2. **A Hawking anchor** fixing κ or A₁ independently, which would
   turn H(N) from a curve into a test.
3. **A real APQS dataset** under §4 plus the pre-declared
   comparative statistic, which would test coherence on both
   branches head-to-head.

Until at least one lands, the final paper must not claim a selected
branch. What it can claim honestly is the current state: two
admissible branches, one (N = 5) with its seed, time, modal, and
discriminator layers specified and its remaining gaps named, the
other (N = 12) frozen as the original canon text.

**Registry note.** No new claim is registered: H(N) is a
[construction] quantity, not a claim; URM-11 is already registered;
V3 is a verdict on existing data, not a new claim.

## 6. Addendum 2026-10-25 (afternoon): validation-lab deposit

The author supplied the MMURM Phase-Hawking Validation Lab v4.0
(a falsification-first package; its 30 tests pass on Cami's VM, its
phase-inverse example and smoke emergence reproduce exactly). Two
deposits from it are copied verbatim into this repo's data
directory (md5-verified on deposit):

- `data/topology_sweep.json` — the full F(g) table, g = 0..16
  (F(5) = −9.202295078056759, F(12) = −0.6028778739347526, global
  minimum at g = 1, strictly increasing for g ≥ 1). V6 reproduces
  the solver's selection (min among {5, 12} → 5) from this table.
  Status change, stated precisely: I3 moves from "two reported
  values" to "full table deposited, selection reproduced". It does
  NOT move to full reproduction — the objective functional and the
  generator code are absent from the package, and no simple closed
  form in genus, χ, soft-mode count, or bridge integral fits all 17
  points, so F(g) still cannot be recomputed from a definition.
  The remaining F ask narrows to the functional alone.
- `data/validation_lab_standard_emergence.json` — the lab's
  preregistered 24-run blind-dynamics standard result (V7 checks
  its fields): status **unsupported** for N = 12; histogram
  9:1, 10:6, 11:8, 12:8, 13:1; 12 recurs in 8/24 (Wilson 95% CI
  [0.18, 0.53]) against a null that never produces 12 in 2000
  synthetic experiments (p = 0.0005); stable 12-recurrence 5/24;
  11 and 12 tie at the top, so the lab's modal field (11) is a
  tie-break, not a majority; dynamic horizon identifiability in
  12/24 runs. Read precisely: 12 is present in the dynamics well
  above chance but is not the dominant or stable answer, and the
  distribution spreads 9–13. Preset sensitivity is itself a
  finding: the lab's 5-run smoke preset (same master seed, 3
  seeds/run vs 6) gave modal 5 over range 4–7 with 0/5 for 12 —
  the blind-k outcome moves with the preset, so blind dynamics
  cannot yet weigh between branches until that shift is
  understood.

### Three H(N) versions, reconciled

| Version | Definition | Verdict |
|---|---|---|
| V2 temperature ratio [construction] | T_H(N)/T_H(5) = √(4/(N−1)) under handle-quantized area + Schwarzschild κ–area relation | Anchorless; satisfies recovery at every N; ranks nothing |
| Lab Schwarzschild log-slope (archived) | H = −dln(T_H)/dln(M) = 1/(N−2) under Tangherlini + D = N bridge | Anchored: standard 3+1 GR gives H = 1 → N = 3, inadmissible. Inconsistent with BOTH candidates; falsifies the conjunction (Hawking assumptions + D = N bridge), not N = 5 specifically |
| Lab phase cardinality (consistency only) | H_boundary = 2/(N+2), H_out = 1/(N+2) from the source 14-state architecture | N = 12 exactly, zero residual — restates the source; measures nothing |

The lab's own cross-evidence verdict is `cross_evidence_conflict`
(topology → 5, phase → 12, Hawking-slope → neither, blind
standard → unsupported for 12). V8 carries the updated synthesis:
**still NOT PINNED DOWN**, with the unblockers reordered — (a) the
F functional, (b) resolution of the Hawking-slope vs bridge
inconsistency (preregistered bridge revision, or a scope argument
for the black-hole regime), (c) a real APQS dataset under §4 plus
the comparative statistic, (d) blind-dynamics stabilization.
