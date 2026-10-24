"""Group T — T4 branch-selection closure for the N = 5 time layer.

The source's T4 convention (Time Governing Equations, parameterized
restatement, section 2) maps three predicates to three branches:

    b = 1  for  dK >= 0
    b = 2  for  dK < 0 and Dcal > Dc
    b = 3  for  Bcal > Bc

where Dcal / Bcal are the T4 predicate variables (written script-D /
script-B in the restatement to avoid collision with the architecture
counts D = dimensions and B = branches per timeline).

That mapping, as stated, is not a function: it overlaps on two
predicate combinations and covers nothing on a third. This module
closes the branch-selection part of open item O2 with a single
[construction] rule -- priority in the source's own listing order
(1, then 2, then 3) -- and proves the closure by exhaustive
enumeration of the predicate space. It is the builder's construction,
not the author's canon, and it decides the branch index only: the
successor timeline l' remains unspecified, exactly as in the source.

No external packages are needed; run standalone:

    python tests/time_branch.py
"""

# Predicate combination: (dK >= 0, Dcal > Dc, Bcal > Bc).
# dK is real, so dK >= 0 and dK < 0 partition the sign axis exactly.

def source_predicates(combo):
    """Return the set of branches the source mapping assigns, possibly >1."""
    dk_ge0, d_gt, b_gt = combo
    out = set()
    if dk_ge0:
        out.add(1)
    if (not dk_ge0) and d_gt:
        out.add(2)
    if b_gt:
        out.add(3)
    return out


def priority_branch(combo):
    """[construction] Priority in the source's listing order 1 > 2 > 3.

    Returns a branch index 1..3, or None for 'no transition': when no
    predicate fires, T4 selects no successor branch and the state
    persists in its current channel. Returning None rather than
    inventing a fourth branch is deliberate -- the source gives no
    predicate for any other outcome.
    """
    dk_ge0, d_gt, b_gt = combo
    if dk_ge0:
        return 1
    if d_gt:
        return 2
    if b_gt:
        return 3
    return None


def all_combos():
    return [(a, b, c) for a in (False, True)
            for b in (False, True) for c in (False, True)]


def audit():
    """Exhaustive audit of the predicate space. Returns a plain dict."""
    combos = all_combos()
    assert len(combos) == 8, "predicate space must have 2^3 combinations"

    source_map = {c: sorted(source_predicates(c)) for c in combos}
    overlaps = [c for c in combos if len(source_map[c]) > 1]
    uncovered = [c for c in combos if len(source_map[c]) == 0]
    # P1 and P2 can never co-fire: they require dK >= 0 and dK < 0.
    assert all(not (1 in source_map[c] and 2 in source_map[c])
               for c in combos), "P1/P2 overlap is impossible by sign"

    priority_map = {c: priority_branch(c) for c in combos}
    # Priority rule is single-valued everywhere, agrees with the source
    # wherever the source is already single-valued, and never invents
    # a branch the source did not name.
    for c in combos:
        if len(source_map[c]) == 1:
            assert priority_map[c] == source_map[c][0], \
                f"priority changed a unique source assignment at {c}"
        assert priority_map[c] in (None, 1, 2, 3)
    reachable = sorted({b for b in priority_map.values() if b is not None})
    # Every branch is reachable, and the only no-transition case is
    # (dK < 0, Dcal <= Dc, Bcal <= Bc).
    assert reachable == [1, 2, 3], f"branches reachable: {reachable}"
    assert uncovered == [(False, False, False)], f"uncovered: {uncovered}"
    assert priority_map[(False, False, False)] is None

    return {
        "predicate_combinations": 8,
        "source_overlaps": [list(c) for c in overlaps],
        "source_overlap_count": len(overlaps),
        "source_uncovered": [list(c) for c in uncovered],
        "source_uncovered_count": len(uncovered),
        "priority_map": {str(list(c)): priority_map[c] for c in combos},
        "branches_reachable_at_N5": reachable,
        "no_transition_case": [False, False, False],
        "general_B_note": "At B = 4 (N = 12 branch) the source names no "
                          "predicate for branch 4; this rule assigns "
                          "branches 1-3 only and leaves branch 4 "
                          "unassigned rather than inventing a predicate.",
        "verdict": "O2 branch-selection CLOSED at N = 5 by [construction] "
                   "priority rule; successor timeline l' still open.",
    }


def run():
    """Return ([entry], {}) in the suite's standard shape for run_all.py."""
    a = audit()
    entry = {
        "id": "T1",
        "test": "T4 branch-selection closure at N = 5 (O2, branch-selection part)",
        "label": "CONSTRUCTION",
        "published_result": "Source T4 convention (Time Governing Equations, "
            "parameterized restatement, section 2): b = 1 for dK >= 0; "
            "b = 2 for dK < 0 and Dcal > Dc; b = 3 for Bcal > Bc. "
            "Stated with the caveat that the conditions overlap, so "
            "priority or multichannel selection must be specified (O2).",
        "recomputed_result": {
            "predicate_combinations_enumerated": a["predicate_combinations"],
            "source_overlap_count": a["source_overlap_count"],
            "source_overlaps": a["source_overlaps"],
            "source_uncovered_count": a["source_uncovered_count"],
            "source_uncovered": a["source_uncovered"],
            "closure_rule": "priority in the source's listing order "
                "1 > 2 > 3; no predicate firing -> no transition",
            "priority_map": a["priority_map"],
            "branches_reachable_at_N5": a["branches_reachable_at_N5"],
            "no_transition_case": a["no_transition_case"],
            "general_B_note": a["general_B_note"],
        },
        "verdict": "CLOSED (branch selection, construction)",
        "notes": ("Agrees with the source wherever the source is already "
                  "single-valued (asserted over all 8 combinations); the "
                  "only new choice is the uncovered case, deliberately "
                  "left as no-transition rather than inventing a fourth "
                  "predicate. NOT closed: successor timeline l' (O2's "
                  "remainder); branch 4 at N = 12 (no source predicate); "
                  "O1 (H_in/H_out) and F1/F2/F3 (theta/Delta-tau, state "
                  "space, Reality Anchor) are untouched."),
    }
    return [entry], {}


if __name__ == "__main__":
    import json
    print(json.dumps(audit(), indent=2))
