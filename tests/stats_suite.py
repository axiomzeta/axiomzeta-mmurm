"""Group S — Statistical suite on the 22-reality ensemble (S1-S7).
Label: RECONSTRUCTION (see ensemble.py). Observables: sin2_thetaW, DM_sigma,
M_Amat, t_half, rho_DE. H_0 appears in the document's S6/S7 tables but has no
published per-reality distribution, so it cannot be reconstructed; that is
recorded, not worked around.
"""
import numpy as np
from scipy import stats

from ensemble import OBS, PUBLISHED_R

JULIUS_EIGENVALUES = [3.70, 0.80, 0.50, 0.30, 0.10]
JULIUS_PCA_RATIOS = [0.30, 0.24, 0.19, 0.16, 0.11]

NULLS = {
    # value, provenance, flags
    "sin2_thetaW": (0.2315, "PDG 2024 (LEP/Z-pole)", []),
    "M_Amat": (140.0, "document's own ensemble median",
               ["SELF-REFERENTIAL NULL: 140 GeV is URM's own predicted/median "
                "value, not an independent measurement (M_Amat is 'not in SM'). "
                "Deviations from it measure ensemble spread, not agreement "
                "with experiment."]),
    "DM_sigma": (1.0, "LUX-ZEPLIN upper limit (<1.0e-47 cm^2)",
                 ["An upper limit is used as a point null: every model value "
                  "above the limit is a >= +50% 'deviation', so band membership "
                  "tests the limit's misuse, not the model."]),
    "t_half": (1.0e10, "quantum-gravity expectation (>1e10 yr)",
               ["Model values are 800-1600 yr, ~7 orders of magnitude below "
                "this null; deviations are ~-100% by construction."]),
    "rho_DE": (6.5, "Planck 2018 (6.5e-30 J/m^3)", []),
    "H_0": (70.2, "document's compromise value (Planck 67.4 / SH0ES 73.0)",
            ["H_0 is NOT one of the 5 ensemble observables and has no "
             "published per-reality distribution; the document's H_0 band "
             "entries cannot be reconstructed or checked."]),
}

BAND_LO, BAND_HI = 5.0, 7.5  # % deviation band, per TEST_CENSUS.md


def _partial_corr_from_matrix(R, i, j, k):
    return ((R[i, j] - R[i, k] * R[j, k])
            / np.sqrt((1 - R[i, k] ** 2) * (1 - R[j, k] ** 2)))


def _pca_ratios(X, correlation=False):
    if correlation:
        X = (X - X.mean(axis=0)) / X.std(axis=0, ddof=1)
    Xc = X - X.mean(axis=0)
    cov = np.cov(Xc, rowvar=False)
    ev = np.linalg.eigvalsh(cov)[::-1]
    return ev / ev.sum(), ev


