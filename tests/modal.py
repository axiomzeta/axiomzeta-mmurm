"""Group M — the N = 5 modal system + n = 8 ensemble. Label: CONSTRUCTION
(specification) + SIMULATION (statistics).

The author has not developed these layers; they are built here, and every
choice that is the builder's rather than the framework's is marked
[construction]. Nothing in this module is presented as the author's canon
or as empirical data.

Design decisions (see paper/MMURM_N5_modal.md for the full statement):
- Modes k = 1..5 (K = N). Frequencies omega_k = omega_0 / F_k with
  Fibonacci F = (1, 1, 2, 3, 5); only the ratios are used, since omega_0
  is stated as both 1.0 and 1.4e14 rad/s elsewhere (Group X flag).
  Damping gamma_k = 0.94 * (1 - delta_k1) as stated; core mode k = 1
  intrinsically undamped.
- The 5-branch modal matrix IS the 5x5 correlation matrix of modal
  amplitudes across the R = 8 realities. Its eigenvalues lam_k have
  trace 5; the modal weights w_k = lam_k / 5 sum to 1. This dissolves
  the legacy conflation (manuscript R3) by construction: on this branch
  the modal weight of mode 1 and its variance share are the same number,
  w_1 = lam_1 / 5, by definition.
- Two leading eigenvalues are kept distinct throughout:
  lam1_obs  = leading eigenvalue of the 5-observable correlation matrix
              (the E1 analogue at n = 8);
  lam1_mod  = leading eigenvalue of the 5-mode modal-amplitude
              correlation matrix (the Section 6.4 analogue at K = 5).
- The observable arm reuses the published target correlation matrix as
  a STATED ASSUMPTION (it is the only published correlation structure;
  nothing derives it for the 5-branch) via ensemble.generate_ensemble.
- lam1(5) is defined as an ENSEMBLE STATISTIC (median of a 1,000-draw
  simulation), not as a measurement. The single fixed-seed 8-reality
  dataset is one draw and is reported as one draw.
- Seed 20250922 throughout (simulation draws offset to avoid overlap
  with the single dataset's seed).
"""
import os

import numpy as np
import pandas as pd

import ensemble

SEED = 20250922
N_DRAWS = 1000
R5 = 8   # realities at N = 5
K5 = 5   # modes at N = 5
FIB = np.array([1, 1, 2, 3, 5], dtype=float)
GAMMA = 0.94 * (1.0 - np.eye(1, K5, 0).ravel())  # gamma_k, k = 1..5
GAMMA[0] = 0.0

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data")


def mp_edge(n, p):
    """Marchenko-Pastur upper edge (1 + sqrt(p/n))^2."""
    return (1.0 + np.sqrt(p / n)) ** 2


def eigs_of_corr(X):
    """Descending eigenvalues of the p x p correlation matrix of rows X."""
    corr = np.corrcoef(X, rowvar=False)
    eig = np.linalg.eigvalsh(corr)[::-1]
    assert abs(eig.sum() - X.shape[1]) < 1e-8, "correlation trace != p"
    return eig


def summarize(lam1):
    lam1 = np.asarray(lam1)
    return {
        "median": round(float(np.median(lam1)), 4),
        "mean": round(float(np.mean(lam1)), 4),
        "sd": round(float(np.std(lam1, ddof=1)), 4),
        "p5": round(float(np.percentile(lam1, 5)), 4),
        "p95": round(float(np.percentile(lam1, 95)), 4),
    }


