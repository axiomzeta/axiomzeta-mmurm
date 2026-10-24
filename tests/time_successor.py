"""Group U (options, NOT a closure) — successor timeline l' for T4 at N = 5.

Group T closed the branch-selection part of O2: given the three T4
predicates, the branch index b in 1..3 is single-valued (priority
1 > 2 > 3, uncovered case = no transition). What Group T deliberately
did NOT close is the successor timeline l' in the T4 arrow

    C_{l,b} -> {C_{l',1}; ...; C_{l',B}}.

The source's only statement about l' is that it "denotes an allowed
successor timeline (which may equal l if within-timeline transitions
are intended)". That is a permission, not a rule: it allows l' = l, it
does not prescribe it, and it names no rule mapping (l, b) -> l'.

This module enumerates the candidate rules that are consistent with
everything the source says, and proves their graph properties, so
that adopting one is a visible choice with visible consequences
rather than a silent assumption. SELECTION (2026-10-24): the author
selected stay (l' = l). That selection is recorded in run() as
[construction]; the enumeration below is unchanged, and stay's
selection does not depend on the flagged assumptions for its
definition (no mod-7 arithmetic is used; predicates are not consulted
for l').

At N = 5 the timeline count is T = 7 (see the parameterized
restatement summary: R = 8, T = 7, B = 3, D = 5). Timelines are
indexed l = 0..6 and branches b = 1..3. The branch index is taken as
given by Group T; predicates are treated as independent of l, since
the source states no l-dependence for them (flagged as an assumption
below, not a finding).

Candidate rules, each a function of (l, b) unless noted:

    stay:           l' = l
    advance-branch: l' = (l + b) mod 7
    advance-one:    l' = (l + 1) mod 7
    retreat-branch: l' = (l - b) mod 7
    free:           l' in {0..6} — set-valued by design; l' is an
                    output of the admissibility rule A_r, not a
                    function of (l, b) at all.

No external packages are needed; run standalone:

    python tests/time_successor.py
"""

T = 7
BRANCHES = (1, 2, 3)


def stay(l, b):
    return l


def advance_branch(l, b):
    return (l + b) % T


def advance_one(l, b):
    return (l + 1) % T


def retreat_branch(l, b):
    return (l - b) % T


FUNCTION_RULES = {
    "stay": stay,
    "advance-branch": advance_branch,
    "advance-one": advance_one,
    "retreat-branch": retreat_branch,
}


def one_step_reachable(rule, l):
    """Timelines reachable from l in one transition under rule."""
    if rule == "free":
        return set(range(T))
    f = FUNCTION_RULES[rule]
    return {f(l, b) for b in BRANCHES}


def reachable_closure(rule, l):
    """Timelines reachable from l over any number of transitions."""
    seen = set()
    frontier = {l}
    while frontier:
        seen |= frontier
        nxt = set()
        for x in frontier:
            nxt |= one_step_reachable(rule, x)
        frontier = nxt - seen
    return seen


