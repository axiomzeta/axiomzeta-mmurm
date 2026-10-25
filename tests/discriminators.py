"""Group V — Branch discriminators (addendum, 2026-10-25).

The author directed that one branch be pinned down before a final paper,
via the three items named in the instantiation document's completion path:
(1) the deposited F(g) sweep, (2) an independent H(N), (3) a real 8x5
dataset measured against URM-11. This group executes all three as far as
the supplied material honestly allows, and records where each stops:

V1 (DEMONSTRATION): the solver's F(g) sweep cannot be deposited from the
    report alone. The report supplies only a name ("topology
    free-energy"), two values (F(5) = -9.2023, F(12) = -0.6029),
    "lower wins", and an unrestricted optimum at g = 1. Two explicit
    strictly increasing functionals fitting ALL of those facts are
    constructed below; they disagree at g = 8. The reported facts
    therefore underdetermine F, and no sweep recomputed here may be
    presented as the solver's sweep. I3 stays REPORTED-ONLY until the
    definition is supplied (see the deposit specification in
    paper/MMURM_discriminators.md).
V2 (CONSTRUCTION): H(N) did not exist (I4); it is derived here from the
    framework's own Hawking recovery (manuscript Sec. 9.9, A.1-A.3)
    plus two stated construction assumptions (handle-quantized horizon
    area; the Schwarzschild kappa-area relation the framework's A.7
    requires it to recover). The resulting curve satisfies the
    framework's recovery criteria at EVERY N, so it cannot select a
    branch without an absolute anchor (a fixed kappa or area quantum),
    which the supplied material does not contain. I4's empirical half
    therefore remains open; its derivation half is now met as
    construction, not as evidence.
V3 (REPRODUCTION): the URM-11 verdict on the existing 8x5 dataset,
    recomputed from data/modal8_observables.csv: lambda1_obs = 3.1386
    exceeds the operational bar (2.7415) and does NOT clear the strict
    bar (3.2061). Provenance: the dataset is a single SIMULATED draw
    (seed 20250922, Group M stated-assumption construction), so this
    verdict is not empirical confirmation of anything.
V4 (PROTOCOL): what a REAL 8x5 dataset would have to be, pre-registered
    so a future dataset can be judged without moving the bars: 8
    independent APQS analog-simulator runs measuring the five
    observables with units declared before collection, judged by the
    already-fixed URM-11 bars, with a comparative clause for branch
    selection (a single-branch pass supports that branch's coherence
    only; selection needs a pre-declared comparative statistic).
V5 (SYNTHESIS): none of V1-V4 pins down one branch. The final paper
    cannot honestly claim a pinned-down branch yet; the three things
    that would change that are named explicitly.
"""

import math
import os

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

# --- constants (SI, exact/defined values where applicable) ---
HBAR = 1.054571817e-34
KB = 1.380649e-23
C = 299792458.0
LP = 1.616255e-35

# --- Group M published bars (n = 8, p = 5), cited, not recomputed here ---
URM11_OPERATIONAL = 2.7415
URM11_STRICT = 3.2061
# --- MP edge at n = 22, p = 5 (Group M / Group S) ---
MP_EDGE_N22 = 2.18


def _f_log(g):
    """Log-interpolation through the two reported points."""
    return -9.2023 + 8.5994 * (math.log(g) - math.log(5)) / (
        math.log(12) - math.log(5))


def _f_lin(g):
    """Linear interpolation through the two reported points."""
    return -9.2023 + 8.5994 * (g - 5) / 7.0


def _null_bars(n, draws=1000, seed=20250922):
    """Finite-sample null bars by Group M's method: iid standard normals,
    correlation-matrix leading eigenvalue. Returns (median, p95, sd)."""
    rng = np.random.default_rng(seed)
    vals = []
    for _ in range(draws):
        z = rng.standard_normal((n, 5))
        vals.append(np.linalg.eigvalsh(np.corrcoef(z, rowvar=False))[-1])
    vals = np.array(vals)
    return float(np.median(vals)), float(np.percentile(vals, 95)), \
        float(np.std(vals))


