# Time Governing Equations — Parameterized Restatement

**Status:** restatement, 2026-10-23. Source: the author's revised
8–7–3–21–5 formulation (`Time_Governing_Equations_source_2026-10-23.md`),
restated here in the parameterized seed form used throughout this
repository (Groups A and I), with the N = 5 instantiation substituted.
No equation's content is altered. The source's own caveats are retained
in place; editorial disambiguations are marked [ed.]; audit flags are
collected in Section 4 in the source's own convention of explicit
caveat statements. Companion to `MMURM_N5_instantiation.md`.

Time is modeled as update order arising from a recursively evolving
phase state. Duration, causal direction, and branching are projections
of the update structure. The formulation retains the four original
equations, with the architecture counts carried symbolically.

## 1. Configuration and indexing (parameterized)

Architecture counts from the bridge system (Group A): realities
$R = 2N - 2$, timelines $T = N + 2$, branches $B$ with
$B = (5N-4)/(N+2)$, dimensions $D = N$.

| Symbol | Range (general) | N = 5 | N = 12 (legacy) | Interpretation |
|---|---|---|---|---|
| $r$ | $1, \dots, R$ | 1…8 | 1…22 | Reality sector |
| $\ell$ | $1, \dots, T$ | 1…7 | 1…14 | Timeline within reality $r$ |
| $b$ | $1, \dots, B$ | 1…3 | 1…4 | Branch within timeline $\ell$ |
| $c = B(\ell-1) + b$ | $1, \dots, T \cdot B$ | 1…21 | 1…56 | Branched-channel index within a reality |
| $x = (x^1, \dots, x^D)$ | $x \in M^D$ | $M^5$ | $M^{12}$ | Spatial coordinate |

Counting rule: $T \times B$ channels per reality; $R \times T \times B$
indexed reality–channel combinations globally — **168** at N = 5
(1,232 at N = 12). These are discrete sectors and pathways, not spatial
dimensions. The channel index $c = B(\ell-1)+b$ is a bijection
$(\ell, b) \leftrightarrow c$ [verified for both branches].

*Branch note.* The legacy time layer predates this indexed form: its
admissibility set was $\{C_1, \dots, C_{12}, H_{in}, H_{out}\}$. The
N = 12 column above is therefore the parameterized family's reading of
the legacy counts, not a legacy statement; the legacy layer's own
structure is the subject of Open Item O1.

## 2. The four equations (parameterized; N = 5 substituted)

### T1 — Recursive succession across indexed sectors

$$
P^{(r,\ell,b)}_{n+1}(x) = R_{r,\ell,b}\left[P^{(r,\ell,b)}_{n}(x);\
C_n, A_n, G_D\right]
$$

Here $P$ is a phase state on the $D$-dimensional spatial manifold
$M^D$, $R$ is the state-update map, $C_n$ and $A_n$ retain the original
model's context/control inputs, and $G_D$ denotes optional geometric
data (such as a metric) on $M^D$. Coupling between sectors is not
assumed unless specified separately.

*Instantiation (N = 5):* $r \in 1\dots8$, $\ell \in 1\dots7$,
$b \in 1\dots3$, $G_5$ on $M^5$ — the source's form, unchanged.

### T2 — Temporal-channel admissibility

$$
\Pi_{\mathcal{T}}\left(P_n \to P_{n+1} \mid r, x\right) \in
\mathcal{T}_{T \cdot B} = \{\,C_{\ell,b} : \ell = 1, \dots, T;\
b = 1, \dots, B\,\}
$$

[ed.: the admissibility *set* is written $\mathcal{T}$ to distinguish it
from the timeline count $T$; the source uses $T$ for both.]

$C_{\ell,b}$ labels one of the $T \cdot B$ branch channels in each
reality. A complete state is indexed by $(r, \ell, b, x)$; the global
set of indexed channels is $\mathcal{T} = \{\,(r, C_{\ell,b})\,\}$,
with cardinality $R \cdot T \cdot B$.

*Instantiation (N = 5):* $\mathcal{T}_{21}$, global cardinality 168 —
the source's form. This replaces the original fourteenfold
admissibility set $\{C_1, \dots, C_{12}, H_{in}, H_{out}\}$; see O1.

### T3 — Duration as a phase projection

$$
\Delta\Theta^{(r,\ell,b)}_{n}(x) =
\mathrm{Arg}\left[\tau_{n+1}(x)\,\tau_n(x)^{*}\right], \qquad
\frac{t_{n+1}}{t_n} =
\exp\left[\Delta\Theta^{(r,\ell,b)}_{n}(x) \,\big/\, \theta_{r,\ell,b}\right]
$$

The logarithmic relation $\Delta\Theta = \theta \ln(t_{n+1}/t_n)$ is a
constitutive model assumption, not a general mathematical identity of
complex phase. It requires positive clock readings, nonzero $\theta$,
and a chosen phase-unwrapping convention; otherwise Arg is defined
only modulo $2\pi$. (This is the indexed form of the framework's
standing temporal-phase structure $\tau(t) = e^{i\theta \ln t + \phi}$:
the phase increment between successive updates is
$\theta \ln(t_{n+1}/t_n)$ mod $2\pi$.) Identical at both branches in
form; the sector indices are the only change.

