"""Group X — Decoherence half-life audit (author-supplied addendum,
2026-10-23; NOT part of the original Julius 38-item suite).

Claim under audit (manuscript + author's decoherence memo,
*800_to_1600_Decoherence.docx*): a multiversal Lindblad half-decoherence
time t1/2 ~ 800-1600 years.

Method: use ONLY numbers the manuscript itself states:
  - gamma = 0.94 per recursion (energy decay; constants table, Sec. 6.2)
  - decoherence jump operator L ~ sqrt(gamma) * sigma_z (Sec. 6.3 table)
  - modal damping gamma_k = 0.94 * (1 - delta_k1): core mode k=1 undamped
  - modal coupling c_kj = eps * m_kj with eps ~ 0.15 (parameter sweep)
  - lambda_1 = 3.71
  - Lambda = 0.12 s^-1 (Eq. 1 instance damping -- the only rate in seconds)
  - omega_0 = 1.0e14 rad/s (Sec. 6.2 table; body text also states 1.4e14)
  - graphene G-band 1580 cm^-1 (experimental anchor)
Everything else -- in particular the per-recursion proper-time step dtau
and any protected-sector leak rate -- is treated as a free parameter and
swept, so the output is the *requirement* the claim imposes, not an
assumption smuggled in.
"""
import json
import os

import numpy as np

LN2 = float(np.log(2.0))
YR_S = 365.25 * 86400.0
GAMMA = 0.94


def compute():
    r = {}

    # ---- A. The memo's Gamma_eff <-> t1/2 conversion, recomputed.
    g_lo, g_hi = LN2 / 1600.0, LN2 / 800.0                      # per year
    r["A_memo_budget"] = {
        "gamma_eff_per_yr": [g_lo, g_hi],
        "gamma_eff_per_s": [g_lo / YR_S, g_hi / YR_S],
        "memo_claim_per_s": [1.37e-11, 2.75e-11],
        "agrees": bool(abs(g_lo / YR_S - 1.37e-11) < 0.05e-11
                       and abs(g_hi / YR_S - 2.75e-11) < 0.05e-11),
        "illustrative_check_yr": LN2 / 7.5e-4,                   # -> 924 yr
    }

    # ---- B. Stated decoherence operator L = sqrt(gamma) sigma_z.
    sz = np.diag([1.0, -1.0])
    L = np.sqrt(GAMMA) * sz
    I2 = np.eye(2)
    Liouv = (np.kron(L, L) - 0.5 * np.kron(L.T @ L, I2)
             - 0.5 * np.kron(I2, L.T @ L))
    eigs = np.linalg.eigvals(Liouv)
    decay_rates = sorted({round(float(-e.real), 10) for e in eigs
                          if e.real < -1e-9})
    slowest = decay_rates[0]                                     # 2*gamma
    t_half_steps = LN2 / slowest
    r["B_stated_dephasing"] = {
        "operator": "L = sqrt(0.94) * sigma_z (manuscript Sec. 6.3)",
        "liouvillian_eigenvalues": sorted([complex(e) for e in eigs],
                                          key=lambda z: z.real),
        "slowest_decay_per_step": slowest,
        "t_half_steps": t_half_steps,
    }

    # ---- C. Modal drift spectrum (real part), per recursion step.
    # dPsi_k/dt = -i w_k Psi_k + sum_j c_kj Psi_j + gamma_k (lambda1-1) Psi_k
    # c_kj = eps * m_kj, m from Eq. 5.2 with third index fixed at the core.
    lam1, eps, N = 3.71, 0.15, 12
    A = np.zeros((N, N))
    for k in range(1, N + 1):
        gk = GAMMA * (1.0 - (1.0 if k == 1 else 0.0))
        A[k - 1, k - 1] += gk * (lam1 - 1.0)
        for j in range(1, N + 1):
            if j != k:
                m = np.exp(-((k - j) ** 2 + (j - 1) ** 2 + (1 - k) ** 2)
                           / (2 * 6.0 ** 2))
                A[k - 1, j - 1] += eps * m
    ev = np.linalg.eigvals(A)
    r["C_modal_drift"] = {
        "min_real_eigenvalue": float(ev.real.min()),
        "max_real_eigenvalue": float(ev.real.max()),
        "core_mode_intrinsic_decay_per_step": 0.0,
        "slowest_coupled_decay_per_step": float(-ev.real.min()),
        "slowest_coupled_t_half_steps": float(LN2 / -ev.real.min()),
    }

    # ---- D. dtau conversion / requirement table.
    c_cm = 2.99792458e10
    g_band_period = 1.0 / (c_cm * 1580.0)
    anchors = {
        "planck_time": 5.391e-44,
        "g_band_period_1580cm-1": g_band_period,
        "omega0_1.0e14_period": 2 * np.pi / 1.0e14,
        "omega0_1.4e14_period": 2 * np.pi / 1.4e14,
        "one_second": 1.0,
        "one_day": 86400.0,
        "one_year": YR_S,
    }
    r["D_conversion"] = {
        "t_half_years_if_dtau_is": {
            name: {"dtau_s": d, "t_half_yr": t_half_steps * d / YR_S}
            for name, d in anchors.items()},
        "required_dtau_s_for_stated_dephasing": {
            f"t_half_{t}yr": t * YR_S / t_half_steps for t in (800, 1600)},
        "required_coherence_decay_per_step_gband": {
            f"{t}yr": LN2 * g_band_period / (t * YR_S) for t in (800, 1600)},
    }

    # ---- E. Protected sector: leak rate sets t1/2 exactly.
    def slowest_decay(eps_leak):
        sz3 = np.diag([1.0, -1.0, 1.0])   # protected pair shares eigenvalue
        Ls = [np.sqrt(GAMMA) * sz3]
        leak = np.zeros((3, 3))
        leak[1, 2] = np.sqrt(eps_leak)
        Ls.append(leak)
        Id = np.eye(3)
        Ltot = np.zeros((9, 9), dtype=complex)
        for Lop in Ls:
            LdL = Lop.conj().T @ Lop
            Ltot += (np.kron(Lop, Lop.conj()) - 0.5 * np.kron(LdL, Id)
                     - 0.5 * np.kron(Id, LdL.T))
        evv = np.linalg.eigvals(Ltot)
        dec = sorted({round(float(-e.real), 15) for e in evv
                      if e.real < -1e-14})
        return dec[0] if dec else 0.0

    sweep = {}
    for e in (1e-2, 1e-6, 1e-10, 1e-12):
        sd = slowest_decay(e)
        sweep[f"eps_leak={e:g}"] = {
            "slowest_decay_per_step": sd,
            "t_half_steps": LN2 / sd if sd else None,
            "t_half_yr_at_gband_dtau": (LN2 / sd) * g_band_period / YR_S
            if sd else None,
        }
    r["E_protected_sector"] = {
        "sweep": sweep,
        "required_coherence_decay_per_step_for_800yr_at_gband_dtau":
            LN2 * g_band_period / (800 * YR_S),
        "mechanism": "protected coherence decays at eps_leak/2, so "
                     "t1/2 = 2 ln2 / eps_leak exactly (sweep-verified)",
    }

    # ---- F. The one physical rate stated in the manuscript.
    r["F_stated_physical_rate"] = {
        "Lambda_Eq1_instance_s-1": 0.12,
        "t_half_s": LN2 / 0.12,
        "orders_from_claim_rate": float(np.log10(0.12 / (g_hi / YR_S))),
    }
    r["_t_half_steps"] = t_half_steps
    r["_g_band_period"] = g_band_period
    return r


