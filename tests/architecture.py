"""Group A — Parameterized seed architecture (2026-10-23).

The framework's seed integers are treated as a one-parameter family.
Under the bridge relations (Group I)
    g = N,  D = N,  T = N + 2,  chi = 2 - 2N,  R = -chi = 2N - 2,
    chi = D - (T * B) + R        (Euler closure)
the branch factor is forced: B = (5N - 4)/(N + 2) = 5 - 14/(N + 2), and
positive-integer B over N = 2..64 leaves exactly two admissible branches,
N = 5 and N = 12. This module computes both branches' seed-dependent
objects from the manuscript's stated formulas, so the N = 5 instantiation
(tests/../paper/MMURM_N5_instantiation.md) rests on recomputation, not
assertion. Quantities that exist for one branch only are labeled as such;
nothing is transferred between branches silently.
"""
from fractions import Fraction
from math import factorial

import numpy as np
from scipy.special import zeta


def architecture(N):
    """Seed architecture for structural count N (exact rational B)."""
    B = Fraction(5 * N - 4, N + 2)
    arch = {
        "N": N,
        "R_realities": 2 * N - 2,
        "T_timelines": N + 2,
        "B_branches_per_timeline": B,
        "admissible": B.denominator == 1 and B > 0,
        "D_dimensions": N,
        "g_genus": N,
        "chi": 2 - 2 * N,
    }
    if arch["admissible"]:
        arch["channels_TxB"] = arch["T_timelines"] * int(B)
        arch["closure_D_minus_TB_plus_R"] = (
            arch["D_dimensions"] - arch["channels_TxB"]
            + arch["R_realities"])
        arch["closure_holds"] = (arch["closure_D_minus_TB_plus_R"]
                                 == arch["chi"])
    return arch


def admissible_set(lo=2, hi=64):
    return [N for N in range(lo, hi + 1) if architecture(N)["admissible"]]


def p_shadow_prefactor(N):
    """Gamma(R)/Gamma(D) in P_shadow = [Gamma(R)/Gamma(D)] oint ... :
    (R-1)! / (D-1)! exactly."""
    a = architecture(N)
    return Fraction(factorial(a["R_realities"] - 1),
                    factorial(a["D_dimensions"] - 1))


def mp_edge(p, n):
    """Marchenko-Pastur upper edge (1 + sqrt(p/n))^2 for a p-observable
    correlation matrix estimated from n realities."""
    return (1.0 + np.sqrt(p / n)) ** 2


def modal_drift_spectrum(K, gamma=0.94, lam1=3.71, eps=0.15):
    """Real drift spectrum of the manuscript's stated modal dynamics at
    K modes (same construction as decoherence.py Part C): diagonal
    gamma_k (lambda_1 - 1) with gamma_k = gamma (1 - delta_k1), coupling
    c_kj = eps * m_kj with m from Eq. 5.2, third index at the core."""
    A = np.zeros((K, K))
    for k in range(1, K + 1):
        gk = gamma * (1.0 - (1.0 if k == 1 else 0.0))
        A[k - 1, k - 1] += gk * (lam1 - 1.0)
        for j in range(1, K + 1):
            if j != k:
                m = np.exp(-((k - j) ** 2 + (j - 1) ** 2 + (1 - k) ** 2)
                           / (2 * 6.0 ** 2))
                A[k - 1, j - 1] += eps * m
    ev = np.linalg.eigvals(A)
    return {
        "modes": K,
        "max_real_eigenvalue": float(ev.real.max()),
        "min_real_eigenvalue": float(ev.real.min()),
        "core_mode_intrinsic_decay_per_step": 0.0,
    }


def branch_objects(N):
    a = architecture(N)
    return {
        "architecture": {k: (str(v) if isinstance(v, Fraction) else v)
                         for k, v in a.items()},
        "p_shadow_prefactor_GammaR_over_GammaD": str(p_shadow_prefactor(N)),
        "mp_edge_p5_at_n_equals_R": mp_edge(5, a["R_realities"]),
        "modal_drift_stated_couplings": modal_drift_spectrum(N),
        "phi_total_sum_terms_R": a["R_realities"],
        "gammaN_over_zeta2": float(factorial(N - 1) / zeta(2)),
    }


