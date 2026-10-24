"""Group I — Inverse structural solver audit (author-supplied addendum,
2026-10-23; NOT part of the original Julius 38-item suite).

Published input (solver report supplied by the author): bridge relations
    g = N,  D = N,  T = N + 2,  chi = 2 - 2N,  R = -chi = 2N - 2,
with Euler closure
    chi = D - (T * B) + R,
solver selects N = 5 over the only other admissible candidate N = 12 via a
topology free-energy sweep (F(g=5) = -9.2023 vs F(g=12) = -0.6029, lower
wins; the sweep's unrestricted optimum is g = 1, rejected on admissibility).
The solver itself labels the result a provisional structural candidate and
the physical Hawking identification NOT established (the recovered
T_H = hbar*kappa / (2*pi*k_B*c) contains no structural N).

Recomputed here: the algebra, the exhaustive integer search, and both
architectures' closures. NOT recomputed: the F(g) sweep (the sweep itself
was not supplied; values are recorded as reported-only), and any Hawking
identification (no H(N) exists yet — that derivation is the stated next
milestone).
"""


def _architecture(N, B):
    return {
        "N": N, "R": 2 * N - 2, "T": N + 2, "B": B, "T_x_B": (N + 2) * B,
        "D": N, "g": N, "chi": 2 - 2 * N,
        "closure_D_minus_TB_plus_R": N - (N + 2) * B + (2 * N - 2),
    }


def run():
    # Exhaustive integer admissibility: B = (5N - 4)/(N + 2) = 5 - 14/(N + 2)
    admissible = []
    for N in range(2, 65):
        num, den = 5 * N - 4, N + 2
        if num % den == 0 and num // den > 0:
            admissible.append((N, num // den))

    arch = {N: _architecture(N, B) for N, B in admissible}
    closures_ok = all(a["closure_D_minus_TB_plus_R"] == a["chi"]
                      for a in arch.values())
    legacy = arch.get(12, {})
    legacy_ok = (legacy.get("R") == 22 and legacy.get("T") == 14
                 and legacy.get("B") == 4 and legacy.get("T_x_B") == 56
                 and legacy.get("D") == 12 and legacy.get("chi") == -22)
    n1_ok = (5 * 1 - 4) % (1 + 2) != 0  # N=1 gives B = 1/3, inadmissible

    return [
        {
            "id": "I1",
            "test": "Bridge relations imply B = (5N-4)/(N+2); positive-integer "
                    "B over N=2..64 leaves only {5, 12}",
            "label": "REPRODUCTION",
            "published_result": "Admissible set {N=5 (B=3), N=12 (B=4)}; "
                                "N=1 rejected (B not a positive integer)",
            "recomputed_result": {
                "admissible_set": [f"N={N} (B={B})" for N, B in admissible],
                "reason": "B = 5 - 14/(N+2) is a positive integer only when "
                          "(N+2) divides 14; in range only N+2 in {7, 14}",
                "N1_inadmissible": n1_ok,
            },
            "verdict": "AGREES" if admissible == [(5, 3), (12, 4)] and n1_ok
                       else "DIFFERS",
        },
        {
            "id": "I2",
            "test": "Both candidate architectures satisfy the Euler closure "
                    "chi = D - (T*B) + R; N=12 reproduces the legacy "
                    "architecture (R=22, T=14, B=4, 56 channels, D=12, "
                    "chi=-22)",
            "label": "REPRODUCTION",
            "published_result": "N=5: R=8, T=7, B=3, 21 channels, D=5, "
                                "g=5, chi=-8. N=12: R=22, T=14, B=4, 56 "
                                "channels, D=12, g=12, chi=-22",
            "recomputed_result": {
                "N5": arch.get(5, {}), "N12": arch.get(12, {}),
                "closures_hold": closures_ok,
                "legacy_architecture_reproduced": legacy_ok,
            },
            "verdict": "AGREES" if closures_ok and legacy_ok else "DIFFERS",
            "notes": "The legacy architecture (22/14/4/12/-22), assembled "
                     "before this solver, is one of only two integer "
                     "solutions of the bridge system. The closure is a "
                     "counting identity the architecture imposes on itself, "
                     "not an independently computed Euler characteristic of "
                     "a specified manifold.",
            "flags": [
                "The bridge relations (g=N, D=N, T=N+2, R=-chi) carry all "
                "of the selective power and their provenance is not stated "
                "in the solver report: if they were abstracted from the "
                "legacy architecture, the N=12 reproduction is guaranteed "
                "by construction and N=5 is the other solution of a system "
                "built around the first; if derived independently, the "
                "{5, 12} admissible set is a discovery. The audit cannot "
                "distinguish these from the report alone.",
            ],
        },
        {
            "id": "I3",
            "test": "Topology free-energy sweep selects N=5 over N=12 "
                    "(lower F wins)",
            "label": "REPORTED-ONLY",
            "published_result": "F(g=5) = -9.2023 vs F(g=12) = -0.6029; "
                                "unrestricted sweep optimum is g=1, "
                                "rejected on admissibility (see I1)",
            "recomputed_result": "Not re-performed: the topology sweep "
                                 "itself (objective definition, code, data) "
                                 "was not supplied with the solver report, "
                                 "so the F values are recorded as reported, "
                                 "not verified.",
            "verdict": "RECORDED (not re-run)",
            "flags": [
                "F has its unrestricted optimum at g=1, so the objective "
                "alone mostly prefers small genus; the admissibility "
                "filter performs the selection and F breaks a two-way tie. "
                "Depositing the sweep would upgrade this item to "
                "REPRODUCTION.",
            ],
        },
        {
            "id": "I4",
            "test": "Physical (Hawking) identification of the structural "
                    "count N",
            "label": "PROTOCOL",
            "published_result": "Solver reports: Inference = provisional "
                                "structural candidate (N=5); Physical "
                                "Hawking identification = not yet "
                                "established. The recovered Hawking "
                                "temperature T_H = hbar*kappa/(2*pi*k_B*c) "
                                "contains no structural N.",
            "recomputed_result": "Agrees with the solver's own labeling: "
                                 "no H(N) — a Hawking-side observable "
                                 "depending on N — exists in the supplied "
                                 "material, so no independent test of N=5 "
                                 "against Hawking physics can be performed.",
            "verdict": "NOT ESTABLISHED",
            "notes": "Stated next milestone (from the solver report): "
                     "derive an independent H(N). If a Hawking-side "
                     "quantity lands near N=5 without passing through the "
                     "bridge relations, the candidate upgrades from "
                     "internal structure to evidence.",
        },
    ]


if __name__ == "__main__":
    import json
    print(json.dumps(run(), indent=2))
