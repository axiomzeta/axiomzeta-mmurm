"""Group D — Dimensional analysis (D1-D6). Label: REPRODUCTION (sympy units).

Each formula is taken verbatim from TEST_CENSUS.md / the Foundation document's
URM_Dimensional_Analysis table. Dimensions are propagated with
sympy.physics.units dimension algebra over abstract base dimensions
(length, time, mass). Julius result: 6/6 PASS.
"""
from sympy.physics.units.definitions.dimension_definitions import length, time, mass

L = length
T = time
M = mass
DIMLESS = L / L  # Dimension(1)

HBAR = M * L**2 / T          # action
C = L / T                    # speed of light
ENERGY = M * L**2 / T**2     # (sympy's named 'energy' dimension is a separate
                             #  symbol, so the required dimension is built from
                             #  base dimensions directly)


def _check(tid, quantity, formula, computed, required, validity):
    ok = computed == required
    return {
        "id": tid,
        "test": quantity,
        "label": "REPRODUCTION",
        "formula_as_published": formula,
        "computed_dimension": str(computed),
        "required_dimension": str(required),
        "status": "PASS" if ok else "FAIL",
        "published_result": "PASS (Julius: 6/6 PASS)",
        "recomputed_result": "PASS" if ok else "FAIL",
        "verdict": "AGREES" if ok else "DIFFERS",
        "validity_domain": validity,
        "notes": "Dimensional consistency is necessary, not sufficient: passing "
                 "shows the formula is unit-coherent, not that it is correct.",
    }


def run():
    results = []

    # D1: N = ln(M_Planck / M_obs) / ln(phi); ratio of two masses is
    # dimensionless, phi is a pure number, ln of a dimensionless number is
    # dimensionless.
    d1 = (M / M) / DIMLESS
    results.append(_check(
        "D1", "Recursion depth N",
        "ln(M_Planck / M_obs) / ln(phi)", d1, DIMLESS, "N > 0"))

    # D2: sigma = (hbar c)^2 / (M_DM c^2)^2
    d2 = (HBAR * C) ** 2 / (M * C**2) ** 2
    results.append(_check(
        "D2", "DM cross-section sigma",
        "(hbar c)^2 / (M_DM c^2)^2", d2, L**2, "M_DM > 0"))

    # D3: m_i = m_0 * sqrt(i); sqrt of a pure index is dimensionless.
    d3 = M * DIMLESS
    results.append(_check(
        "D3", "Mass hierarchy m_i",
        "m_0 * sqrt(i)", d3, M, "i = 1, 2, 3, ..."))

    # D4: P(t) = exp(-lambda t); lambda has dimension 1/time so the exponent
    # is dimensionless and P is dimensionless.
    d4_arg = (1 / T) * T
    d4 = DIMLESS if d4_arg == DIMLESS else d4_arg
    results.append(_check(
        "D4", "Entanglement decay P(t)",
        "exp(-lambda * t)  [lambda ~ 1/time]", d4, DIMLESS, "lambda > 0"))

    # D5: Lambda = 1 / (N * l_Planck)^2 ; N dimensionless.
    d5 = 1 / (DIMLESS * L) ** 2
    results.append(_check(
        "D5", "Cosmological constant Lambda",
        "1 / (N * l_Planck)^2", d5, L**-2, "N > 0"))

    # D6: E_res = sqrt(N) * m_Planck c^2 / phi^N ; sqrt(N) and phi^N are
    # dimensionless, leaving an energy.
    d6 = DIMLESS * (M * C**2) / DIMLESS
    results.append(_check(
        "D6", "Resonance energy E_res",
        "sqrt(N) * m_Planck c^2 / phi^N", d6, ENERGY, "N > 0"))

    return results
