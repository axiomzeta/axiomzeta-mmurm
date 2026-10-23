"""Counterpart figure set (PNG) for the MMURM Foundation re-analysis.

Every figure is generated from the same pipeline outputs as the numeric
results (published correlation matrix, fixed-seed RECONSTRUCTION ensemble,
bootstrap arrays, deviation table) — no separate data.
"""
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from ensemble import OBS, PUBLISHED_R

PRETTY = {
    "sin2_thetaW": r"$\sin^2\theta_W$",
    "DM_sigma": r"DM $\sigma$ ($10^{-47}$ cm$^2$)",
    "M_Amat": r"$M_{Amat}$ (GeV)",
    "t_half": r"$t_{half}$ (yr)",
    "rho_DE": r"$\rho_{DE}$ ($10^{-30}$ J/m$^3$)",
}
NULLS = {"sin2_thetaW": 0.2315, "DM_sigma": 1.0, "M_Amat": 140.0,
         "t_half": 1.0e10, "rho_DE": 6.5}


def make(outdir, df22, artifacts, s_results):
    os.makedirs(outdir, exist_ok=True)
    paths = []
    by_id = {r["id"]: r for r in s_results}

    # ---- (1) eigenvalue spectrum of the published matrix + MP edge -------
    eig = np.linalg.eigvalsh(PUBLISHED_R)[::-1]
    julius = [3.70, 0.80, 0.50, 0.30, 0.10]
    mp_edge = (1 + np.sqrt(5 / 22)) ** 2
    fig, ax = plt.subplots(figsize=(7.2, 4.2))
    x = np.arange(5)
    ax.bar(x - 0.2, eig, width=0.4, label="Recomputed from published matrix")
    ax.bar(x + 0.2, julius, width=0.4, label="Published (Julius) spectrum")
    ax.axhline(mp_edge, color="r", ls="--",
               label=f"Marchenko-Pastur edge (p=5, n=22) = {mp_edge:.2f}")
    ax.axhline(1.0, color="gray", ls=":", label="Document's plot line (1.0)")
    ax.set_xticks(x)
    ax.set_xticklabels([f"$\\lambda_{i+1}$" for i in x])
    ax.set_ylabel("Eigenvalue")
    ax.set_title("S1 — Eigenvalue spectrum of the published correlation matrix\n"
                 "Published spectrum sums to 5.40; a 5x5 correlation matrix "
                 "has trace exactly 5")
    ax.legend(fontsize=8)
    fig.tight_layout()
    p = os.path.join(outdir, "fig1_eigenvalue_spectrum.png")
    fig.savefig(p, dpi=150)
    plt.close(fig)
    paths.append(p)

    # ---- (2) PCA explained-variance bars ---------------------------------
    pca = artifacts["pca"]
    fig, ax = plt.subplots(figsize=(7.2, 4.2))
    ax.bar(x - 0.27, pca["published"], width=0.27, label="Published (Julius)")
    ax.bar(x, pca["covariance"], width=0.27,
           label="Recomputed: covariance PCA (natural units)")
    ax.bar(x + 0.27, pca["correlation"], width=0.27,
           label="Recomputed: correlation PCA")
    ax.set_xticks(x)
    ax.set_xticklabels([f"PC{i+1}" for i in x])
    ax.set_ylabel("Explained-variance ratio")
    ax.set_title("S2 — PCA explained variance (RECONSTRUCTION)\n"
                 "Covariance PCA in natural units is dominated by t_half "
                 "(PC1 ~= 1.0)")
    ax.legend(fontsize=8)
    fig.tight_layout()
    p = os.path.join(outdir, "fig2_pca_variance.png")
    fig.savefig(p, dpi=150)
    plt.close(fig)
    paths.append(p)

    # ---- (3) bootstrap correlation histogram ------------------------------
    boot = artifacts["bootstrap_r"]
    r_sample = artifacts["bootstrap_sample_r"]
    fig, ax = plt.subplots(figsize=(7.2, 4.2))
    ax.hist(boot, bins=30, color="#4477aa", alpha=0.85)
    ax.axvspan(0.05, 0.15, color="red", alpha=0.18,
               label="Published bootstrap 95% CI [0.05, 0.15]")
    ax.axvline(0.10, color="red", ls="--", label="Published mean r = 0.10")
    ax.axvline(r_sample, color="black", ls="-",
               label=f"Reconstruction sample r = {r_sample:.3f} "
                     f"(published matrix: 0.926)")
    ax.set_xlabel(r"Bootstrap correlation $\sin^2\theta_W$ vs $M_{Amat}$ (800 resamples)")
    ax.set_ylabel("Count")
    ax.set_title("S3 — Bootstrap correlation distribution (RECONSTRUCTION)\n"
                 "A bootstrap of matrix-consistent data cannot centre on 0.10")
    ax.legend(fontsize=8)
    fig.tight_layout()
    p = os.path.join(outdir, "fig3_bootstrap_histogram.png")
    fig.savefig(p, dpi=150)
    plt.close(fig)
    paths.append(p)

    # ---- (4) published correlation-matrix heatmap --------------------------
    fig, ax = plt.subplots(figsize=(6.4, 5.4))
    im = ax.imshow(PUBLISHED_R, vmin=-1, vmax=1, cmap="RdBu_r")
    ax.set_xticks(range(5))
    ax.set_yticks(range(5))
    ax.set_xticklabels([PRETTY[o] for o in OBS], fontsize=8, rotation=20, ha="left")
    ax.set_yticklabels([PRETTY[o] for o in OBS], fontsize=8)
    for i in range(5):
        for j in range(5):
            ax.text(j, i, f"{PUBLISHED_R[i, j]:.3f}", ha="center", va="center",
                    fontsize=8,
                    color="white" if abs(PUBLISHED_R[i, j]) > 0.55 else "black")
    fig.colorbar(im, ax=ax, shrink=0.85)
    ax.set_title("S4 — Published 5x5 correlation matrix (n = 22 realities)\n"
                 "Used verbatim as the reconstruction target")
    fig.tight_layout()
    p = os.path.join(outdir, "fig4_correlation_heatmap.png")
    fig.savefig(p, dpi=150)
    plt.close(fig)
    paths.append(p)

    # ---- (5) parameter distributions, reconstructed ensemble -------------
    fig, axes = plt.subplots(1, 5, figsize=(13.5, 3.4))
    for ax, name in zip(axes, OBS):
        vals = df22[name].to_numpy(dtype=float)
        ax.hist(vals, bins=10, color="#4477aa", alpha=0.85)
        ax.set_title(PRETTY[name], fontsize=9)
        if name == "t_half":
            ax.text(0.97, 0.93, "null > 1e10 yr\n(off scale)", transform=ax.transAxes,
                    ha="right", va="top", fontsize=7.5, color="red")
        else:
            ax.axvline(NULLS[name], color="red", ls="--", lw=1.4)
            ax.text(0.97, 0.93, f"null = {NULLS[name]:g}", transform=ax.transAxes,
                    ha="right", va="top", fontsize=7.5, color="red")
        ax.tick_params(labelsize=7.5)
    fig.suptitle("Reconstructed 22-reality ensemble — parameter distributions "
                 "with null values (RECONSTRUCTION, seed 20250922)", fontsize=10)
    fig.tight_layout(rect=[0, 0, 1, 0.92])
    p = os.path.join(outdir, "fig5_parameter_distributions.png")
    fig.savefig(p, dpi=150)
    plt.close(fig)
    paths.append(p)

    # ---- (6) S6 deviation-band chart --------------------------------------
    dev = artifacts["deviations"]
    fig, ax = plt.subplots(figsize=(7.6, 4.6))
    ax.axhspan(5.0, 7.5, color="orange", alpha=0.3,
               label="Published 'cascade ignition' band 5.0-7.5%")
    rng = np.random.default_rng(0)
    for k, name in enumerate(OBS):
        vals = np.abs(dev[name])
        xs = k + rng.uniform(-0.22, 0.22, size=len(vals))
        ax.scatter(xs, np.clip(vals, 0.01, None), s=22, alpha=0.8,
                   label=None)
        ax.annotate(f"max {vals.max():.1f}%", (k, vals.max()),
                    textcoords="offset points", xytext=(0, 6),
                    ha="center", fontsize=8)
    ax.set_yscale("log")
    ax.set_ylim(0.01, 1000)
    ax.set_xticks(range(5))
    ax.set_xticklabels([PRETTY[o] for o in OBS], fontsize=8.5)
    ax.set_ylabel("|deviation from null| (%)  [log scale]")
    ax.set_title("S6 — Per-reality deviations from the published nulls "
                 "(RECONSTRUCTION)\nNo sin2/M_Amat point can reach the band: "
                 "published ranges cap them at 2.8% / 2.9%")
    ax.legend(fontsize=8, loc="center right")
    fig.tight_layout()
    p = os.path.join(outdir, "fig6_deviation_band.png")
    fig.savefig(p, dpi=150)
    plt.close(fig)
    paths.append(p)

    return paths
