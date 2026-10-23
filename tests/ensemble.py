"""Ensemble reconstruction + Group E (E1). Label: RECONSTRUCTION.

The Foundation document publishes a 5x5 correlation matrix and verbal
distribution summaries for its 22 'realities', but not the raw dataset.
The dataset is therefore REGENERATED here: a Gaussian copula targeting the
published correlation matrix, with marginals matching the published
summaries, under a fixed seed. Every output of this module is a
RECONSTRUCTION, not the original data. If the original dataset is supplied
at data/ensemble22_original.csv it is used instead and the label upgrades
to REPRODUCTION (see load_reconstruction).
"""
import os

import numpy as np
import pandas as pd
from scipy import stats

OBS = ["sin2_thetaW", "DM_sigma", "M_Amat", "t_half", "rho_DE"]
SEED = 20250922

PUBLISHED_R = np.array([
    [1.000, 0.898, 0.926, -0.701, 0.456],
    [0.898, 1.000, 0.800, -0.623, 0.512],
    [0.926, 0.800, 1.000, -0.689, 0.478],
    [-0.701, -0.623, -0.689, 1.000, -0.334],
    [0.456, 0.512, 0.478, -0.334, 1.000],
])

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data")


def nearest_correlation(R, eps=1e-10, max_iter=200):
    """Higham-style nearest correlation matrix (alternating projections,
    simplified): eigenvalue clipping + unit-diagonal renormalisation."""
    Y = R.copy()
    for _ in range(max_iter):
        w, V = np.linalg.eigh(Y)
        w = np.clip(w, eps, None)
        Y = (V * w) @ V.T
        d = np.sqrt(np.diag(Y))
        Y = Y / np.outer(d, d)
        np.fill_diagonal(Y, 1.0)
        if np.linalg.eigvalsh(Y).min() > 0:
            break
    return Y


# ---- marginal quantile functions, per the document's published summaries ----
def _ppf_sin2(u):
    # "tight ~0.231-0.238", peaked near 0.231-0.235
    a = (0.231 - 0.2345) / 0.0016
    b = (0.238 - 0.2345) / 0.0016
    return stats.truncnorm.ppf(u, a, b, loc=0.2345, scale=0.0016)


_DM_GRID = None


def _ppf_dm(u):
    # "multimodal: peaks at 1.5, 2.5, 3.0" (x1e-47 cm^2)
    global _DM_GRID
    if _DM_GRID is None:
        x = np.linspace(0.05, 4.6, 200001)
        pdf = (0.34 * stats.norm.pdf(x, 1.5, 0.28)
               + 0.33 * stats.norm.pdf(x, 2.5, 0.28)
               + 0.33 * stats.norm.pdf(x, 3.0, 0.28))
        cdf = np.concatenate([[0.0], np.cumsum(0.5 * (pdf[1:] + pdf[:-1]) * np.diff(x))])
        cdf /= cdf[-1]
        _DM_GRID = (x, cdf)
    x, cdf = _DM_GRID
    return np.interp(u, cdf, x)


def _ppf_mamat(u):
    # "broad, 136-144 GeV", centred on the predicted 140
    a = (136.0 - 140.0) / 2.3
    b = (144.0 - 140.0) / 2.3
    return stats.truncnorm.ppf(u, a, b, loc=140.0, scale=2.3)


def _ppf_thalf(u):
    # "800-1600 yr, left-skewed" (mass near the top, tail to low values)
    return 800.0 + 800.0 * stats.beta.ppf(u, 5.0, 2.0)


def _ppf_rhode(u):
    # "sharp at ~6.5" (x1e-30 J/m^3)
    return stats.norm.ppf(u, loc=6.5, scale=0.12)


PPFS = [_ppf_sin2, _ppf_dm, _ppf_mamat, _ppf_thalf, _ppf_rhode]


def generate_ensemble(n, seed, target_R=PUBLISHED_R):
    """Gaussian copula: latent MVN(0, R) -> uniforms -> published marginals."""
    min_eig = float(np.linalg.eigvalsh(target_R).min())
    psd_adjusted = False
    R_used = target_R
    if min_eig <= 0:
        R_used = nearest_correlation(target_R)
        psd_adjusted = True
    rng = np.random.default_rng(seed)
    W = rng.multivariate_normal(np.zeros(len(OBS)), R_used, size=n)
    U = stats.norm.cdf(W)
    U = np.clip(U, 1e-10, 1 - 1e-10)
    X = np.column_stack([PPFS[j](U[:, j]) for j in range(len(OBS))])
    df = pd.DataFrame(X, columns=OBS)
    df.insert(0, "reality", [f"R{i+1}" for i in range(n)])
    meta = {
        "target_min_eigenvalue": min_eig,
        "psd_adjusted": psd_adjusted,
        "n": n,
        "seed": seed,
    }
    return df, meta


