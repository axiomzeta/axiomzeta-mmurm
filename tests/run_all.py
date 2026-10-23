"""Run the full MMURM Foundation re-analysis suite.

    .venv/bin/python tests/run_all.py

Writes results/results.json and results/RESULTS.md, plus the figure set in
results/figures/. Groups D and L are REPRODUCTION; groups S and E are
RECONSTRUCTION from the published summaries under seed 20250922 (see
ensemble.py). Group C is SYMBOLIC and Group R is a PROTOCOL registry: both
are recorded from TEST_CENSUS.md / data/claims_registry.json, not re-run.
"""
import json
import os
import sys
from datetime import date

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

import dimensional          # noqa: E402
import ensemble             # noqa: E402
import figures              # noqa: E402
import lhc_compare          # noqa: E402
import stats_suite          # noqa: E402

RESULTS_DIR = os.path.join(ROOT, "results")


def clean(obj):
    """Convert numpy scalars/containers to plain JSON types."""
    import numpy as np
    if isinstance(obj, dict):
        return {k: clean(v) for k, v in obj.items()}
    if isinstance(obj, (list, tuple)):
        return [clean(v) for v in obj]
    if isinstance(obj, (np.integer,)):
        return int(obj)
    if isinstance(obj, (np.floating,)):
        return float(obj)
    if isinstance(obj, (np.bool_,)):
        return bool(obj)
    return obj


GROUP_C = [
    {"id": f"C{i+1}", "test": name, "label": "SYMBOLIC",
     "published_result": status, "recomputed_result": "Not re-performed: "
     "structural/Noether audit item per TEST_CENSUS.md; no script output is "
     "presented as a proof.",
     "verdict": "RECORDED (not re-run)"}
    for i, (name, status) in enumerate([
        ("Energy-Momentum conservation", "PASS (conserved globally)"),
        ("Angular Momentum conservation", "PASS (conserved per universe)"),
        ("Charge conservation", "PASS (conserved absolutely)"),
        ("Baryon Number conservation", "REQUIRES REVIEW (conserved in recursion)"),
        ("Lepton Number conservation", "REQUIRES REVIEW (conserved in recursion)"),
        ("CPT symmetry", "PASS (preserved in multiverse)"),
    ])
]


def fmt(val, indent=0):
    if isinstance(val, dict):
        return "\n".join(f"{' ' * indent}- {k}: {fmt(v, indent + 2)}"
                         for k, v in val.items())
    if isinstance(val, list):
        if val and all(not isinstance(v, (dict, list)) for v in val):
            return ", ".join(str(v) for v in val)
        return "\n".join(f"{' ' * indent}- {fmt(v, indent + 2)}" for v in val)
    return str(val)


def entry_md(e):
    lines = [f"### {e['id']} — {e.get('test', '')}", ""]
    lines.append(f"- **Label:** {e.get('label', '')}")
    lines.append(f"- **Published:** {fmt(e.get('published_result'))}")
    lines.append(f"- **Recomputed:** {fmt(e.get('recomputed_result'))}")
    lines.append(f"- **Verdict: {e.get('verdict', '')}**")
    if e.get("verdict_scope"):
        lines.append(f"- Scope: {e['verdict_scope']}")
    for f in e.get("flags", []) or []:
        lines.append(f"- ⚠️ {f}")
    if e.get("notes"):
        lines.append(f"- Notes: {e['notes']}")
    if e.get("spot_check"):
        sc = e["spot_check"]
        lines.append(f"- Spot check: {sc['reference']} → URM value deviates "
                     f"{sc['urm_vs_reference_deviation_pct']}% "
                     f"({sc['urm_vs_reference_pull_sigma']} sigma). {sc['finding']}")
    lines.append("")
    return "\n".join(lines)