### T4 — Causal direction and $B$-way temporal branching

$$
C_{\ell,b} \;\longrightarrow\; \{\,C_{\ell',1};\ \dots;\
C_{\ell',B}\,\} \quad \text{subject to } A_r(\Delta K, \mathcal{D},
\mathcal{B}, x)
$$

$A_r$ is an admissibility/selection rule, and $\ell'$ denotes an
allowed successor timeline (which may equal $\ell$ if within-timeline
transitions are intended).

[ed.: the source's predicate variables $D$ and $B$ collide with the
architecture counts ($D$ = dimensions, $B$ = branches per timeline).
They are written $\mathcal{D}$ and $\mathcal{B}$ here — a
disambiguation of symbols only; the predicates are the source's.]

The original conditions $\Delta K \ge 0$; $\Delta K < 0$ with
$\mathcal{D} > \mathcal{D}^c$; and $\mathcal{B} > \mathcal{B}^c$ can
still serve as selection predicates, but their mapping to the $B$
branches must be declared. The source's proposed convention at N = 5
is $b = 1$ for $\Delta K \ge 0$; $b = 2$ for $\Delta K < 0$ and
$\mathcal{D} > \mathcal{D}^c$; $b = 3$ for $\mathcal{B} >
\mathcal{B}^c$. For general $B$ (the legacy branch has $B = 4$) the
convention must be re-declared per branch. See O2.

## 3. Open items carried from the source (retained, not resolved)

- **O1 — Fate of $H_{in}/H_{out}$.** The parameterized admissibility
  set $\mathcal{T}_{T \cdot B}$ contains no horizon pair. The original
  fourteenfold set's $H_{in}, H_{out}$ must be explicitly specified —
  retained as distinct channels, mapped onto branch channels, or
  retired — rather than silently equating them with the new branches.
  This is now a *branch* question as well: the horizon pair belongs to
  the legacy layer, and its status on the N = 5 branch is undecided.
- **O2 — Predicate overlap.** The T4 selection conditions overlap, so
  priority or multichannel selection must be specified. Unchanged from
  the source; the general-$B$ form additionally requires the
  branch↔predicate mapping to be declared for each branch.
  **Branch selection at N = 5: CLOSED 2026-10-24 (Group T,
  `MMURM_N5_time_branch.md`)** by [construction] priority in the
  source's listing order (1 > 2 > 3), with the uncovered case as no
  transition — proven by exhaustive enumeration of the 8 predicate
  combinations. What remains of O2 is the successor timeline $\ell'$
  (which timeline a transition lands on), still unspecified, plus
  branch 4 at N = 12, for which the source names no predicate.

## 4. Flagged seams (audit, 2026-10-23)

Stated in the source document's own convention — explicit caveats
attached to the formulation, to be closed by specification, not by
silence.

- **F1 — Sector-indexed phase scale; no Δτ.** T3 makes the
  phase-to-duration scale sector-dependent, $\theta_{r,\ell,b}$: up to
  $R \cdot T \cdot B$ distinct values (168 at N = 5), none specified.
  Duration is thereby sector-relative in a stronger sense than the
  original single-$\theta$ form. Further, T3 constrains clock
  *ratios* only; it does not assign a proper-time duration to an
  update step. The decoherence audit's identified requirement
  (Group X: Δτ ≈ 2,170 yr/step, or a protected-sector leak
  ε ≈ 1.2×10⁻²⁴/step) is therefore **unaffected by this layer** —
  T1–T4 neither supply Δτ nor constrain it.
- **F2 — Global update index; undeclared global state space.** In T1
  the update index $n$ is a single global counter shared by all
  sectors: cross-reality synchrony of update order is thereby
  assumed, and the assumption is nowhere stated as one. Relatedly,
  the global state space over the $R \cdot T \cdot B$ indexed channels
  is not declared — direct sum over sectors (dimension additive in
  $R$) versus tensor product (dimension multiplicative) fixes the size
  of every global object, including the density matrix on which the
  decoherence claim (URM-9) is defined. Both points must be specified
  before global quantities are computed from this layer.
- **F3 — Reality Anchor form on $M^D$.** The framework's Reality
  Anchor is the Einstein field equation, a statement about 4D
  spacetime. In this formulation space is $M^D$ and time is update
  order; the anchor's statement for general $D$ — and in particular
  its N = 5 form (a 5-spatial-dimensional geometry? an emergent 4D
  spacetime within it?) — is not given in the supplied material.
  $G_D$ in T1 is accordingly "optional geometric data" until the
  anchor is restated for this layer.

## 5. Summary of the restatement

The four equations survive parameterization intact; the N = 5
instantiation reproduces the source text exactly under substitution
$R{=}8$, $T{=}7$, $B{=}3$, $D{=}5$. Two open items are the source's own
(O1, O2); three seams are flagged by the audit (F1–F3). None of the
five is a defect of arithmetic — each is a specification the layer
needs and does not yet have, recorded here so that closing them is a
matter of writing the specification down. **Update 2026-10-24:** O2's
branch-selection part is closed at N = 5 by Group T (see §3); O1,
F1–F3, and O2's successor-timeline remainder stay open.