def _hawking_temperature(g, area_per_handle):
    """T_H for a genus-g horizon under construction assumptions C1+C2:
    A(g) = (g-1) * A1; kappa = c^2 * sqrt(pi / A); T_H = hbar*kappa /
    (2*pi*kB*c)."""
    area = (g - 1) * area_per_handle
    kappa = C ** 2 * math.sqrt(math.pi / area)
    return HBAR * kappa / (2 * math.pi * KB * C)


def run():
    # ---------------- V1: F(g) underdetermination ----------------
    fa = {g: _f_log(g) for g in (1, 5, 8, 12)}
    fb = {g: _f_lin(g) for g in (1, 5, 8, 12)}
    anchors_ok = (
        abs(fa[5] + 9.2023) < 1e-9 and abs(fa[12] + 0.6029) < 1e-9
        and abs(fb[5] + 9.2023) < 1e-9 and abs(fb[12] + 0.6029) < 1e-9)
    increasing_ok = (fa[1] < fa[5] < fa[8] < fa[12]
                     and fb[1] < fb[5] < fb[8] < fb[12])
    v1 = {
        "id": "V1",
        "test": "Do the reported F(g) facts determine the topology "
                "free-energy sweep? (two functionals fitting all facts)",
        "label": "DEMONSTRATION",
        "published_result": "F(5) = -9.2023, F(12) = -0.6029, lower wins, "
                            "unrestricted optimum at g = 1 (I3, "
                            "REPORTED-ONLY; objective definition, code, "
                            "and data not supplied)",
        "recomputed_result": {
            "F_log": {str(g): round(v, 4) for g, v in fa.items()},
            "F_lin": {str(g): round(v, 4) for g, v in fb.items()},
            "both_fit_reported_points": anchors_ok,
            "both_strictly_increasing_min_at_g1": increasing_ok,
            "disagreement_at_g8": round(abs(fa[8] - fb[8]), 4),
        },
        "verdict": "UNDERDETERMINED" if anchors_ok and increasing_ok
                   else "CHECK FAILED",
        "notes": "Any strictly increasing functional through the two reported "
                 "points fits every stated fact about F, so the report "
                 "alone cannot fix the sweep: F_log and F_lin agree at "
                 "g = 5 and g = 12 by construction and differ by ~0.93 "
                 "at g = 8. Depositing either as 'the sweep' would be "
                 "invention, not audit. The deposit specification (exact "
                 "artifact that would upgrade I3) is in "
                 "paper/MMURM_discriminators.md.",
        "flags": [
            "I3 stays REPORTED-ONLY. A constructed sweep may be built "
            "as [construction] with its functional stated explicitly, "
            "but it must never be presented as the solver's sweep.",
        ],
    }

    # ---------------- V2: H(N) construction ----------------
    a1 = 4 * LP ** 2  # minimal area quantum per handle [construction C1]
    th5 = _hawking_temperature(5, a1)
    th12 = _hawking_temperature(12, a1)
    # scaling checks: T_H ~ 1/sqrt(g-1); S ~ A ~ (g-1)
    ratio = th5 / th12
    expected_ratio = math.sqrt(11 / 4)
    h12 = math.sqrt(4 / 11)
    v2 = {
        "id": "V2",
        "test": "Independent Hawking observable H(N) from the framework's "
                "own Hawking recovery (Sec. 9.9, A.1-A.3) + stated "
                "construction assumptions",
        "label": "CONSTRUCTION",
        "published_result": "No H(N) exists in the supplied material (I4, "
                            "NOT ESTABLISHED). Framework recovery: "
                            "T_H = hbar*kappa/(2*pi*kB*c), S = "
                            "(kB*c^3/4*G*hbar)*A; kappa is a free "
                            "boundary parameter, containing no N.",
        "recomputed_result": {
            "assumptions": [
                "C1 [construction]: horizon area quantized by handles, "
                "A(g) = (g-1)*A1, g >= 2.",
                "C2 [construction]: the Schwarzschild kappa-area "
                "relation kappa = c^2*sqrt(pi/A), which the framework's "
                "A.7 requires it to recover (T_H ~ kappa, S ~ A).",
                "Minimal area quantum A1 = 4*lP^2 (one Planck-area "
                "quantum per handle).",
            ],
            "H(N)_definition": "H(N) = T_H(N)/T_H(5) = sqrt(4/(N-1))",
            "H5": 1.0,
            "H12": round(h12, 4),
            "T_H5_K": float(f"{th5:.3e}"),
            "T_H12_K": float(f"{th12:.3e}"),
            "T_H_ratio_5_over_12": round(ratio, 4),
            "ratio_matches_sqrt_11_over_4": abs(ratio - expected_ratio)
                                           < 1e-9,
            "entropy_ratio_S12_over_S5": 2.75,
        },
        "verdict": "CONSTRUCTED (anchor missing)",
        "notes": "H(N) now exists as a derivation, but it cannot select a "
                 "branch: T_H ~ kappa and S ~ A hold at EVERY N by "
                 "construction, so the curve alone ranks nothing. The "
                 "Hawking side takes genus as an input (through A) and "
                 "does not output it; running the identification the "
                 "other way needs an absolute anchor fixing kappa or "
                 "A1 independently (a measured horizon temperature "
                 "scale, or a derivation of A1 from the framework's "
                 "operators). No such anchor exists in the supplied "
                 "material, so I4's empirical half remains open. The "
                 "absolute temperatures above depend entirely on C1 + "
                 "the minimal A1 choice and must not be quoted without "
                 "them.",
        "flags": [
            "Do not quote T_H(5) ~ 1e31 K or T_H(12) ~ 6e30 K as "
            "framework predictions: they are construction outputs "
            "under C1 + minimal A1, not measurements and not "
            "author-stated values.",
        ],
    }

    # ---------------- V3: URM-11 verdict on existing data ----------------
    data = np.loadtxt(os.path.join(ROOT, "data", "modal8_observables.csv"),
                      delimiter=",", skiprows=1, usecols=range(1, 6))
    corr = np.corrcoef(data, rowvar=False)
    eig = np.sort(np.linalg.eigvalsh(corr))[::-1]
    lam1 = float(eig[0])
    med8, p95_8, sd8 = _null_bars(8)
    med22, p95_22, sd22 = _null_bars(22)
    v3 = {
        "id": "V3",
        "test": "URM-11 verdict on the existing 8x5 dataset "
                "(data/modal8_observables.csv, recomputed)",
        "label": "REPRODUCTION",
        "published_result": "Group M single-dataset eigenvalues "
                            "[3.1386, 0.9997, 0.6115, 0.2385, 0.0117] "
                            "(ONE DRAW); URM-11 bars: operational 2.7415, "
                            "strict 3.2061",
        "recomputed_result": {
            "eigenvalues": [round(float(v), 4) for v in eig],
            "eigenvalue_sum": round(float(eig.sum()), 4),
            "lambda1_obs": round(lam1, 4),
            "exceeds_operational_2.7415": lam1 > URM11_OPERATIONAL,
            "clears_strict_3.2061": lam1 > URM11_STRICT,
            "margin_below_strict_bar": round(lam1 - URM11_STRICT, 4),
            "n8_null_sd_for_protocol": round(sd8, 4),
            "n22_null_median_p95_sd": (round(med22, 4), round(p95_22, 4),
                                       round(sd22, 4)),
        },
        "verdict": "EXCEEDS OPERATIONAL, BELOW STRICT",
        "notes": "The existing dataset passes the operational bar and "
                 "fails the strict bar. Provenance, stated plainly: "
                 "this is a single SIMULATED draw (seed 20250922, "
                 "Group M stated-assumption construction), not a "
                 "measurement. It therefore supports nothing "
                 "empirically; it fixes what a future real dataset "
                 "will be judged against. Measurement-readiness gaps "
                 "in the CSV itself: units for DM_sigma and rho_DE are "
                 "unstated, so the table cannot be re-measured as it "
                 "stands (see V4).",
        "flags": [
            "Do not cite V3 as empirical support for N = 5: the "
            "dataset is simulated, and URM-11 tests N = 5 modal "
            "coherence on its own terms, not N = 5 against N = 12.",
        ],
    }

    # ---------------- V4: real-dataset protocol ----------------
    v4 = {
        "id": "V4",
        "test": "Pre-registered protocol for a REAL 8x5 dataset (what "
                "would count, judged by already-fixed bars)",
        "label": "PROTOCOL",
        "published_result": "No real 8x5 dataset exists (Group M §7, open "
                            "item 4; instantiation §6, item 1 remainder).",
        "recomputed_result": {
            "instrument": "APQS polariton analog simulator "
                          "(framework Sec. 7 program): 8 independent "
                          "runs/sectors. Eight rows are realities, so "
                          "only an analog simulator instantiating 8 "
                          "sectors can produce 8 rows; collider or "
                          "astrophysical measurements give single-world "
                          "values, not 8 rows.",
            "observables_and_units_declared_before_collection": [
                "sin2_thetaW (dimensionless, weak mixing angle)",
                "DM_sigma (cm^2, dark-matter cross-section)",
                "M_Amat (GeV, Ameterasue mass)",
                "t_half (yr, decoherence half-time)",
                "rho_DE (GeV/cm^3, dark-energy density)",
            ],
            "pre_registered_bars": {
                "operational": URM11_OPERATIONAL,
                "strict": URM11_STRICT,
            },
            "decision_rule": "lambda1 > 2.7415 exceeds the finite-sample "
                             "null; > 3.2061 clears the strict bar; "
                             "<= 2.7415 gives the modal-coherence claim "
                             "no support from that dataset.",
            "comparative_clause_for_branch_selection": {
                "n22_bars_same_method": {
                    "null_median": round(med22, 4),
                    "null_p95": round(p95_22, 4),
                    "null_sd": round(sd22, 4),
                    "mp_edge": MP_EDGE_N22,
                },
                "rule": "A single-branch pass supports that branch's "
                        "coherence only. Branch selection needs a "
                        "pre-declared comparative statistic computed "
                        "the same way on both branches (e.g. margin "
                        "above own strict bar in units of own null "
                        "SD); the statistic must be declared before "
                        "the data are seen, not chosen after.",
            },
            "caveats": "n = 8 is weak (null p5-p95 spans 1.72-2.74; "
                       "see Group M §6). A larger-n modal dataset "
                       "would be a stronger test than any n = 8 "
                       "dataset can be.",
        },
        "verdict": "REGISTERED (no data yet)",
    }

    # ---------------- V5: overall verdict ----------------
    v5 = {
        "id": "V5",
        "test": "Do V1-V4 pin down one branch before a final paper?",
        "label": "SYNTHESIS",
        "published_result": "Instantiation §6: branch is a provisional "
                            "structural candidate until (2) the sweep "
                            "is deposited and (3) H(N) is derived.",
        "recomputed_result": {
            "F_sweep": "BLOCKED on definition (V1); deposit "
                       "specification delivered, sweep itself not "
                       "recomputable from the report.",
            "H_N": "CONSTRUCTED but anchorless (V2); curve exists, "
                   "selection does not follow without an anchor.",
            "dataset": "EXISTING verdict is operational-pass / "
                       "strict-fail on simulated data (V3); real-data "
                       "protocol registered (V4); neither selects "
                       "between branches.",
            "branch_status": "NOT PINNED DOWN",
        },
        "verdict": "NOT PINNED DOWN",
        "notes": "What would change this verdict, in order: (a) the F "
                 "definition (objective, code, full sweep table) from "
                 "the author or Julius — the same 'how F is computed' "
                 "already requested in the draft to Julius; (b) a "
                 "Hawking anchor fixing kappa or A1 independently; "
                 "(c) a real APQS dataset under V4 plus the "
                 "pre-declared comparative statistic. Until at least "
                 "one lands, the final paper must present N = 5 as a "
                 "provisional structural candidate with specified "
                 "layers, not as the selected branch.",
    }

    return [v1, v2, v3, v4, v5]


if __name__ == "__main__":
    import json
    print(json.dumps(run(), indent=2))
