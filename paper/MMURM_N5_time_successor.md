# MMURM — Successor Timeline ℓ′ for T4 at N = 5 (Group U)

**Status:** stay selected by author decision 2026-10-24, recorded as
[construction]. This document began as an options register (2026-10-24);
the candidate enumeration is unchanged, and the selection is layered
on top of it. The author has not developed this layer; at his
direction ("you'll have to build those") the candidate space was
built here. Nothing in this document is the author's canon in the
source-text sense, and nothing here is empirical data. Computation:
`tests/time_successor.py` (Group U, wired into `tests/run_all.py`
following the selection).

## 1. What Group T left open, exactly

Group T closed the branch-selection part of open item O2: given the
three T4 predicates, the branch index b ∈ {1, 2, 3} is single-valued
(priority 1 > 2 > 3, uncovered case = no transition). What it did
not close is the other half of the T4 arrow:

$$
C_{\ell,b} \;\longrightarrow\; \{\,C_{\ell',1};\ \dots;\ C_{\ell',B}\,\}
\quad \text{subject to } A_r(\Delta K, \mathcal{D}, \mathcal{B}, x)
$$

The source's only statement about ℓ′ is that it "denotes an allowed
successor timeline (which may equal ℓ if within-timeline transitions
are intended)". That sentence is a permission, not a rule: it allows
ℓ′ = ℓ, it does not prescribe it, and it names no mapping
(ℓ, b) → ℓ′. Unlike Group T, where the source's own listing order
1, 2, 3 supplied a tiebreak, there is no tiebreak in the source for
ℓ′ at all. Any deterministic ℓ′ rule is therefore a choice, and this
document refuses to dress one up as a derivation.

## 2. The candidate space [construction]

At N = 5, timelines T = 7, branches B = 3 (parameterized restatement
summary: R = 8, T = 7, B = 3, D = 5). The pair space is 7 × 3 = 21
(ℓ, b) pairs, treating the predicates as independent of ℓ — the
source states no ℓ-dependence for them, and that assumption is
flagged, not hidden (see §4).

| Rule | Definition | One step from one timeline | Long run |
|---|---|---|---|
| **stay** | ℓ′ = ℓ | 1 timeline (itself) | 1 timeline |
| **advance-one** | ℓ′ = (ℓ + 1) mod 7 | 1 timeline | all 7 |
| **advance-branch** | ℓ′ = (ℓ + b) mod 7 | 3 timelines | all 7 |
| **retreat-branch** | ℓ′ = (ℓ − b) mod 7 | 3 timelines | all 7 |
| **free** | ℓ′ ∈ {0..6}, chosen by A_r | all 7 | all 7 |

Verified by enumeration in `tests/time_successor.py` (all assertions
pass). Two findings matter for the decision:

- **Stay is the only rule with any textual support** — and that
  support is the "may equal ℓ" permission, not a prescription.
  Adopting stay is still a choice; it is just the minimal one.
- **Forward vs backward is undecidable from the graph:**
  advance-branch and retreat-branch have identical reachability
  profiles (3 in one step, all 7 in the long run). Direction can
  only come from an author statement, never from the math here.
- **Free is the honest non-choice:** it declines to invent a rule
  and hands ℓ′ to A_r as an output — but A_r itself is unspecified,
  so free closes nothing; it just names where the gap lives.

## 3. The decision, made

**Selected 2026-10-24, by the author: stay — ℓ′ = ℓ for every
(ℓ, b) pair, recorded as [construction].** Transitions change
branch, never timeline. Consequence, stated plainly: at N = 5 the
seven timelines evolve independently of one another — consistent
with T1's rule that coupling between sectors is not assumed unless
specified, now extended in effect to timelines. The unselected rules
(advance-one, advance-branch, retreat-branch, free) remain
enumerated in §2 and in the test audit for the record; they are not
adopted.

Scope of the closure: O2 is now closed **at N = 5** — branch
selection by Group T's priority rule, successor timeline by stay.
What stays open: the general-$B$ form (branch 4 at N = 12 has no
source predicate, and whether stay generalizes to the N = 12 branch
is not decided here). Stay's definition uses no mod-7 arithmetic
and consults no predicates for ℓ′, so flagged assumption 2 is moot
for the selected rule (it still conditions the pair-space
enumeration, which is retained as background).

This layer is committed with the suite wiring; its push follows
whatever token the author next authorizes, per protocol.

## 4. What this does not close, and two flagged assumptions

- Branch 4 at N = 12, O1 (H_in/H_out), and F1–F3 are untouched.
- **Assumption 1:** predicates independent of ℓ. If they depend on
  ℓ, the 21-pair space is not the full space.
- **Assumption 2:** timeline indices 0..6 are labels only. Mod-7
  arithmetic is bookkeeping for the candidate rules, not a claim
  that timelines are cyclically ordered in the framework.

## 5. Housekeeping, folded into this commit

`paper/MMURM_N5_time_branch.md` §4 said Group T was "local only,
unpushed" — true when drafted, stale since commit 2217ada went live
on main (39 files, verified 2026-10-24). That section is corrected
in this commit; no token was minted for the correction alone.