def load_reconstruction():
    """Return (df22, label, meta). Uses the drop-in original data file if
    present, else the fixed-seed copula reconstruction (n=22)."""
    orig = os.path.join(DATA_DIR, "ensemble22_original.csv")
    if os.path.exists(orig):
        df = pd.read_csv(orig)
        return df, "REPRODUCTION", {"source": "data/ensemble22_original.csv (drop-in original data)"}
    df, meta = generate_ensemble(22, SEED)
    meta["source"] = ("Gaussian copula reconstruction from the published "
                      "correlation matrix + published marginal summaries, "
                      f"seed {SEED}")
    return df, "RECONSTRUCTION", meta


def run(data_dir=DATA_DIR):
    """Write the reconstructed 22-reality CSV and compute E1 on a
    1,000-reality ensemble generated with the same copula."""
    df22, label, meta22 = load_reconstruction()
    recon_path = os.path.join(data_dir, "ensemble22_reconstructed.csv")
    df22.to_csv(recon_path, index=False)

    df1000, meta1000 = generate_ensemble(1000, SEED)
    X = df1000[OBS].to_numpy()
    corr = np.corrcoef(X, rowvar=False)
    eigvals = np.linalg.eigvalsh(corr)[::-1]
    lam1 = float(eigvals[0])
    share = lam1 / 5.0

    # Reference ('measured') reality: sin2 = 0.2315 (PDG), DM_sigma = 2.5
    # (mid-peak of the published multimodal distribution), M_Amat = 140
    # (published prediction), rho_DE = 6.5 (Planck). t_half is EXCLUDED from
    # the distance: the model puts t_half at 800-1600 yr while the only
    # published reference is a >1e10 yr expectation ~7 orders of magnitude
    # away, so there is no measured t_half value to locate a reality by.
    ref_cols = ["sin2_thetaW", "DM_sigma", "M_Amat", "rho_DE"]
    ref_vec = np.array([0.2315, 2.5, 140.0, 6.5])
    ref_mean = df1000[ref_cols].mean().to_numpy()
    ref_std = df1000[ref_cols].std(ddof=1).to_numpy()
    Z = (df1000[ref_cols].to_numpy() - ref_mean) / ref_std
    zref = (ref_vec - ref_mean) / ref_std
    dist = np.linalg.norm(Z - zref, axis=1)
    nearest_idx = int(np.argmin(dist))

    # PC1 scores from the ensemble correlation matrix.
    w, V = np.linalg.eigh(corr)
    pc1 = V[:, -1]
    Z5 = (X - X.mean(axis=0)) / X.std(axis=0, ddof=1)
    scores = Z5 @ pc1
    if np.corrcoef(scores, Z5.sum(axis=1))[0, 1] < 0:
        pc1 = -pc1
        scores = -scores
    pct = float(stats.percentileofscore(scores, scores[nearest_idx], kind="rank"))

    lam_ok = abs(lam1 - 3.71) <= 0.04
    share_ok = abs(share - 0.78) <= 0.02
    pct_ok = abs(pct - 49.8) <= 3.0
    verdict = "AGREES" if (lam_ok and share_ok and pct_ok) else "DIFFERS"
    diffs = []
    if not lam_ok:
        diffs.append(f"lambda_1 = {lam1:.3f}, outside the published 3.71 +/- 0.04")
    if not share_ok:
        diffs.append(f"dominant-mode variance share = {share:.1%}, not 78% "
                     f"(note: even the published lambda_1 = 3.71 gives "
                     f"3.71/5 = 74.2%, not 78%; the 78% figure matches the "
                     f"separate 12-layer modal decomposition in Draft-C, "
                     f"not this 5-observable correlation matrix)")
    if not pct_ok:
        diffs.append(f"reference-reality PC1 percentile = {pct:.1f}, not 49.8")

    e1 = {
        "id": "E1",
        "test": "URM full ensemble, N = 1,000 realities",
        "label": label,
        "published_result": "lambda_1 = 3.71 +/- 0.04; dominant mode = 78% of "
                            "cross-observable variance; reference reality at "
                            "49.8th percentile (seed 'URM-22 + R3 (2025 data)')",
        "recomputed_result": {
            "lambda_1_correlation_matrix": round(lam1, 4),
            "eigenvalues": [round(float(v), 4) for v in eigvals],
            "dominant_mode_variance_share": round(share, 4),
            "reference_reality_index": f"R{nearest_idx + 1}",
            "reference_reality_pc1_percentile": round(pct, 2),
            "reference_vector": dict(zip(ref_cols, ref_vec.tolist())),
            "t_half_excluded_from_distance_because": (
                "model t_half = 800-1600 yr vs the only published reference "
                ">1e10 yr (quantum-gravity expectation): no measured t_half "
                "exists to locate a reality by, and including it would make "
                "the distance a pure t_half mismatch counter"),
        },
        "verdict": verdict,
        "notes": ("Ensemble is a RECONSTRUCTION (same copula as the 22-reality "
                  "set, seed 20250922); the document's seed string 'URM-22 + R3' "
                  "is not a reproducible seed. Differences: " + "; ".join(diffs)
                  if diffs else "All three headline quantities reproduce."),
    }
    artifacts = {"df22": df22, "df1000": df1000, "label": label, "meta22": meta22}
    return [e1], artifacts
