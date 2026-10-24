# MMURM — T4 Branch-Selection Closure at N = 5 (Group T)

**Status:** construction, 2026-10-24. The author has not developed this
layer; at his direction ("you'll have to build those") it is built
here. Everything in this document that is the builder's choice rather
than the framework's is marked **[construction]**. Nothing here is the
author's canon, and nothing here is empirical data. Computation:
`tests/time_branch.py` (Group T). Companion to
`Time_Governing_Equations_parameterized.md`.

## 1. The problem, exactly

The time layer's T4 convention, as the author stated it at N = 5,
maps three predicates to three branches (predicate variables written
𝒟, ℬ, per the restatement's disambiguation from the architecture
counts D and B):

- b = 1 for ΔK ≥ 0
- b = 2 for ΔK < 0 and 𝒟 > 𝒟ᶜ
- b = 3 for ℬ > ℬᶜ

This is not a function. Over the 8 combinations of the three binary
conditions (ΔK ≥ 0?, 𝒟 > 𝒟ᶜ?, ℬ > ℬᶜ?):

- **3 combinations overlap** (two predicates fire at once): (ΔK < 0,
  𝒟 > 𝒟ᶜ, ℬ > ℬᶜ) → b = 2 or 3; (ΔK ≥ 0, ℬ > ℬᶜ) with either 𝒟
  value → b = 1 or 3.
- **1 combination is uncovered** (no predicate fires): (ΔK < 0,
  𝒟 ≤ 𝒟ᶜ, ℬ ≤ ℬᶜ) → no branch at all.
- P1 and P2 can never co-fire: they require ΔK ≥ 0 and ΔK < 0
  simultaneously, so the overlap is always between b = 3 and one of
  b = 1, b = 2 — never all three.

This is open item O2 from the time layer, in its branch-selection
part: "priority or multichannel selection must be specified."

## 2. The closure [construction]

**Rule: priority in the source's own listing order, 1 > 2 > 3.**

1. If ΔK ≥ 0 → b = 1, whatever ℬ does.
2. Else if ΔK < 0 and 𝒟 > 𝒟ᶜ → b = 2, whatever ℬ does.
3. Else if ℬ > ℬᶜ → b = 3.
4. Else → **no transition**: T4 selects no successor branch and the
   state persists in its current channel.

Why listing order, rather than another priority? It is the only
priority the source itself suggests — the predicates are listed
1, 2, 3 — and it changes nothing the source already decides
uniquely: wherever exactly one predicate fires, the rule returns
exactly that branch (verified by enumeration). The one genuinely
new choice is step 4, and it is chosen to *not* invent: assigning
the uncovered case to any branch would be a fourth, unstated
predicate, so it is left as no-transition instead.

**What this proves (by exhaustive enumeration, `tests/time_branch.py`):**

- The rule is single-valued on all 8 combinations.
- All three branches remain reachable: b = 1, b = 2 and b = 3 each
  occur for at least one combination.
- The only no-transition case is (ΔK < 0, 𝒟 ≤ 𝒟ᶜ, ℬ ≤ ℬᶜ).

## 3. What this does not close

- **Successor timeline ℓ′.** T4 selects a branch index; which
  successor timeline ℓ′ the transition lands on (including whether
  ℓ′ = ℓ is allowed) is still unspecified in the source and is
  untouched here. O2 is therefore closed for *branch selection* at
  N = 5, not for T4 as a whole.
- **The general-B form.** At N = 12, B = 4, the source names no
  predicate for branch 4. This rule assigns branches 1–3 only and
  leaves branch 4 unassigned rather than inventing a predicate.
  A branch-4 predicate, if the author ever states one, slots into
  the same priority framework without disturbing branches 1–3.
- **O1, F1, F2, F3** are untouched: the horizon pair H_in/H_out,
  the 168 sector-indexed θ values and the Δτ gap, the global update
  index and undeclared state space, and the Reality Anchor's form
  on M⁵ all remain open exactly as recorded in the time layer.

## 4. Status in the repo

This layer is **local only, unpushed**: it sits in the working tree
as `paper/MMURM_N5_time_branch.md` + `tests/time_branch.py` and has
been run standalone (all assertions pass). Pushing it needs the
author's go and a fresh push token — the previous token's copy was
shredded after the Group M push, and it expires Friday, Oct 30 in
any case. Wiring into `tests/run_all.py` and the census/claims
registry is the one remaining integration step before a push.