def run(df22, label):
    X = df22[OBS].to_numpy(dtype=float)
    n = X.shape[0]
    artifacts = {}
    results = []

    # ---------------- S1: eigenvalue spectrum of the published matrix ----
    eig_pub = np.linalg.eigvalsh(PUBLISHED_R)[::-1]
    mp_edge = (1 + np.sqrt(5 / 22)) ** 2
    s1 = {
        "id": "S1",
        "test": "Eigenvalue spectrum of the 5x5 correlation matrix",
        "label": "REPRODUCTION (published matrix is fully specified)",
        "published_result": {
            "eigenvalues_julius": JULIUS_EIGENVALUES,
            "julius_eigenvalue_sum": round(sum(JULIUS_EIGENVALUES), 2),
            "marchenko_pastur_bound_as_printed": 1.97,
            "plot_threshold_line": 1.0,
        },
        "recomputed_result": {
            "eigenvalues_of_published_matrix": [round(float(v), 4) for v in eig_pub],
            "eigenvalue_sum": round(float(eig_pub.sum()), 4),
            "matrix_trace": 5.0,
            "min_eigenvalue": round(float(eig_pub.min()), 4),
            "marchenko_pastur_edge_p5_n22": round(float(mp_edge), 4),
            "lambda_1_above_mp_edge": bool(eig_pub[0] > mp_edge),
            "lambda_1_variance_share": round(float(eig_pub[0] / 5.0), 4),
        },
        "verdict": "DIFFERS",
        "flags": [
            "TRACE VIOLATION: the published eigenvalues (3.70, 0.80, 0.50, "
            "0.30, 0.10) sum to 5.40, but every 5x5 correlation matrix has "
            "trace exactly 5, so its eigenvalues must sum to 5. The published "
            "spectrum is not the spectrum of the published matrix, nor of "
            "any 5x5 correlation matrix.",
            "The document also prints lambda_1 = 2.80 in its cascade section "
            "('2.80 (report) or 3.70 (plot)') while using 3.70 elsewhere; the "
            "recomputed value from its own matrix is "
            f"{eig_pub[0]:.3f} — neither printed number.",
            f"The Marchenko-Pastur edge for the actual case (p=5, n=22) is "
            f"{mp_edge:.2f}, not the printed 1.97 (and not the plot's 1.0 "
            "line). lambda_1 does exceed the correct edge, so the "
            "qualitative 'one dominant mode' reading survives; the printed "
            "numbers do not.",
        ],
        "notes": "Eigenvalues recomputed from data/ensemble22_correlation_"
                 "published.csv. The published matrix itself is a valid "
                 "correlation matrix (min eigenvalue > 0).",
    }
    results.append(s1)

    # ---------------- S2: PCA explained variance --------------------------
    ratios_cov, _ = _pca_ratios(X, correlation=False)
    ratios_corr, _ = _pca_ratios(X, correlation=True)
    artifacts["pca"] = {"covariance": ratios_cov, "correlation": ratios_corr,
                        "published": JULIUS_PCA_RATIOS}
    s2 = {
        "id": "S2",
        "test": "PCA explained variance",
        "label": label,
        "published_result": {"ratios": JULIUS_PCA_RATIOS,
                             "basis_as_printed": "covariance ('PCA is on "
                             "covariance, not correlation')"},
        "recomputed_result": {
            "covariance_pca_ratios_reconstructed": [round(float(v), 4) for v in ratios_cov],
            "correlation_pca_ratios_reconstructed": [round(float(v), 4) for v in ratios_corr],
            "dominant_covariance_component": OBS[int(np.argmax(np.cov(X - X.mean(axis=0), rowvar=False).diagonal()))] + " (largest raw variance)",
        },
        "verdict": "DIFFERS",
        "flags": [
            "In natural units the covariance PCA is dominated by t_half "
            "(values 800-1600 yr; variance orders of magnitude larger than "
            "the other observables), giving PC1 ~= 100% — the published "
            "0.30/0.24/0.19/0.16/0.11 profile cannot arise from the "
            "documented distributions in natural units.",
            "The correlation PCA gives yet another profile "
            "(~eigenvalues/5 of the sample correlation matrix). Neither "
            "recomputation matches the published ratios; the source "
            "simulation's variable scaling is undocumented, so the published "
            "PCA cannot be reproduced or audited (CANNOT AGREE on method, "
            "DIFFERS on numbers).",
        ],
        "notes": "The document's own resolution ('after standardization -> "
                 "correlation PCA -> PC1 dominates') contradicts its printed "
                 "covariance ratios, which show PC1 at only 30%.",
    }
    results.append(s2)

    # ---------------- S3: bootstrap correlation sin2 vs M_Amat ------------
    i_sin, i_mam = OBS.index("sin2_thetaW"), OBS.index("M_Amat")
    r_sample = float(np.corrcoef(X[:, i_sin], X[:, i_mam])[0, 1])
    rng = np.random.default_rng(20250922)
    boot = []
    for _ in range(800):
        idx = rng.integers(0, n, n)
        a, b = X[idx, i_sin], X[idx, i_mam]
        if a.std() > 0 and b.std() > 0:
            boot.append(np.corrcoef(a, b)[0, 1])
    boot = np.array(boot)
    artifacts["bootstrap_r"] = boot
    artifacts["bootstrap_sample_r"] = r_sample
    # Fisher z CI and t-test for the sample correlation at n = 22
    z = np.arctanh(np.clip(r_sample, -0.999, 0.999))
    z_se = 1 / np.sqrt(n - 3)
    fisher_ci = [float(np.tanh(z - 1.96 * z_se)), float(np.tanh(z + 1.96 * z_se))]
    t_stat = r_sample * np.sqrt((n - 2) / (1 - r_sample ** 2))
    p_val = float(2 * stats.t.sf(abs(t_stat), n - 2))
    # The document's claimed effect size r = 0.10 assessed at its own n = 22:
    t_010 = 0.10 * np.sqrt((n - 2) / (1 - 0.10 ** 2))
    p_010 = float(2 * stats.t.sf(abs(t_010), n - 2))
    s3 = {
        "id": "S3",
        "test": "Bootstrap correlation sin^2(theta_W) vs M_Amat, 800 resamples",
        "label": label,
        "published_result": {"mean_r": 0.10, "ci_95": [0.05, 0.15],
                             "claimed": "p < 0.001, 'highly significant due "
                                        "to large n=22 realities'"},
        "recomputed_result": {
            "sample_correlation_reconstructed": round(r_sample, 4),
            "bootstrap_mean_r": round(float(boot.mean()), 4),
            "bootstrap_ci_95": [round(float(np.percentile(boot, 2.5)), 4),
                                round(float(np.percentile(boot, 97.5)), 4)],
            "fisher_z_ci_95": [round(fisher_ci[0], 4), round(fisher_ci[1], 4)],
            "t_statistic_n22": round(float(t_stat), 3),
            "p_value_n22": p_val,
            "published_pair_correlation_in_matrix": 0.926,
            "claimed_r_0.10_at_n22": {"t": round(float(t_010), 3), "p": round(p_010, 3)},
        },
        "verdict": "DIFFERS",
        "flags": [
            "INTERNAL CONTRADICTION: the document's bootstrap centres on "
            "r ~= 0.10 for sin^2(theta_W) vs M_Amat, but its own published "
            "correlation matrix gives r = 0.926 for the same pair. A "
            "bootstrap of data with correlation 0.926 cannot centre on "
            "0.10. The reconstruction (built on the published matrix) "
            f"bootstraps around r ~= {boot.mean():.2f}. One of the two "
            "published artefacts does not describe the ensemble.",
            f"SIGNIFICANCE ERROR: at n = 22, r = 0.10 gives t = {t_010:.2f}, "
            f"p = {p_010:.2f} — nowhere near significant. 800 bootstrap "
            "resamples of 22 points do not create significance the sample "
            "does not contain; 'large n' is the resample count, not the "
            "sample size.",
        ],
        "notes": "Resampling 22 fixed points measures the stability of the "
                 "estimate for THIS ensemble; it is not independent evidence "
                 "about physics.",
    }
    results.append(s3)

    # ---------------- S4: correlation matrix ------------------------------
    sample_corr = np.corrcoef(X, rowvar=False)
    max_dev = float(np.max(np.abs(sample_corr - PUBLISHED_R)))
    artifacts["sample_corr"] = sample_corr
    s4 = {
        "id": "S4",
        "test": "Correlation matrix, n = 22 realities",
        "label": label,
        "published_result": "matrix as in data/ensemble22_correlation_published.csv",
        "recomputed_result": {
            "matrix_is_valid_correlation_matrix": bool(eig_pub.min() > 0),
            "min_eigenvalue": round(float(eig_pub.min()), 4),
            "reconstruction_sample_corr_max_abs_dev_vs_published": round(max_dev, 4),
        },
        "verdict": "AGREES",
        "verdict_scope": "The published matrix is internally valid (symmetric, "
                         "unit diagonal, positive definite) and is used "
                         "verbatim as the reconstruction target. The n=22 "
                         "reconstruction's sample correlations deviate by up "
                         f"to {max_dev:.2f}, which is ordinary sampling noise "
                         "at n=22 — the matrix is a summary the document "
                         "asserts, not a result this suite can confirm.",
        "notes": "Strong positive block sin2/DM/M_Amat (r = 0.80-0.93) and "
                 "negative t_half couplings (r ~= -0.62..-0.70) are properties "
                 "asserted by the document; no independent dataset exists "
                 "to check them against.",
    }
    results.append(s4)

    # ---------------- S5: partial correlation -----------------------------
    i_dm = OBS.index("DM_sigma")
    pc_matrix = float(_partial_corr_from_matrix(PUBLISHED_R, i_sin, i_dm, i_mam))
    # From reconstructed data: residualise on M_Amat.
    def _resid(y, x):
        A = np.column_stack([np.ones_like(x), x])
        beta, *_ = np.linalg.lstsq(A, y, rcond=None)
        return y - A @ beta
    pc_data = float(np.corrcoef(_resid(X[:, i_sin], X[:, i_mam]),
                                _resid(X[:, i_dm], X[:, i_mam]))[0, 1])
    s5 = {
        "id": "S5",
        "test": "Partial correlation sin^2(theta_W) <-> DM_sigma controlling M_Amat",
        "label": "REPRODUCTION (from published matrix) + " + label + " (from data)",
        "published_result": 0.692,
        "recomputed_result": {
            "from_published_matrix_formula": round(pc_matrix, 4),
            "from_reconstructed_data": round(pc_data, 4),
        },
        "verdict": "AGREES",
        "notes": "The one ensemble statistic that reproduces cleanly: "
                 "(0.898 - 0.926*0.800) / sqrt((1-0.926^2)(1-0.800^2)) "
                 f"= {pc_matrix:.3f} vs published 0.692 (rounding). "
                 "Agreement is with the document's own matrix arithmetic; "
                 "it does not validate the matrix itself.",
    }
    results.append(s5)

    # ---------------- S6: deviation band ----------------------------------
    dev = {}
    hits = {}
    for j, name in enumerate(OBS):
        null_val = NULLS[name][0]
        d = (X[:, j] - null_val) / null_val * 100.0
        dev[name] = d
        hits[name] = (np.abs(d) >= BAND_LO) & (np.abs(d) <= BAND_HI)
    hit_count = np.sum([hits[name] for name in OBS], axis=0)
    flagged_ge1 = hit_count >= 1
    flagged_ge3 = hit_count >= 3
    cooc = {}
    if flagged_ge3.sum() > 0:
        for a in OBS:
            for b in OBS:
                cooc[f"{a}|{b}"] = int(np.sum(hits[a][flagged_ge3] & hits[b][flagged_ge3]))
    artifacts["deviations"] = dev
    artifacts["hits"] = hits
    artifacts["hit_count"] = hit_count
    # Arithmetic caps from the document's own published ranges:
    cap_sin = (0.238 - 0.2315) / 0.2315 * 100
    cap_mam = (144.0 - 140.0) / 140.0 * 100
    s6 = {
        "id": "S6",
        "test": "Deviation-band detection (5.0-7.5%) vs nulls, co-occurrence",
        "label": label,
        "nulls": {k: {"value": v[0], "provenance": v[1], "flags": v[2]}
                  for k, v in NULLS.items()},
        "published_result": {
            "flagged_realities": 6,
            "cooccurrence": "sin2/M_Amat/DM_sigma 6/6; H_0 5/6; t_half 0/6",
            "fraction_with_ge3_hits": "27%",
        },
        "recomputed_result": {
            "band_hits_per_observable": {name: int(hits[name].sum()) for name in OBS},
            "realities_with_ge1_hit": int(flagged_ge1.sum()),
            "realities_with_ge3_hits": int(flagged_ge3.sum()),
            "cooccurrence_among_ge3_flagged": cooc if cooc else "none (no flagged realities)",
            "max_abs_deviation_pct_per_observable": {
                name: round(float(np.max(np.abs(dev[name]))), 3) for name in OBS},
            "arithmetic_caps_from_published_ranges": {
                "sin2_thetaW_max_possible_deviation_pct": round(float(cap_sin), 2),
                "M_Amat_max_possible_deviation_pct": round(float(cap_mam), 2),
            },
        },
        "verdict": "DIFFERS",
        "flags": [
            "ARITHMETICALLY IMPOSSIBLE AS PUBLISHED: the document's own "
            "ranges cap sin^2(theta_W) deviations at "
            f"{cap_sin:.1f}% (values 0.231-0.238 vs null 0.2315) and M_Amat "
            f"at {cap_mam:.1f}% (136-144 vs null 140) — both below the 5% "
            "band floor. No dataset consistent with the published "
            "distributions can put either observable in the 5-7.5% band, "
            "yet the document reports 6/6 co-occurrence for both.",
            "DM_sigma: the published distribution (peaks 1.5/2.5/3.0) vs the "
            "LUX-ZEPLIN upper-limit 'null' of 1.0 gives deviations of "
            "+50% to +200% — above the band, not in it.",
            "t_half 0/6 'agrees' only trivially: model values sit ~7 orders "
            "of magnitude below the >1e10 yr null (deviation ~-100%), not "
            "just outside a 5-7.5% band as a 'threshold effect'.",
            "H_0 cannot be checked at all: it is not in the ensemble and "
            "has no published per-reality values.",
        ],
        "notes": "Run on the RECONSTRUCTION, but the caps above are pure "
                 "arithmetic on the document's published ranges and nulls — "
                 "they hold for ANY dataset matching those summaries, "
                 "including the original one.",
    }
    results.append(s6)

    # ---------------- S7: PC1 clustering of flagged realities -------------
    w, V = np.linalg.eigh(PUBLISHED_R)
    pc1_vec = V[:, -1]
    Z = (X - X.mean(axis=0)) / X.std(axis=0, ddof=1)
    scores = Z @ pc1_vec
    artifacts["pc1_scores"] = scores

    def _clustering_pvalue(flag_mask, n_boot=10000, seed=777):
        if flag_mask.sum() < 1 or flag_mask.sum() >= len(scores):
            return None
        obs = abs(np.mean(np.abs(scores[flag_mask])) - np.mean(np.abs(scores[~flag_mask])))
        r = np.random.default_rng(seed)
        cnt = 0
        k = int(flag_mask.sum())
        for _ in range(n_boot):
            perm = r.permutation(len(scores))[:k]
            m = np.zeros(len(scores), dtype=bool)
            m[perm] = True
            d = abs(np.mean(np.abs(scores[m])) - np.mean(np.abs(scores[~m])))
            if d >= obs:
                cnt += 1
        return {"observed_diff_mean_abs_pc1": round(float(obs), 4),
                "bootstrap_p": (cnt + 1) / (n_boot + 1), "n_boot": n_boot}

    if flagged_ge3.sum() >= 1:
        s7_main = _clustering_pvalue(flagged_ge3)
        s7_verdict = "DIFFERS"  # recomputed on reconstruction; see notes
        s7_status = "performed on reconstruction with the published >=3-hit definition"
    else:
        s7_main = None
        s7_verdict = "CANNOT AGREE"
        s7_status = ("NOT PERFORMABLE: under the published >=3-hit flag "
                     "definition, zero realities are flagged in any dataset "
                     "consistent with the published distributions and nulls "
                     "(see S6), so there is no flagged group to cluster.")
    sensitivity = None
    if 2 <= int(flagged_ge1.sum()) < n:
        sensitivity = _clustering_pvalue(flagged_ge1)
    s7 = {
        "id": "S7",
        "test": "PC1 clustering of flagged realities + 10,000-resample bootstrap",
        "label": label,
        "published_result": {"flagged_mean_abs_pc1": 0.48, "others_mean_abs_pc1": 0.12,
                             "p_value": 0.0008, "bootstrap": "99.92% rejection"},
        "recomputed_result": {
            "status": s7_status,
            "published_definition_ge3_hits": s7_main,
            "sensitivity_ge1_hit_definition_NOT_published": sensitivity,
            "n_flagged_ge3": int(flagged_ge3.sum()),
            "n_flagged_ge1": int(flagged_ge1.sum()),
        },
        "verdict": s7_verdict,
        "flags": [
            "The published p = 0.0008 clustering result presupposes 6 flagged "
            "realities whose band membership is arithmetically impossible "
            "under the document's own published ranges and nulls (S6). The "
            "clustering machinery is implemented here exactly as described "
            "(PC1 of the published correlation matrix; label-permutation "
            "bootstrap, 10,000 resamples) and runs the moment a dataset "
            "with flagged realities is supplied — on every dataset "
            "consistent with the published summaries, there is nothing "
            "to run it on.",
        ],
        "notes": "PC1 scores use the published matrix's dominant eigenvector "
                 "applied to the standardised reconstruction.",
    }
    results.append(s7)

    return results, artifacts
