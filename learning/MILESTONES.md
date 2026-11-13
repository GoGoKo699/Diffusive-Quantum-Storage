# Project understanding map

The map has **30 milestones: 12 background/preliminaries and 18 narrative/innovation**. The background connects a single carried state to a reference-preserving storage task. The longer narrative then joins the spatial guard mechanism, finite-size coding, late-time comparison and lifetime statement. This allocation gives the construction and its meaning more space than the prerequisites.

The educational anchor is John Watrous, [*The Theory of Quantum Information* (2018)](https://cs.uwaterloo.ca/~watrous/TQI/). Its sections supply quantum-information foundations. The project pages supply the exchange-process estimates, guarded channel identity and research-level coding and mixing ingredients. The [source bridge](WATROUS_BRIDGE.md) explains that division, and the [worked examples](WORKED_EXAMPLES.md) connect the formulas to concrete registers.

The milestones are common understanding targets. Dependencies refer only to earlier milestones. M12 assembles the background into the complete task; M30 assembles the scientific account and its limits.

## Phase I — Background (M01–M12)

### M01 — A state and its position label

**Phase:** Background/preliminaries.

**Central question:** What changes when two quantum carriers exchange positions?

**Understanding target:** Distinguish the internal qubit state, the physical site address and an unobserved carrier origin. Explain why an unknown SWAP can corrupt positional encoding without applying a generic single-qubit noise channel.

**Dependencies and story role:** None. Establishes the local physical object from which the storage problem is built.

**Conceptual connection:** Connects density operators to the distinction between information carried by a spin and knowledge of where that spin went.

**Source pointers:** [Path model](../science/model.md#a-path-with-unrecorded-local-exchanges); Watrous [§2.1.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf), quantum states.

### M02 — One register can carry joint information

**Phase:** Background/preliminaries.

**Central question:** Why is a collection of blocks more than a list of individual states?

**Understanding target:** Interpret a many-qubit tensor-product space and distinguish product inputs from states entangled between blocks. Recognize that a storage guarantee must preserve joint correlations, not only separate block marginals.

**Dependencies and story role:** M01. Extends the local state description to the whole stored register.

**Conceptual connection:** Links the physical partition into blocks to quantum correlations that cross that partition.

**Source pointers:** [One memory use](../science/model.md#one-memory-use); Watrous [§§2.1.2–2.1.3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf), states and composite-system reductions.

### M03 — Unobserved randomness defines a channel

**Phase:** Background/preliminaries.

**Central question:** How does a random sequence of reversible SWAPs become noisy evolution?

**Understanding target:** Explain a CPTP channel as the unconditional input–output map. Distinguish a known permutation unitary from a mixture over inaccessible permutations, and retain rate per edge as part of the model.

**Dependencies and story role:** M01, M02. Turns individual exchanges into the mathematical storage channel.

**Conceptual connection:** Connects classical uncertainty about trajectories with a linear quantum channel acting on all inputs.

**Source pointers:** [Noise channel and normalization](../science/model.md#a-path-with-unrecorded-local-exchanges); Watrous [§§2.2.1–2.2.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf), channel definitions and representations.

### M04 — Discarding a subsystem has a definite meaning

**Phase:** Background/preliminaries.

**Central question:** What remains when a decoder keeps a core and discards its guards?

**Understanding target:** Use partial trace to describe retained information, including correlations with other retained systems. Distinguish discarding known physical sites from selecting a favorable measurement outcome.

**Dependencies and story role:** M02, M03. Supplies the output operation used by the guarded decoder.

**Conceptual connection:** Links a physical loss of access to a channel, without a success flag or postselection.

**Source pointers:** [Predetermined blocks and cores](../science/guarded_blocks.md#predetermined-blocks-and-cores); Watrous [§2.1.3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf), reductions and purifications.

### M05 — The reference is part of the guarantee

**Phase:** Background/preliminaries.

**Central question:** What does it mean to preserve information already entangled with another system?

**Understanding target:** Interpret an untouched reference and a purification of a mixed logical input. Explain why the reference tests preservation of quantum correlations while remaining unavailable to the encoder and decoder.

**Dependencies and story role:** M02, M04. Adds the external system needed to state quantum-memory quality.

**Conceptual connection:** Connects local reduced states with a stronger joint reference–output requirement.

**Source pointers:** [Logical input and inaccessible reference](../science/model.md#one-memory-use); Watrous [§2.1.3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf), reductions and purifications.

### M06 — Two error criteria serve different roles

**Phase:** Background/preliminaries.

**Central question:** How do entanglement fidelity and half-diamond error compare?

**Understanding target:** Distinguish overlap entanglement fidelity from a uniform channel guarantee over arbitrary reference-entangled inputs. Keep the factor one half in the diamond criterion explicit; the project's overlap fidelity is the square of Watrous's fidelity against the target pure state.

**Dependencies and story role:** M03, M05. Defines the operational standard that both construction and converse must meet.

**Conceptual connection:** Connects state comparison to complete channel comparison and explains why a later subcode step is needed.

**Source pointers:** [Operational error](../science/model.md#one-memory-use); Watrous [§3.2 and §§3.3.2–3.3.3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf), fidelity and channel distances.

### M07 — A channel can be viewed through its environment

**Phase:** Background/preliminaries.

**Central question:** Where can the correlations lost by a receiver go?

**Understanding target:** Interpret an isometric dilation and its receiver and complementary channels. Explain how tracing guards creates an environment even though the storage noise itself is a mixture of unitaries.

**Dependencies and story role:** M03, M04, M05. Supplies the receiver–environment view used in coding.

**Conceptual connection:** Connects discarded physical factors to a mathematical test of information leakage.

**Source pointers:** [Symmetric split isometry](../science/one_shot_coding.md#the-symmetric-partial-trace-isometry); Watrous [§2.2.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf), representations of channels.

### M08 — Symmetric vectors remove internal labels

**Phase:** Background/preliminaries.

**Central question:** What does a permutation do inside a fully symmetric spin space?

**Understanding target:** Explain why every permutation acts as the identity on the symmetric vectors, whose length-$`L`$ qubit space has dimension $`L+1`$. Distinguish this protected space from the full $`2^L`$-dimensional register.

**Dependencies and story role:** M01, M02, M03. Introduces the local protection on which the construction is based.

**Conceptual connection:** Connects a symmetry restriction to insensitivity to unknown internal exchanges, with its reduced encoding dimension counted.

**Source pointers:** [Symmetric block spaces](../science/guarded_blocks.md#predetermined-blocks-and-cores); [exact baseline](../science/model.md#exact-all-time-baseline); Watrous [§7.1.1](https://cs.uwaterloo.ca/~watrous/TQI/TQI.7.pdf), symmetric vectors.

### M09 — Symmetry constrains the split channel

**Phase:** Background/preliminaries.

**Central question:** Why do symmetric receiver and environment spaces have simple marginals?

**Understanding target:** Connect a symmetric input split to receiver dimension $`k+1`$ and environment dimension $`L-k+1`$. Explain the role of covariance and irreducibility in the uniform marginals used by the project proof.

**Dependencies and story role:** M07, M08. Turns the protected input space into a tractable loss channel.

**Conceptual connection:** Links invariant-space geometry to the dimensions that will determine the finite coding bound.

**Source pointers:** [Split geometry and marginals](../science/one_shot_coding.md#the-symmetric-partial-trace-isometry); Watrous [§§7.1.1–7.1.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.7.pdf), symmetric vectors and invariant operators.

### M10 — Haar averaging can prove existence

**Phase:** Background/preliminaries.

**Central question:** What can averaging over random subspaces establish about a code?

**Understanding target:** Interpret Haar measure and the use of second moments to bound an average error. Explain why such an average supplies existence of a fixed encoder, while leaving its circuit complexity and a practical search procedure unresolved.

**Dependencies and story role:** M03, M07, M09. Introduces the finite random-coding method used after the spatial reduction.

**Conceptual connection:** Connects symmetry of a mathematical ensemble to existence of a deterministic endpoint code.

**Source pointers:** [Finite-size random-subspace bound](../science/one_shot_coding.md#finite-size-random-subspace-bound); Watrous [§§7.2.1–7.2.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.7.pdf), Haar measure and applications.

### M11 — Decoupling explains recovery

**Phase:** Background/preliminaries.

**Central question:** Why does making the environment independent of the reference permit recovery?

**Understanding target:** Relate a nearly product reference–environment state to a recovered maximally entangled reference–output state. Identify purification and Uhlmann's theorem as the connection, with the chosen fidelity convention retained.

**Dependencies and story role:** M05, M06, M07, M10. Connects the random-code calculation to an operational decoder.

**Conceptual connection:** Joins information leakage, purification and recovery rather than treating a small matrix norm as a storage result by itself.

**Source pointers:** [Recovery from the Haar bound](../science/one_shot_coding.md#finite-size-random-subspace-bound); Watrous [§3.2.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf), characterizations of fidelity.

### M12 — Assemble the complete storage task

**Phase:** Background/preliminaries.

**Central question:** What must be specified before a quantum-memory claim is meaningful?

**Understanding target:** Bring together the physical noise, counted width, inaccessible reference, error criterion, endpoint operations and storage interval. Distinguish one use of a growing register from an asymptotic capacity of repeated independent channels.

**Dependencies and story role:** M03, M06, M08, M11. Synthesizes the background into the complete task used by the scientific account.

**Conceptual connection:** Connects the anchor's channel-coding framework to this project's finite-time definition and resource conventions.

**Source pointers:** [Model and resources](../science/model.md); [finite-size theorem](../science/storage_theorem.md); Watrous [§§8.2.1–8.2.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.8.pdf), capacity definitions and theorem, used as a comparison framework.

## Phase II — Project narrative (M13–M30)

### M13 — Follow one tagged carrier

**Phase:** Narrative/innovation.

**Central question:** How does a local exchange process move a single carrier origin?

**Understanding target:** Explain why a tagged carrier follows a nearest-neighbor continuous-time walk at rate $`\gamma`$ along each incident edge. Keep its diffusive displacement separate from the total number of SWAP clock rings in the register.

**Dependencies and story role:** M01, M03, M12. Begins the construction with one local stochastic trajectory.

**Conceptual connection:** Connects the physical noise generator to spatial uncertainty that guards can control.

**Source pointers:** [Backward tagged trajectories](../science/guarded_blocks.md#a-favorable-event-defined-by-backward-trajectories); Watrous [§2.2.1](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf) supplies channel language; the walk argument is supplied by the project.

### M14 — Allocate blocks, cores and guards

**Phase:** Narrative/innovation.

**Central question:** Which physical spins are encoded, retained and discarded?

**Understanding target:** Interpret the predetermined parameters $`L,r,k=L-2r`$ and $`B=\lfloor N/L\rfloor`$. Explain why guards and unused sites count toward $`N`$, and why the output cores are chosen before any trajectory occurs.

**Dependencies and story role:** M04, M08, M12, M13. Gives the local walk a concrete geometry and a width cost.

**Conceptual connection:** Connects partial trace and symmetry protection to an explicitly charged spatial design.

**Source pointers:** [Predetermined blocks and cores](../science/guarded_blocks.md#predetermined-blocks-and-cores); Watrous [§2.1.3 and §7.1.1](https://cs.uwaterloo.ca/~watrous/TQI/), reductions and symmetric vectors; [worked examples](WORKED_EXAMPLES.md).

### M15 — Origins determine the retained channel

**Phase:** Narrative/innovation.

**Central question:** Why does correct block membership suffice despite many boundary exchanges?

**Understanding target:** Explain the deterministic origin condition and the resulting exact product of symmetric partial traces. Track arbitrary retained subsets and their order, including inputs entangled across blocks and with a reference.

**Dependencies and story role:** M05, M08, M14. Establishes the channel identity at the center of the spatial mechanism.

**Conceptual connection:** Converts local permutation invariance into an exact statement about the global reference–output map.

**Source pointers:** [Deterministic channel identity](../science/guarded_blocks.md#the-deterministic-channel-identity); Watrous [§7.1.1](https://cs.uwaterloo.ca/~watrous/TQI/TQI.7.pdf), symmetric vectors; [worked examples](WORKED_EXAMPLES.md).

### M16 — Stop the walk before a guard is crossed

**Phase:** Narrative/innovation.

**Central question:** How can one bound a retained carrier's failure event on a finite path?

**Understanding target:** Explain the sufficient event that a backward trajectory stays within displacement $`r`$ throughout storage. Understand why stopping at that radius handles physical endpoints and why leaving and returning is conservatively counted as unfavorable.

**Dependencies and story role:** M13, M14, M15. Connects the exact origin identity to an event whose probability can be controlled.

**Conceptual connection:** Joins finite-path geometry to a full-line stopped-walk estimate without assuming an infinite physical memory.

**Source pointers:** [Favorable backward event](../science/guarded_blocks.md#a-favorable-event-defined-by-backward-trajectories); Watrous [§3.3.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf) motivates the eventual complete-channel error target; the stopped-walk derivation is project material.

### M17 — Control all cores at once

**Phase:** Narrative/innovation.

**Central question:** Why does a square-root diffusion estimate also need a logarithmic guard term?

**Understanding target:** Connect the stopped exponential-moment estimate and union bound over retained sites. Distinguish the all-time guard $`r=O(\sqrt{\gamma t\ln(N/\delta)}+\ln(N/\delta))`$ from a Gaussian-only approximation, without assuming independent tagged walks.

**Dependencies and story role:** M14, M16. Converts the local probability estimate into a global failure budget.

**Conceptual connection:** Connects a spatial fluctuation scale to unconditional accuracy of an entire growing quantum register.

**Source pointers:** [All-time tail bound](../science/guarded_blocks.md#a-tail-bound-valid-at-all-times); Watrous [§3.3.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf), complete channel distance; the concentration calculation is supplied locally.

### M18 — Average over favorable and unfavorable histories

**Phase:** Narrative/innovation.

**Central question:** Why is the actual channel close to product loss without observing a favorable event?

**Understanding target:** Explain why input-independent clock probabilities give a convex channel decomposition and half-diamond distance at most $`p_{\mathrm{bad}}`$. Keep the same decoder on every run and preserve the reference-uniform meaning of the bound.

**Dependencies and story role:** M03, M06, M15, M17. Assembles the spatial part of the construction into a usable channel approximation.

**Conceptual connection:** Connects stochastic geometry, exact channel equality and complete-norm contraction under endpoint processing.

**Source pointers:** [Physical channel and product loss](../science/guarded_blocks.md#the-physical-channel-is-close-to-product-loss); Watrous [§§2.2.1–2.2.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf) and [§3.3.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf).

### M19 — Read the receiver–environment dimension ratio

**Phase:** Narrative/innovation.

**Central question:** What quantitative coding resource survives the symmetric partial trace?

**Understanding target:** Derive the roles of $`d=(L+1)^B`$, $`b=(k+1)^B`$ and $`e=(L-k+1)^B`$. Explain the uniform marginals and flat nonzero spectrum of the normalized reference–environment Choi state, yielding purity $`1/b`$.

**Dependencies and story role:** M07, M09, M15. Supplies the finite channel data used by the random-code calculation.

**Conceptual connection:** Connects symmetric-space geometry to leakage into the discarded spins, with both sides of the split counted.

**Source pointers:** [Symmetric partial-trace isometry](../science/one_shot_coding.md#the-symmetric-partial-trace-isometry); Watrous [§2.2.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf) and [§§7.1.1–7.1.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.7.pdf).

### M20 — Turn finite Haar moments into a code

**Phase:** Narrative/innovation.

**Central question:** How does the dimension ratio produce an actual one-use coding guarantee?

**Understanding target:** Explain the Haar second-moment bound $`\mathbb E\lVert\sigma_{RE}-\pi_R\otimes\pi_E\rVert_1\le\sqrt{Ke/b}`$ and the existence of a code with entanglement infidelity at most $`\eta`$ when $`K\le\eta^2b/e`$. Retain its finite-size character when block length grows.

**Dependencies and story role:** M10, M11, M19. Turns the reduced channel's geometry into a recoverable logical dimension.

**Conceptual connection:** Connects random-subspace averaging and decoupling to a fixed endpoint encoder and decoder in one memory use.

**Source pointers:** [Finite-size random-subspace bound](../science/one_shot_coding.md#finite-size-random-subspace-bound); Watrous [§§7.2.1–7.2.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.7.pdf) and [§3.2.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf).

### M21 — Upgrade fidelity on a smaller code

**Phase:** Narrative/innovation.

**Central question:** How is a maximally mixed code's fidelity upgraded to uniform reference-preserving recovery?

**Understanding target:** Explain the common-environment Stinespring comparison and selection of a half-dimensional low-error subspace. Connect the loss of one logical qubit to ideal half-diamond error at most $`2\sqrt\eta`$, rather than treating high entanglement fidelity as an automatic uniform bound.

**Dependencies and story role:** M06, M07, M20. Makes the finite code satisfy the project's operational criterion.

**Conceptual connection:** Joins a trace-averaged coding statement to an operator-norm estimate stable under arbitrary references.

**Source pointers:** [Subcode expurgation](../science/one_shot_coding.md#expurgation-to-a-half-diamond-guarantee); Watrous [§2.2.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf) and [§§3.3.2–3.3.3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf).

### M22 — Spend one unconditional error budget

**Phase:** Narrative/innovation.

**Central question:** How do trajectory failure and imperfect coding combine in the physical memory?

**Understanding target:** Explain the bound $`p_{\mathrm{bad}}+2\sqrt\eta`$ after all endpoint operations. Track the choices $`\delta=\epsilon/2`$ and $`\eta=\epsilon^2/16`$ without adding a success-conditioned claim or a protected bypass.

**Dependencies and story role:** M18, M21. Joins the spatial mechanism and finite code into one unconditional storage protocol.

**Conceptual connection:** Connects complete-channel contraction and the triangle inequality to a single stated accuracy target.

**Source pointers:** [Transfer to the exchange process](../science/one_shot_coding.md#transfer-to-the-physical-exchange-process); [explicit error choices](../science/storage_theorem.md#an-explicit-bound-with-one-error-parameter); Watrous [§3.3.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf).

### M23 — Count the finite logical payload

**Phase:** Narrative/innovation.

**Central question:** What does the theorem certify for specified finite parameters?

**Understanding target:** Interpret the rounded block bound with $`L=8r`$, $`k=6r`$, $`B=\lfloor N/(8r)\rfloor`$ and coding overhead. Compare it with the exact $`\lfloor\log_2(N+1)\rfloor`$ baseline by taking their maximum, including cases where the block certificate is inactive.

**Dependencies and story role:** M12, M14, M19, M22. Assembles all constructive ingredients into the finite theorem.

**Conceptual connection:** Connects physical width, receiver–environment ratio, integer code dimension and unconditional error in one accounting statement.

**Source pointers:** [Explicit finite bound](../science/storage_theorem.md#an-explicit-bound-with-one-error-parameter); [worked examples](WORKED_EXAMPLES.md); Watrous [§8.2.1](https://cs.uwaterloo.ca/~watrous/TQI/TQI.8.pdf) for the coding-task comparison.

### M24 — Interpret the achieved time regimes

**Phase:** Narrative/innovation.

**Central question:** How much information does the construction retain for growing storage times?

**Understanding target:** Explain the fixed-error lower bound and its consequences at $`\gamma t=N`$ and $`\gamma t=N^{2-\zeta}`$ for fixed $`0\lt\zeta\lt2`$. Distinguish the sufficient superlogarithmic window $`\gamma t=o(N^2/(\ln N)^3)`$ from a matching optimal payload curve.

**Dependencies and story role:** M23. Connects the exact finite result to the contribution's macroscopic storage consequence.

**Conceptual connection:** Links diffusion distance and available block count to a growing quantum payload without intervention during storage.

**Source pointers:** [Scaling consequences](../science/storage_theorem.md#scaling-that-follows-from-the-finite-bound); [physical interpretation](../science/interpretation.md#the-finite-time-consequence); Watrous [§§8.2.1–8.2.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.8.pdf), with the distinction from repeated-use capacity retained.

### M25 — Separate exact error from fixed nonzero error

**Phase:** Narrative/innovation.

**Central question:** Why does full permutation support at positive time not defeat the approximate code?

**Understanding target:** Explain why exact recovery for a full-support permutation mixture would also recover the uniform twirl. Distinguish that support-based requirement from the probabilities of harmful histories and the fixed nonzero-error guarantee; M27 supplies the structural ceiling for the twirl.

**Dependencies and story role:** M03, M06, M08, M23, M24. Resolves an apparent conflict between the inherited exact baseline and finite-time retention, while preparing the twirl comparison.

**Conceptual connection:** Connects exact symmetry protection with an accuracy-dependent operational task.

**Source pointers:** [Exact all-time baseline](../science/model.md#exact-all-time-baseline); [late-time scope](../science/late_time.md#what-this-comparison-establishes); Watrous [§7.1.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.7.pdf) and [§3.3.3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf).

### M26 — Import the classical path-mixing scale

**Phase:** Narrative/innovation.

**Central question:** What does the established adjacent-shuffle mixing theorem actually say?

**Understanding target:** Interpret total-variation distance from the uniform permutation law, rate per bond and the inherited $`N^2\ln N/\gamma`$ mixing scale. Keep the theorem's fixed error level and path geometry visible; do not turn a classical cutoff into a quantum-capacity cutoff.

**Dependencies and story role:** M03, M12, M13. Introduces the global stochastic input needed for the late-time comparison.

**Conceptual connection:** Connects local tagged motion to a separate statement about mixing the entire permutation distribution.

**Source pointers:** [Exact path normalization and inherited mixing](../science/late_time.md#the-exact-path-normalization); Watrous [§§2.2.1–2.2.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf) supplies the mixture-of-channels framework; the mixing theorem is credited in the project source.

### M27 — Identify what survives a uniform twirl

**Phase:** Narrative/innovation.

**Central question:** Why can a fully mixed permutation channel preserve only a logarithmic quantum payload?

**Understanding target:** Explain the spin and permutation-multiplicity factors in Schur–Weyl structure. Track the untouched reference and show why the twirled output has Schmidt number at most $`N+1`$, even with arbitrary endpoint processing.

**Dependencies and story role:** M05, M07, M08, M25, M26. Supplies the all-code restriction after positional labels have mixed.

**Conceptual connection:** Connects permutation-invariant operator structure to entanglement that remains recoverable, rather than merely counting a particular encoding space.

**Source pointers:** [Twirl Schmidt-number bound](../science/late_time.md#a-uniform-twirl-cannot-carry-a-large-schmidt-rank); Watrous [§7.1.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.7.pdf) and [§2.1.3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf).

### M28 — Turn mixing into a one-use converse

**Phase:** Narrative/innovation.

**Central question:** How does classical mixing bound every fixed-error quantum code?

**Understanding target:** Combine half-diamond distance at most $`d_N(t)`$ from the twirl with $`F_e\le(N+1)/K`$ for the twirl. Interpret the resulting finite-time ceiling and its $`O(\log N)`$ late-time consequence for arbitrary encoders, decoders and references.

**Dependencies and story role:** M06, M26, M27. Assembles the inherited ingredients into the operational comparison with the constructive lower bound.

**Conceptual connection:** Connects a classical distribution distance and an entanglement limitation to the same one-use criterion used by the code.

**Source pointers:** [Finite-time one-shot converse](../science/late_time.md#the-finite-time-one-shot-converse); Watrous [§3.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf), [§§3.3.2–3.3.3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf) and [§8.2.1](https://cs.uwaterloo.ca/~watrous/TQI/TQI.8.pdf).

### M29 — State the lifetime exponent with its threshold

**Phase:** Narrative/innovation.

**Central question:** Which lifetime exponent follows despite the remaining logarithmic gap?

**Understanding target:** Define the last admissible time for at least $`A\log_2N`$ logical qubits at fixed $`A\gt1`$ and fixed $`0\lt\epsilon\lt1/8`$. Explain the lower $`N^2/(\gamma(\ln N)^3)`$ and upper $`N^2\ln N/\gamma`$ scales, semigroup monotonicity and the limiting exponent two.

**Dependencies and story role:** M12, M23, M24, M28. Joins construction and converse into a precisely quantified lifetime statement.

**Conceptual connection:** Connects endpoint-operation freedom and time monotonicity with a threshold-specific asymptotic conclusion, leaving the payload curve unresolved.

**Source pointers:** [Quantified lifetime statement](../science/interpretation.md#a-quantified-lifetime-statement); Watrous [§§2.2.1–2.2.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf) and [§8.2.1](https://cs.uwaterloo.ca/~watrous/TQI/TQI.8.pdf) for the operational framework.

### M30 — Explain the complete contribution and its boundary

**Phase:** Narrative/innovation.

**Central question:** What new storage capability has been established after the inherited tools and full assumptions are credited?

**Understanding target:** Explain the complete route from local exchanges through guarded product loss and one-shot reference-preserving coding to growing finite-time storage, then its late-time and threshold-lifetime comparison. Separate the spatial contribution from inherited symmetry, coding and mixing tools. Keep endpoint complexity, exact noise structure, accuracy conventions and unresolved optimality visible.

**Dependencies and story role:** M12, M18, M21, M23, M24, M25, M28, M29. Synthesizes the project globally and connects every load-bearing stage to its scientific consequence.

**Conceptual connection:** Joins physical mechanism, operational theorem, attribution and limits into one account: no matching finite-time payload curve, efficient implementation, quantum cutoff profile or generic-noise protection is inferred.

**Source pointers:** [Scientific route](../science/README.md); [interpretation and limits](../science/interpretation.md); [related work](../references/RELATED_WORK.md); [verification scope](../verification/README.md); Watrous [§§3.3.2–3.3.3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf), [§7.1](https://cs.uwaterloo.ca/~watrous/TQI/TQI.7.pdf) and [§8.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.8.pdf) supply the connected foundations.

Return to the [learning route](README.md) or the [scientific account](../science/README.md).
