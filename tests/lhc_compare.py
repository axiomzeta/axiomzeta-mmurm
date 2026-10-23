"""Group L — LHC observable comparisons (L1-L10). Label: REPRODUCTION.

URM 'predicted' values and the document's measured values/uncertainties are
taken from TEST_CENSUS.md (source doc attributes them to ATLAS/CMS/PDG 2024).
Deviation % = (pred - meas)/meas * 100 and pull = (pred - meas)/uncertainty are
recomputed. Spot checks against independently retrieved published values
(PDG 2024 listings; ATLAS Eur. Phys. J. C 80 (2020) 528) are included for
L1, L5, L6, L7 and flagged where the document's 'measured' value is a
superseded average or coincides with a theory prediction.
"""

ROWS = [
    # id, observable, unit, urm_pred, doc_meas, doc_unc, kind, mechanism
    ("L1", "Higgs mass", "GeV", 125.09, 125.09, 0.24, "exact",
     None),
    ("L2", "H -> gamma gamma", "fb", 10.6, 10.1, 1.2, "knob",
     "Gravity-EM coupling c_14 = 0.05 ('5% Higgs enhancement')"),
    ("L3", "H -> ZZ -> 4l", "fb", 1.41, 1.34, 0.15, "knob",
     "Gravity-EM coupling c_14 = 0.05 (same Higgs-sector mechanism as L2)"),
    ("L4", "Top quark mass", "GeV", 172.76, 172.76, 0.3, "exact",
     None),
    ("L5", "W boson mass", "GeV", 80.379, 80.379, 0.012, "exact",
     None),
    ("L6", "Z boson mass", "GeV", 91.1876, 91.1876, 0.0021, "exact",
     None),
    ("L7", "ttbar cross-section 13 TeV", "pb", 879.0, 832.0, 29.0, "knob",
     "Recursive flux factor 1.056 (832.0 x 1.056 = 878.6 ~= 879)"),
    ("L8", "Dijet mass spectrum 13 TeV", "pb/GeV", 0.048, 0.045, 0.008, "knob",
     "Higher-dimensional projections ('6-7% dijet/dilepton')"),
    ("L9", "Missing ET > 1 TeV", "events/fb", 13.1, 12.3, 2.1, "knob",
     "Extra-dim energy loss ('6.5% missing ET'), extra-dim scale ~1 TeV"),
    ("L10", "High-mass dilepton 2 TeV", "events/fb", 0.095, 0.089, 0.015, "knob",
     "Higher-dimensional projections ('6-7% dijet/dilepton')"),
]

# Independently retrieved published values (web spot-check, 2026-10-23):
# - PDG 2024 Higgs listing (Navas et al., PRD 110, 030001 (2024)):
#   m_H = 125.20 +/- 0.11 GeV "OUR AVERAGE". The document's 125.09 +/- 0.24 is
#   the 2015 ATLAS+CMS Run-1 combination (125.09 +/- 0.21 +/- 0.11).
# - PDG 2024/2025 gauge-boson summary table: m_W = 80.3692 +/- 0.0133 GeV;
#   m_Z = 91.1880 +/- 0.0020 GeV.
# - ATLAS ttbar 13 TeV, 36.1 fb^-1 (EPJC 80 (2020) 528): 826.4 pb, total
#   uncertainty ~ +/-20 pb (3.6 stat, 11.5 syst, 15.7 lumi, 1.9 beam).
#   The document's 832.0 +/- 29.0 pb coincides with the NNLO+NNLL SM
#   prediction (Top++: 832 +20/-29 pb), not with that measurement.
SPOT_CHECKS = {
    "L1": {
        "reference": "PDG 2024 average m_H = 125.20 +/- 0.11 GeV",
        "reference_value": 125.20, "reference_unc": 0.11,
        "finding": "Document's 'measured' 125.09 +/- 0.24 is the superseded "
                   "2015 ATLAS+CMS Run-1 combination, not the current PDG "
                   "2024 average.",
    },
    "L5": {
        "reference": "PDG 2024/2025 m_W = 80.3692 +/- 0.0133 GeV",
        "reference_value": 80.3692, "reference_unc": 0.0133,
        "finding": "Document's 80.379 +/- 0.012 is an older average; the URM "
                   "value equals the document's number exactly, not the "
                   "current PDG value.",
    },
    "L6": {
        "reference": "PDG 2024/2025 m_Z = 91.1880 +/- 0.0020 GeV",
        "reference_value": 91.1880, "reference_unc": 0.0020,
        "finding": "Document's 91.1876 +/- 0.0021 is the LEP-era value; "
                   "close to, but not, the current PDG average.",
    },
    "L7": {
        "reference": "ATLAS 13 TeV ttbar (36.1 fb^-1) = 826.4 pb, "
                     "total unc ~ +/-20 pb",
        "reference_value": 826.4, "reference_unc": 20.0,
        "finding": "Document's 'measured' 832.0 +/- 29.0 pb coincides with "
                   "the NNLO+NNLL Standard Model prediction (Top++), not "
                   "with the ATLAS measurement it is attributed to.",
    },
}


def run():
    results = []
    for (tid, name, unit, pred, meas, unc, kind, mechanism) in ROWS:
        dev = (pred - meas) / meas * 100.0
        pull = (pred - meas) / unc
        notes = []
        flags = []
        if kind == "exact":
            flags.append(
                "EXACT MATCH: the URM 'predicted' value is identical to the "
                "measured value to every quoted digit (deviation 0.0%). This "
                "is an identity, not a prediction: the value was taken from "
                "the measurement.")
        else:
            flags.append(
                "KNOB-DRIVEN: the +5-7% correction is produced by a named "
                f"adjustment parameter ({mechanism}), applied to the measured "
                "value; it is not derived from the framework's equations.")
        entry = {
            "id": tid,
            "test": f"{name} ({unit})",
            "label": "REPRODUCTION",
            "urm_predicted": pred,
            "measured_document": meas,
            "uncertainty_document": unc,
            "published_result": f"deviation {dev:.2f}%, pull {pull:.2f} sigma "
                                f"(per source document table)",
            "recomputed_deviation_pct": round(dev, 3),
            "recomputed_pull_sigma": round(pull, 3),
            "verdict": "AGREES",
            "verdict_scope": "The document's internal arithmetic (deviation % "
                             "and pull) reproduces exactly. See flags: "
                             "agreement of arithmetic is not validation of "
                             "the 'prediction'.",
            "kind": kind,
            "mechanism": mechanism,
            "flags": flags,
            "notes": notes,
        }
        if tid in SPOT_CHECKS:
            sc = SPOT_CHECKS[tid]
            ref_dev = (pred - sc["reference_value"]) / sc["reference_value"] * 100.0
            ref_pull = (pred - sc["reference_value"]) / sc["reference_unc"]
            entry["spot_check"] = {
                "reference": sc["reference"],
                "urm_vs_reference_deviation_pct": round(ref_dev, 3),
                "urm_vs_reference_pull_sigma": round(ref_pull, 3),
                "finding": sc["finding"],
            }
            entry["flags"].append("PROVENANCE: " + sc["finding"])
        results.append(entry)
    return results