def audit():
    """Enumerate every (l, b) pair and prove each rule's properties."""
    pairs = [(l, b) for l in range(T) for b in BRANCHES]
    assert len(pairs) == 21, "timeline/branch pairs must be 7 x 3"

    out = {"timelines_T": T, "branches_B": BRANCHES, "pairs": len(pairs),
           "rules": {}}
    for name in list(FUNCTION_RULES) + ["free"]:
        # Single-valuedness: a function rule gives exactly one l' per
        # pair; free gives the whole set by design, which is the point.
        if name == "free":
            images = {pair: list(range(T)) for pair in pairs}
            single_valued = False
        else:
            f = FUNCTION_RULES[name]
            images = {pair: f(*pair) for pair in pairs}
            single_valued = all(isinstance(v, int) for v in images.values())
            assert all(0 <= v < T for v in images.values()), \
                f"{name} produced an out-of-range timeline"
        # One-step and long-run reachability from timeline 0 (the same
        # counts hold from any l by translation symmetry of mod 7).
        one = sorted(one_step_reachable(name, 0))
        closure = sorted(reachable_closure(name, 0))
        out["rules"][name] = {
            "single_valued_function_of_l_b": single_valued,
            "one_step_reachable_from_one_timeline": one,
            "one_step_count": len(one),
            "long_run_reachable_from_one_timeline": closure,
            "long_run_count": len(closure),
        }

    # The properties the decision turns on, asserted rather than stated:
    # stay is the only function rule that keeps a transition inside its
    # own timeline; every step-rule reaches all 7 timelines in the long
    # run; free is the only rule that makes no choice at all.
    assert out["rules"]["stay"]["one_step_count"] == 1
    assert out["rules"]["stay"]["long_run_count"] == 1
    assert out["rules"]["advance-one"]["one_step_count"] == 1
    assert out["rules"]["advance-one"]["long_run_count"] == 7
    assert out["rules"]["advance-branch"]["one_step_count"] == 3
    assert out["rules"]["advance-branch"]["long_run_count"] == 7
    assert out["rules"]["retreat-branch"]["one_step_count"] == 3
    assert out["rules"]["retreat-branch"]["long_run_count"] == 7
    assert out["rules"]["free"]["one_step_count"] == 7
    assert out["rules"]["free"]["single_valued_function_of_l_b"] is False
    # Forward vs backward is a pure sign choice: advance-branch and
    # retreat-branch have identical reachability profiles, so no
    # property of the graph distinguishes them — only an author
    # statement could.
    assert (out["rules"]["advance-branch"]["one_step_count"],
            out["rules"]["advance-branch"]["long_run_count"]) == \
           (out["rules"]["retreat-branch"]["one_step_count"],
            out["rules"]["retreat-branch"]["long_run_count"])

    out["verdict"] = (
        "NOT CLOSED: no source statement selects among these rules. "
        "stay is the only rule with any textual support, and that "
        "support is a permission ('may equal l'), not a prescription. "
        "advance-branch vs retreat-branch are graph-identical, so "
        "direction is an author choice, not a derivable one.")
    out["assumptions_flagged"] = [
        "Predicates (dK, Dcal, Bcal) treated as independent of timeline "
        "index l: the source states no l-dependence, but also does not "
        "rule it out. If predicates depend on l, the (l, b) pair space "
        "is not the full 21 pairs.",
        "Timeline indices 0..6 are labels only: mod-7 arithmetic is a "
        "bookkeeping device for the candidate rules, not a claim that "
        "timelines are cyclically ordered in the framework.",
    ]
    return out


def run():
    """Return ([entry], {}) in the suite's standard shape for run_all.py.

    Wired in following the author's 2026-10-24 selection of stay.
    The audit() enumeration is unchanged; the selection is layered
    on top of it and marked [construction].
    """
    a = audit()
    a["selected_rule"] = {
        "rule": "stay",
        "definition": "l' = l for every (l, b) pair",
        "selected_by": "author decision, 2026-10-24",
        "status": "[construction], not source canon",
        "consequence": "transitions change branch, never timeline; "
            "timelines evolve independently (consistent with T1's "
            "no-free-coupling rule)",
        "scope": "N = 5 only; whether stay generalizes to the N = 12 "
            "branch is not decided here",
    }
    entry = {
        "id": "U1",
        "test": "Successor timeline l' at N = 5: stay selected (O2 remainder)",
        "label": "CONSTRUCTION (author-selected)",
        "published_result": "Source T4 arrow: C_{l,b} -> {C_{l',1}; ...; "
            "C_{l',B}} subject to A_r; l' 'denotes an allowed successor "
            "timeline (which may equal l if within-timeline transitions "
            "are intended)'. No rule mapping (l, b) -> l' is stated.",
        "recomputed_result": a,
        "verdict": "SELECTED: stay (l' = l) — O2 successor part closed "
                   "at N = 5 by construction",
        "notes": ("Stay is the minimal rule and the only one with any "
                  "textual support, but that support is a permission "
                  "('may equal l'), not a prescription — hence "
                  "[construction], not canon. The unselected rules "
                  "(advance-one, advance-branch, retreat-branch, free) "
                  "remain enumerated in the audit for the record. "
                  "Branch 4 at N = 12, the general-B form, O1, and "
                  "F1–F3 are untouched."),
    }
    return [entry], {}


if __name__ == "__main__":
    import json
    print(json.dumps(audit(), indent=2))