def run(data_dir=DATA_DIR):
    entries = []
    edge = mp_edge(R5, K5)

    # ---- M1: modal system specification (ratios + damping) ----
    freq_ratios = [round(float(1.0 / f), 4) for f in FIB]
    entries.append({
        "id": "M1",
        "test": "N = 5 modal system: frequencies, damping, weight convention",
        "label": "CONSTRUCTION",
        "published_result": "Legacy (N = 12): 12 modes, omega_k = omega_0 / F_k, "
            "gamma_k = 0.94(1 - delta_k1), modal weights summing to 1 "
            "(printed 1.006), U_core = lam_1 = 3.71 [simulated]. No "
            "5-branch modal specification exists in the supplied material.",
        "recomputed_result": {
            "modes_K": K5,
            "fibonacci_F_k": [int(f) for f in FIB],
            "omega_k_over_omega_0": freq_ratios,
            "gamma_k": [round(float(g), 4) for g in GAMMA],
            "core_mode_k1_intrinsic_decay": 0.0,
            "modal_matrix_definition": "5x5 correlation matrix of modal "
                "amplitudes across the 8 realities; eigenvalues lam_k, "
                "trace 5; modal weights w_k = lam_k / 5, sum 1",
            "convention_note": "w_1 = lam_1 / 5 BY DEFINITION on this "
                "branch, so the legacy weight/variance conflation "
                "(manuscript R3) cannot recur",
        },
        "verdict": "SPECIFIED (construction)",
        "notes": ("Mode identities: only mode 1 carries a branch-invariant "
                  "meaning (core/fundamental resonance, by the gamma_1 = 0 "
                  "rule). The 12 legacy layer names are NOT mapped onto 5 "
                  "modes — no such rule is stated, and inventing one would "
                  "be fabrication. omega_0's dual stated value (1.0 vs "
                  "1.4e14 rad/s, Group X flag) is why only ratios are used."),
    })

    # ---- M2: encompassing matrix form ----
    entries.append({
        "id": "M2",
        "test": "Encompassing matrix U_env at N = 5 (form)",
        "label": "CONSTRUCTION",
        "published_result": "Legacy: (U_env)_ri = R_r . S_i, r, i = 1..22, "
            "Fibonacci diagonal dominance R_r . S_r proportional to F_r. "
            "No numerical entries are given even for the legacy matrix.",
        "recomputed_result": {
            "form": "(U_env)_ri = R_r . S_i, r, i = 1..8",
            "diagonal_dominance": "R_r . S_r proportional to F_r, "
                "F = (1, 1, 2, 3, 5, 8, 13, 21)",
            "numerical_entries": "UNSPECIFIED (as on the legacy branch)",
        },
        "verdict": "FORM CARRIED (numerics open)",
        "notes": ("The 8x8 form is carried, not numerically instantiated: "
                  "the reality amplitudes R_r and string modes S_i are "
                  "never numerically specified in the supplied material. "
                  "Any numeric U_env would be invention."),
    })

    # ---- M3: the n = 8 observable dataset + its simulation ----
    df8, _ = ensemble.generate_ensemble(R5, SEED)
    eig8 = eigs_of_corr(df8[ensemble.OBS].to_numpy())
    df8_path = os.path.join(data_dir, "modal8_observables.csv")
    df8.to_csv(df8_path, index=False)

    lam1_obs_draws = []
    eig_rows = []
    for d in range(N_DRAWS):
        dfd, _ = ensemble.generate_ensemble(R5, SEED + 10000 + d)
        eig = eigs_of_corr(dfd[ensemble.OBS].to_numpy())
        lam1_obs_draws.append(eig[0])
        eig_rows.append(("obs", d, *eig))
    obs_summary = summarize(lam1_obs_draws)
    obs_summary["frac_above_mp_edge"] = round(
        float(np.mean(np.asarray(lam1_obs_draws) > edge)), 4)
    entries.append({
        "id": "M3",
        "test": "n = 8 observable ensemble: lam1_obs(5) (E1 analogue)",
        "label": "SIMULATION",
        "published_result": "No 5-branch ensemble exists (instantiation "
            "doc Section 4). Legacy: lam_1 = 3.71 +/- 0.04 at n = 1,000 "
            "realities; reconstruction 3.659 at n = 22 (E1).",
        "recomputed_result": {
            "single_dataset": "data/modal8_observables.csv (8 realities, "
                "fixed seed 20250922, Gaussian copula targeting the "
                "published correlation matrix)",
            "single_dataset_eigenvalues": [round(float(v), 4) for v in eig8],
            "single_dataset_lam1_obs": round(float(eig8[0]), 4),
            "single_dataset_note": "ONE DRAW, not 'the' lam1(5)",
            "simulation_1000_draws_n8": obs_summary,
            "mp_edge_n8_p5": round(edge, 4),
            "lam1_obs_5_definition": "median of the 1,000-draw distribution",
        },
        "verdict": "SIMULATION",
        "notes": ("Target correlation matrix reused as a STATED ASSUMPTION: "
                  "it is the only published correlation structure, and "
                  "nothing derives it for the 5-branch. t_half's marginal "
                  "is carried as published; its null-status problem (Group "
                  "S/E) is unchanged. The single dataset's lam1 is one "
                  "draw of a wide distribution — see the p5/p95 spread."),
    })

    # ---- M4: modal-amplitude null ensemble ----
    rng = np.random.default_rng(SEED + 20000)
    amps_null = rng.standard_normal((N_DRAWS, R5, K5))
    lam1_null = []
    for d in range(N_DRAWS):
        eig = eigs_of_corr(amps_null[d])
        lam1_null.append(eig[0])
        eig_rows.append(("modal_null", d, *eig))
    null_summary = summarize(lam1_null)
    null_p95 = float(np.percentile(lam1_null, 95))
    null_summary["frac_above_mp_edge"] = round(
        float(np.mean(np.asarray(lam1_null) > edge)), 4)
    entries.append({
        "id": "M4",
        "test": "Modal-amplitude null ensemble: lam1_mod(5) under no coherence",
        "label": "SIMULATION",
        "published_result": "None: no modal-amplitude data exists on either "
            "branch. Legacy MP edge (p = 5, n = 22) = 2.18.",
        "recomputed_result": {
            "model": "8x5 i.i.d. standard normal amplitudes, 1,000 draws",
            "mp_edge_n8_p5": round(edge, 4),
            "null_distribution": null_summary,
            "operational_threshold_null_p95": round(null_p95, 4),
        },
        "verdict": "SIMULATION",
        "notes": ("Two bars, not one, and their order matters. For "
                  "correlation matrices the asymptotic MP edge sits ABOVE "
                  "the finite-sample null: only 0.6% of null draws exceed "
                  "3.21 at n = 8, and the null 95th percentile is 2.74. "
                  "The edge is therefore the stricter bar; the null p95 "
                  "is the operational bar. (Sanity check, independent "
                  "seed: white-noise correlation lam1 medians 2.15 / 1.63 "
                  "/ 1.28 / 1.12 at n = 8 / 22 / 100 / 500 against edges "
                  "3.21 / 2.18 / 1.50 / 1.21 — the null approaches the "
                  "edge from below as n grows. The edge is a covariance "
                  "asymptotic; the unit-diagonal constraint of a "
                  "correlation matrix shrinks the top eigenvalue.)"),
    })

    # ---- M5: one-factor sweep (structured modal coherence) ----
    sweep = []
    for a in (0.5, 0.7, 0.85):
        rng = np.random.default_rng(SEED + 30000 + int(a * 100))
        factor = rng.standard_normal((N_DRAWS, R5, 1))
        noise = rng.standard_normal((N_DRAWS, R5, K5))
        amps = a * factor + np.sqrt(1.0 - a * a) * noise
        lam1_s = []
        for d in range(N_DRAWS):
            eig = eigs_of_corr(amps[d])
            lam1_s.append(eig[0])
            eig_rows.append((f"modal_onefactor_a{a}", d, *eig))
        s = summarize(lam1_s)
        s["frac_above_mp_edge"] = round(
            float(np.mean(np.asarray(lam1_s) > edge)), 4)
        s["frac_above_null_p95"] = round(
            float(np.mean(np.asarray(lam1_s) > null_p95)), 4)
        sweep.append({
            "loading_a": a,
            "population_lam1": round(1.0 + (K5 - 1) * a * a, 4),
            "simulated": s,
        })
    entries.append({
        "id": "M5",
        "test": "One-factor modal coherence sweep: what clears the n = 8 bar?",
        "label": "SIMULATION",
        "published_result": "Legacy claim: a dominant modal core (weight "
            "0.780, U_core = 3.71) [simulated]. No loading parameter is "
            "stated anywhere in the supplied material.",
        "recomputed_result": {
            "model": "amplitude = a * common_factor + sqrt(1 - a^2) * noise; "
                "population lam1 = 1 + 4a^2",
            "sweep": sweep,
            "falsifiable_threshold": {
                "mp_edge_strict_bar": round(edge, 4),
                "null_p95_operational_bar": round(null_p95, 4),
                "statement": "A future empirical 8-reality x 5-mode dataset "
                    "with lam1_mod above the null 95th percentile (2.74) "
                    "exceeds the finite-sample random-matrix null at n = 8; "
                    "above the MP edge (3.21) it clears the stricter "
                    "asymptotic bar as well. Below 2.74, the modal "
                    "coherence claim has no support from that dataset.",
            },
        },
        "verdict": "SIMULATION",
        "notes": ("Loadings are SWEPT, not fitted: no loading is claimed, "
                  "so nothing here bakes in a desired lam1. Small-n "
                  "caveat, stated plainly: at n = 8, p = 5 the eigenvalue "
                  "distribution is wide (see M4 p5/p95), so this test is "
                  "weak — clearing the bar is necessary, not sufficient, "
                  "for the modal-coherence claim. An empirical 8x5 modal "
                  "dataset would upgrade M3/M4 from SIMULATION to "
                  "REPRODUCTION-style measurement; none exists."),
    })

    eig_df = pd.DataFrame(
        eig_rows, columns=["arm", "draw", "lam1", "lam2", "lam3", "lam4", "lam5"])
    eig_df.to_csv(os.path.join(data_dir, "modal_eigenvalues.csv"), index=False)
    artifacts = {"df8": df8, "eig_df": eig_df}
    return entries, artifacts


if __name__ == "__main__":
    ents, _ = run()
    for e in ents:
        print(e["id"], e["verdict"], e["test"][:60])