def run():
    r = compute()
    A, B, C, D, E, F = (r["A_memo_budget"], r["B_stated_dephasing"],
                        r["C_modal_drift"], r["D_conversion"],
                        r["E_protected_sector"], r["F_stated_physical_rate"])
    req_dtau_yr = (D["required_dtau_s_for_stated_dephasing"]["t_half_800yr"]
                   / YR_S)
    return [
        {
            "id": "X1",
            "test": "Memo's effective-rate conversion: t1/2 = 800-1600 yr "
                    "corresponds to Gamma_eff = 4.33e-4 - 8.66e-4 /yr "
                    "(1.37e-11 - 2.75e-11 /s)",
            "label": "REPRODUCTION",
            "published_result": "Gamma_eff = 4.33e-4 - 8.66e-4 yr^-1 "
                                "= 1.37e-11 - 2.75e-11 s^-1; illustrative "
                                "decomposition 7.5e-4 /yr -> t1/2 = 924 yr",
            "recomputed_result": {
                "gamma_eff_per_s": A["gamma_eff_per_s"],
                "illustrative_check_yr": A["illustrative_check_yr"],
            },
            "verdict": "AGREES" if A["agrees"] else "DIFFERS",
            "notes": "The memo's arithmetic is correct. Correct unit "
                     "conversion is not a derivation of the interval: the "
                     "Gamma range is computed FROM 800-1600 yr, and the "
                     "memo itself labels its component values illustrative.",
        },
        {
            "id": "X2",
            "test": "Lindblad computation from the manuscript's stated "
                    "decoherence operator L = sqrt(gamma) sigma_z, "
                    "gamma = 0.94 per recursion",
            "label": "DERIVATION-CHECK",
            "published_result": "Claim: the stated Lindblad framework "
                                "yields t1/2 ~ 800-1600 yr",
            "recomputed_result": {
                "liouvillian_eigenvalues_per_step":
                    [str(z) for z in B["liouvillian_eigenvalues"]],
                "slowest_decay_per_step": B["slowest_decay_per_step"],
                "t_half_steps": B["t_half_steps"],
                "t_half_yr_if_step_is_gband_period":
                    D["t_half_years_if_dtau_is"]
                     ["g_band_period_1580cm-1"]["t_half_yr"],
                "required_dtau_for_800yr_years_per_step": req_dtau_yr,
            },
            "verdict": "DIFFERS",
            "verdict_scope": "The stated operator yields t1/2 = 0.369 "
                             "recursion steps. Reaching 800 yr requires a "
                             "proper-time step of ~2,170 yr per recursion "
                             "(~4,340 yr for 1600 yr); at any step duration "
                             "the text suggests (phonon periods ~1e-14 s) "
                             "the half-life is ~1e-22 yr.",
        },
        {
            "id": "X3",
            "test": "Modal dynamics: does any stated mode supply the slow "
                    "decay? gamma_k = 0.94(1 - delta_k1), lambda_1 = 3.71, "
                    "c_kj = eps*m_kj, eps = 0.15",
            "label": "DERIVATION-CHECK",
            "published_result": "Modal framework with 94% damping of "
                                "non-core modes; core mode persistent",
            "recomputed_result": {
                "max_real_eigenvalue_per_step": C["max_real_eigenvalue"],
                "slowest_coupled_decay_per_step":
                    C["slowest_coupled_decay_per_step"],
                "slowest_coupled_t_half_steps":
                    C["slowest_coupled_t_half_steps"],
                "core_mode_intrinsic_decay_per_step":
                    C["core_mode_intrinsic_decay_per_step"],
            },
            "verdict": "DIFFERS",
            "verdict_scope": "The stated modal drift is growth-dominated "
                             "(max +3.10/step); the slowest decay anywhere "
                             "is 0.024/step (t1/2 ~ 29 steps), and the "
                             "core mode's intrinsic decay is exactly 0 by "
                             "the delta_k1 factor. No stated mode decays "
                             "anywhere near 1e-24/step.",
            "flags": [
                "Prose/equation tension: the text calls gamma_k a 'damping "
                "factor', but the printed modal equation enters it as "
                "+gamma_k (lambda_1 - 1), a growth term for k > 1. The "
                "audit used the equation as printed.",
                "omega_0 is stated as 1.0e14 rad/s in the constants table "
                "and 1.4e14 rad/s in the body text; immaterial at these "
                "orders of magnitude, recorded for the errata list.",
            ],
        },
        {
            "id": "X4",
            "test": "Protected-sector route: can Lindblad form (no signed "
                    "budget) produce the interval, and at what price?",
            "label": "DERIVATION-CHECK",
            "published_result": "Memo's budget ansatz: Gamma_eff = "
                                "Gamma_local + Gamma_leak + Gamma_branch "
                                "- Gamma_recurrence - Gamma_topological",
            "recomputed_result": {
                "mechanism": E["mechanism"],
                "sweep": E["sweep"],
                "required_coherence_decay_per_step_800yr_gband":
                    E["required_coherence_decay_per_step_for_800yr_at_"
                       "gband_dtau"],
                "implied_eps_leak_per_step": 2 * E[
                    "required_coherence_decay_per_step_for_800yr_at_"
                    "gband_dtau"],
                "only_physical_rate_stated": {
                    "Lambda_s-1": F["Lambda_Eq1_instance_s-1"],
                    "t_half_s": F["t_half_s"],
                    "orders_from_claim_rate": F["orders_from_claim_rate"],
                },
            },
            "verdict": "CANNOT BE DERIVED from stated parameters — "
                       "requirement identified",
            "verdict_scope": "A protected sector with a leak channel "
                             "yields arbitrarily long half-lives in strict "
                             "Lindblad form (t1/2 = 2 ln2/eps_leak, "
                             "sweep-verified), so the mechanism exists. "
                             "But the 800-yr claim is then exactly "
                             "equivalent to positing eps_leak ~ 1.2e-24 "
                             "per step (at a G-band-period step) — a "
                             "cancellation to ~3e-25 of the stated "
                             "dephasing rate. No parameter stated in the "
                             "manuscript fixes eps_leak or dtau at the "
                             "required values. This does not disprove the "
                             "interval; it converts it into one auditable "
                             "assumption.",
        },
    ]


if __name__ == "__main__":
    res = compute()
    res.pop("_t_half_steps", None)
    res.pop("_g_band_period", None)
    print(json.dumps(res, indent=2, default=str))
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "..", "results", "decoherence.json")
    with open(out, "w") as fh:
        json.dump(res, fh, indent=2, default=str)
    print("\nwrote", os.path.normpath(out))