def main():
    os.makedirs(RESULTS_DIR, exist_ok=True)

    d_results = dimensional.run()
    l_results = lhc_compare.run()
    e_results, art_e = ensemble.run()
    s_results, art_s = stats_suite.run(art_e["df22"], art_e["label"])

    fig_dir = os.path.join(RESULTS_DIR, "figures")
    fig_paths = figures.make(fig_dir, art_e["df22"], art_s, s_results)
    fig_names = [os.path.basename(p) for p in fig_paths]

    with open(os.path.join(ROOT, "data", "claims_registry.json")) as fh:
        claims = json.load(fh)

    all_flags = []
    for group in (l_results, s_results, e_results):
        for e in group:
            for f in e.get("flags", []) or []:
                all_flags.append(f"{e['id']}: {f}")

    results = {
        "meta": {
            "title": "MMURM Foundation — independent re-performance of the "
                     "Julius AI test suite",
            "source_document": "MMURM_LHC_Foundation (Anthony Castro / Julius "
                               "AI session analyses, data circa Sep 2025)",
            "spec": "tests/TEST_CENSUS.md (38 tracked items: 30 tests + 8 "
                    "registered claims)",
            "generated": str(date.today()),
            "seed": 20250922,
            "honesty_labels": {
                "REPRODUCTION": "recomputed from inputs fully specified in "
                                "the document",
                "RECONSTRUCTION": "document publishes summaries, not raw "
                                  "data; dataset regenerated from the "
                                  "published summaries under a fixed seed",
                "SYMBOLIC": "analytical claim, recorded not re-run",
                "PROTOCOL": "requires experimental facilities; registered, "
                            "not re-run",
            },
            "provenance_notes": [
                "The source document's 'weighted confidence' scores (84.6%, "
                "updated 89.3%) are a self-assigned scoring rubric, not a "
                "statistical test. They are recorded here for provenance and "
                "are NOT re-issued as findings.",
                "The document gives lambda_1 as both 3.70 and 2.80 in "
                "different sections; this suite reports the value recomputed "
                "from the published correlation matrix (see S1).",
            ],
        },
        "groups": {
            "D_dimensional": d_results,
            "C_conservation": GROUP_C,
            "L_lhc": l_results,
            "S_statistics": s_results,
            "E_ensemble": e_results,
            "R_claims_registry": claims["claims"],
        },
        "contradictions_and_flags": all_flags,
        "figures": fig_names,
    }
    results = clean(results)
    with open(os.path.join(RESULTS_DIR, "results.json"), "w") as fh:
        json.dump(results, fh, indent=2)

    # ---------------- RESULTS.md ----------------
    md = []
    md.append("# MMURM Foundation — Re-performance Results\n")
    md.append("Independent re-run of the 38 tracked items in "
              "`tests/TEST_CENSUS.md` (source: *MMURM_LHC_Foundation*, "
              "Anthony Castro / Julius AI, data circa Sep 2025). "
              f"Generated {results['meta']['generated']}.\n")
    md.append("**Honesty labels.** REPRODUCTION = recomputed from inputs "
              "fully specified in the document. RECONSTRUCTION = the document "
              "publishes summaries (distributions, correlation matrix) but "
              "not the raw dataset; the dataset was regenerated from those "
              "summaries under fixed seed 20250922 and the tests run on "
              "that. If the original dataset is dropped in at "
              "`data/ensemble22_original.csv`, the S/E groups upgrade to "
              "REPRODUCTION automatically. SYMBOLIC / PROTOCOL items are "
              "recorded, not re-run.\n")
    md.append("**Provenance.** The source document's 'weighted confidence' "
              "scores (84.6% → 89.3%) are a self-assigned rubric, not a "
              "statistical test; they are recorded here and are **not** "
              "re-issued as findings.\n")

    md.append("## Verdict summary\n")
    md.append("| ID | Test | Verdict |")
    md.append("|----|------|---------|")
    for gname, group in results["groups"].items():
        if gname == "R_claims_registry":
            continue
        for e in group:
            md.append(f"| {e['id']} | {str(e.get('test', ''))[:70]} | "
                      f"{e.get('verdict', '')} |")
    md.append("\nGroup R (URM-1..URM-8) is a PROTOCOL registry — see "
              "`data/claims_registry.json`; statuses are as published, not "
              "re-tested.\n")

    md.append("## Group D — Dimensional analysis (REPRODUCTION)\n")
    for e in d_results:
        md.append(entry_md(e))
    md.append("## Group C — Conservation laws (SYMBOLIC, recorded)\n")
    for e in GROUP_C:
        md.append(entry_md(e))
    md.append("## Group L — LHC comparisons (REPRODUCTION)\n")
    md.append("The recomputed deviation % and pull reproduce the document's "
              "table exactly — the arithmetic is right. The flags are the "
              "substance: four 'predictions' are digit-for-digit copies of "
              "the measured values, and the other six are the measured "
              "values scaled by named adjustment knobs.\n")
    for e in l_results:
        md.append(entry_md(e))
    md.append("## Group S — Statistical suite (RECONSTRUCTION)\n")
    for e in s_results:
        md.append(entry_md(e))
    md.append("## Group E — Ensemble run (RECONSTRUCTION)\n")
    for e in e_results:
        md.append(entry_md(e))

    md.append("## Contradictions & flags (unsoftened)\n")
    for f in all_flags:
        md.append(f"- {f}")
    md.append("")

    md.append("## Figures\n")
    captions = {
        "fig1_eigenvalue_spectrum.png": "S1 eigenvalue spectrum: recomputed "
            "vs published, with the correct Marchenko-Pastur edge.",
        "fig2_pca_variance.png": "S2 PCA explained variance: published vs "
            "covariance vs correlation PCA on the reconstruction.",
        "fig3_bootstrap_histogram.png": "S3 bootstrap correlation "
            "distribution vs the published CI [0.05, 0.15].",
        "fig4_correlation_heatmap.png": "S4 the published correlation matrix.",
        "fig5_parameter_distributions.png": "Reconstructed ensemble "
            "distributions with null values marked.",
        "fig6_deviation_band.png": "S6 per-reality |deviation| from nulls "
            "with the 5.0-7.5% band shaded (log scale).",
    }
    for name in fig_names:
        md.append(f"![{name}](figures/{name})\n\n*{captions.get(name, '')}*\n")

    md.append("## Reproduce\n")
    md.append("```bash\n.venv/bin/python tests/run_all.py\n```\n")
    md.append("Inputs: `tests/TEST_CENSUS.md` (spec), "
              "`data/ensemble22_correlation_published.csv` (published matrix), "
              "`data/claims_registry.json`. The reconstruction seed is "
              "20250922 throughout.\n")

    with open(os.path.join(RESULTS_DIR, "RESULTS.md"), "w") as fh:
        fh.write("\n".join(md))

    print("Wrote results/results.json, results/RESULTS.md and "
          f"{len(fig_names)} figures.")
    for gname, group in results["groups"].items():
        if gname == "R_claims_registry":
            continue
        for e in group:
            print(f"  {e['id']:>4}  {e.get('verdict', ''):<16} {str(e.get('test', ''))[:60]}")


if __name__ == "__main__":
    main()
