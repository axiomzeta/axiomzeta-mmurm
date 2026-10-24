# Time Governing Equations — Source Text (as supplied, 2026-10-23)

Provenance: supplied by the author in chat, 2026-10-23, as "Recursive
Phase Ontology | Revised 8–7–3–21–5 formulation | Formal model proposal"
(Axiom Zeta Innovations). Transcribed verbatim below (plain-text
rendering of the pasted original). The parameterized restatement lives in
`Time_Governing_Equations_parameterized.md`.

---

Time is modeled as update order arising from a recursively evolving
phase state. Duration, causal direction, and branching are projections
of the update structure. The following formulation retains the four
original equations while incorporating eight reality sectors, seven
timelines per sector, three branches per timeline, twenty-one channels
per sector, and five spatial coordinates.

## Configuration and indexing

| Symbol | Range | Interpretation |
|---|---|---|
| r | 1,…,8 | Reality sector |
| ℓ | 1,…,7 | Timeline within reality r |
| b | 1,…,3 | Branch within timeline ℓ |
| c = 3(ℓ−1)+b | 1,…,21 | Branched-channel index within a reality |
| x = (x¹,…,x⁵) | x ∈ M⁵ | Five-dimensional spatial coordinate |

Counting rule: 7 × 3 = 21 channels per reality; 8 × 21 = 168 indexed
reality–channel combinations globally. These are discrete sectors and
pathways, not 168 spatial dimensions.

## T1 — Recursive succession across indexed sectors

P⁽ʳ,ℓ,ᵇ⁾ₙ₊₁(x) = Rᵣ,ℓ,ᵦ[P⁽ʳ,ℓ,ᵇ⁾ₙ(x); Cₙ, Aₙ, G₅]

Here P is a phase state on a five-dimensional spatial manifold M⁵, R is
the state-update map, Cₙ and Aₙ retain the original model's
context/control inputs, and G₅ denotes optional five-dimensional
geometric data (such as a metric). Coupling between sectors is not
assumed unless specified separately.

## T2 — Twenty-onefold temporal-channel admissibility

ΠT(Pₙ → Pₙ₊₁ | r, x) ∈ T₂₁ = {Cℓ,b : ℓ = 1,…,7; b = 1,2,3}

Cℓ,b is a label for one of the 21 branch channels in each reality. A
complete state is indexed by (r,ℓ,b,x); the global set of indexed
channels is T = { (r,Cℓ,b) }, with cardinality 168. This replaces the
original fourteenfold admissibility set {C₁,…,C₁₂,Hᵢₙ,Hₒᵤₜ}; the fate
of Hᵢₙ/Hₒᵤₜ must therefore be explicitly specified, rather than silently
equating them with the new branches.

## T3 — Duration as a phase projection

ΔΘ⁽ʳ,ℓ,ᵇ⁾ₙ(x) = Arg[τₙ₊₁(x) τₙ(x)*]

tₙ₊₁ / tₙ = exp[ΔΘ⁽ʳ,ℓ,ᵇ⁾ₙ(x) / θᵣ,ℓ,ᵦ]

The logarithmic relation ΔΘ = θ ln(tₙ₊₁/tₙ) is a constitutive model
assumption, not a general mathematical identity of complex phase. It
requires positive clock readings, nonzero θ, and a chosen
phase-unwrapping convention; otherwise Arg is defined only modulo 2π.

## T4 — Causal direction and three-way temporal branching

Cℓ,b → { Cℓ′,1 ; Cℓ′,2 ; Cℓ′,3 } subject to Aᵣ(ΔK, D, B, x)

Aᵣ is an admissibility/selection rule, and ℓ′ denotes an allowed
successor timeline (which may equal ℓ if within-timeline transitions are
intended). The original conditions ΔK ≥ 0, ΔK < 0 with D > Dᶜ, and
B > Bᶜ can still serve as selection predicates, but their mapping to
three branches must be declared. A possible explicit convention is b=1
for ΔK ≥ 0; b=2 for ΔK < 0 and D > Dᶜ; b=3 for B > Bᶜ. These conditions
overlap, so priority or multichannel selection must be specified.