def run():
    adm = admissible_set()
    b5, b12 = branch_objects(5), branch_objects(12)
    gamma5_matches = abs(b5["gammaN_over_zeta2"] - 14.59) < 0.01
    gamma12_matches = abs(b12["gammaN_over_zeta2"] - 14.59) < 0.01
    return [
        {
            "id": "A1",
            "test": "Parameterized admissibility of the seed family "
                    "(bridge relations + Euler closure), N = 2..64",
            "label": "REPRODUCTION",
            "published_result": "Admissible branches {5, 12} (Group I)",
            "recomputed_result": {"admissible_branches": adm},
            "verdict": "AGREES" if adm == [5, 12] else "DIFFERS",
        },
        {
            "id": "A2",
            "test": "Both branches' seed architectures and closures",
            "label": "REPRODUCTION",
            "published_result": "N=5: R=8, T=7, B=3, 21 channels, D=5, "
                                "chi=-8. N=12: R=22, T=14, B=4, 56 "
                                "channels, D=12, chi=-22",
            "recomputed_result": {"N5": b5["architecture"],
                                  "N12": b12["architecture"]},
            "verdict": "AGREES" if (b5["architecture"]["closure_holds"]
                                    and b12["architecture"]["closure_holds"])
                       else "DIFFERS",
        },
        {
            "id": "A3",
            "test": "Branch-dependent derived objects, recomputed per "
                    "branch from the manuscript's stated formulas",
            "label": "DERIVATION-CHECK",
            "published_result": "Published objects exist for the N=12 "
                                "branch only (manuscript passim; Groups "
                                "S/E ensemble at n=22; lambda_1 = 3.71 of "
                                "the 12-layer modal object)",
            "recomputed_result": {"N5": b5, "N12": b12},
            "verdict": "COMPUTED for both branches — see notes",
            "notes": "P_shadow prefactor Gamma(R)/Gamma(D): N=5 -> 210; "
                     "N=12 -> 21!/11!. Marchenko-Pastur edge (p=5): "
                     "n=8 -> 3.21 vs n=22 -> 2.18 (the S1-corrected edge "
                     "is the 12-branch value). Stated-coupling modal "
                     "drift: both branches growth-dominated, core mode "
                     "intrinsically undamped. CRITICAL SCOPE NOTE: the "
                     "ensemble statistics (Groups S/E) and lambda_1 = 3.71 "
                     "are N=12-branch objects computed at n=22. The N=5 "
                     "branch currently has NO ensemble statistics and NO "
                     "lambda_1: at n=8 those must be newly simulated, and "
                     "nothing in the 12-branch results transfers.",
        },
        {
            "id": "A4",
            "test": "Identification of the Eq. 11.1 prefactor Gamma(5)/"
                    "zeta(2) = 14.59 under parameterization",
            "label": "DERIVATION-CHECK",
            "published_result": "Phi_total (Eq. 11.1) carries prefactor "
                                "Gamma(5)/zeta(2) = 14.59 in the legacy "
                                "(N=12) text",
            "recomputed_result": {
                "Gamma(N)/zeta(2) at N=5": b5["gammaN_over_zeta2"],
                "Gamma(N)/zeta(2) at N=12": b12["gammaN_over_zeta2"],
                "printed_value": 14.59,
                "matches_at_N5": gamma5_matches,
                "matches_at_N12": gamma12_matches,
            },
            "verdict": "UNRESOLVED identification",
            "flags": [
                "If the prefactor's argument is the structural N, the "
                "printed 14.59 is consistent ONLY with N=5 (at N=12 it "
                "would be ~2.43e7). If it is an independent constant, it "
                "is branch-invariant and the match at N=5 is coincidence. "
                "The supplied material does not decide between these "
                "readings; recorded as an open identification, not as "
                "evidence for either branch.",
            ],
        },
    ]


if __name__ == "__main__":
    import json
    print(json.dumps(run(), indent=2, default=str))
