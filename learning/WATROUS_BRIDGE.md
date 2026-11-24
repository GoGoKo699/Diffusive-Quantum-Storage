# From Watrous to diffusive quantum storage

[Learning route](README.md) · [Thirty milestones](MILESTONES.md) · [Worked examples](WORKED_EXAMPLES.md) · [Scientific account](../science/README.md)

The educational foundation is John Watrous, *The Theory of Quantum Information* (Cambridge University Press, 2018). The [author's page](https://cs.uwaterloo.ca/~watrous/TQI/) identifies the published book and provides an authorized manuscript. Section numbers below were checked against that manuscript. The book supplies the channel, distance, symmetry, and coding language; the repository supplies the spatial exchange model and its finite-time argument.

## Read the foundation alongside the problem

The question is how much unknown quantum information survives when neighboring carriers exchange places without leaving an accessible record. Both codes use permutation-invariant states inside blocks. One keeps interior cores, while the other uses the vacuum and a uniform single excitation to bound the effect of mean label escape across whole blocks.

| Step in this project | Watrous sections | Use the source for | Continue here |
|---|---|---|---|
| Specify the logical register and untouched reference | [2.1.2–2.1.3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf) | Density operators, tensor factors, reductions, and purification | [Model](../science/model.md#one-memory-use) |
| Treat encoding, storage, and recovery as channels | [2.2.1–2.2.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf) | Complete positivity and equivalent operator/dilation descriptions | [Symmetric-loss isometry](../science/one_shot_coding.md#the-symmetric-partial-trace-isometry) |
| Specify what successful recovery means | [3.2, 3.3.2–3.3.3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf) | Purification-based fidelity and channel discrimination with an auxiliary system | [Error criterion](../science/model.md#one-memory-use), then [uniform recovery](../science/one_shot_coding.md#expurgation-to-a-half-diamond-guarantee) |
| Remove sensitivity to internal permutations | [7.1.1–7.1.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.7.pdf) | Vector symmetry and the larger algebra of invariant operators | [Guarded blocks](../science/guarded_blocks.md#the-deterministic-channel-identity), then [late-time structure](../science/late_time.md#a-uniform-twirl-cannot-carry-a-large-schmidt-rank) |
| Average over candidate encoding subspaces | [7.2.1–7.2.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.7.pdf) | Uniform unitary sampling and its moment calculations | [Finite-size code](../science/one_shot_coding.md#finite-size-random-subspace-bound) |
| Read local Bell overlaps from a many-block channel | [2.1.3 and 2.2.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf), [3.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf) | Partial traces, Choi representation, and pure-state overlap | [Logical block channel](../science/mean_label_escape.md#the-logical-channel-of-one-block) and [correlated error correction](../science/mean_label_escape.md#correlated-errors-and-deterministic-endpoints) |
| Interpret a coding statement operationally | [8.2.1–8.2.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.8.pdf) | The relationship between transmission criteria and asymptotic quantum capacity | [One-use theorem](../science/storage_theorem.md) |

Chapter 8 explains a broader asymptotic setting. The present theorem instead constructs a code for one finite memory use, even when its block size depends on the system size. Its finite-size Haar calculation is written out in the repository, so a fixed-channel capacity theorem is not being used to conceal a limiting-order step.

## Translate the notation before comparing equations

| Book convention or concept | Repository notation | Consequence for reading the proof |
|---|---|---|
| A state of a compound register | $`\rho_{RA}`$ | $`R`$ is untouched and unavailable for recovery; successful storage must preserve its correlations with $`A`$ |
| Adjoint written with a star | $`A^\dagger`$ | Both denote the conjugate transpose |
| A channel's dilation with an auxiliary output | $`W:A\to B\otimes E`$ | Tracing $`E`$ gives the receiver channel; tracing $`B`$ defines the complementary channel used here |
| Choi operator $`J(\mathcal N)`$ | Normalized Choi state $`\omega_{RE}`$ | Divide by input dimension $`d`$ and account for the order of the reference and output factors |
| Fidelity $`F(\rho,\sigma)`$ | Overlap entanglement fidelity $`F_e`$ | The repository's $`F_e`$ is the square of the book's fidelity when one argument is the target pure maximally entangled state |
| Completely bounded trace norm, written with triple bars and subscript one | $`\lVert\mathcal M\rVert_\diamond`$ | The project error is half this norm applied to the recovered channel minus the identity |
| Permutation-invariant vectors | $`V_L=\mathrm{Sym}^{L}(\mathbb C^2)`$ | Every permutation inside a block acts as the identity on this input space |
| Haar averaging | A random $`K`$-dimensional subspace of $`V_L^{\otimes B}`$ | Here $`B`$ counts blocks; $`d,b,e`$ denote the input, retained, and discarded dimensions in the coding proof |
| Local reduction of a normalized Choi state | $`F_j`$, the Bell overlap of reference and output qubit $`j`$ | After Pauli averaging, $`1-F_j`$ is the probability of a nonidentity error on block $`j`$. Summing over $`j`$ yields the expected Pauli weight. |

Two normalizations are especially useful to keep visible. With the normalized maximally entangled projector $`\Phi_K`$ and recovered state $`\rho_{R\widehat A}`$,

```math
F_e=\mathrm{Tr}(\Phi_K\rho_{R\widehat A})
=F(\Phi_K,\rho_{R\widehat A})^2,
\qquad
\mathrm{err}(\Lambda)
=\frac12\lVert\Lambda-\mathrm{id}_K\rVert_\diamond.
```

The book's Choi ordering is output followed by input. For a complementary channel $`\mathcal N:A\to E`$ with $`\dim A=d`$, the project convention is

```math
\omega_{RE}
=\frac1d\,\mathrm{SWAP}_{ER}\,
J(\mathcal N)_{ER}\,
\mathrm{SWAP}_{ER}^\dagger.
```

This factor of $`1/d`$ is why the coding proof uses a state of trace one and purity $`1/b`$.

## The connected route through the research

Start with the [worked block example](WORKED_EXAMPLES.md). Then read the [model](../science/model.md) and the first two sections of the [interpretation](../science/interpretation.md): identify the counted physical sites, the inaccessible trajectory, and the reference-preserving error criterion.

Use the symmetry material to read [guarded blocks](../science/guarded_blocks.md). The decisive step is an equality of channels, valid on entangled inputs: if every retained carrier originated inside its own block, the retained channel is a product of symmetric partial traces. The stopped-walk argument then bounds the probability that this condition fails. The favorable event is a proof device, never an observed success flag.

Next read [one-shot coding](../science/one_shot_coding.md). Separate three tasks: calculate the receiver and discarded dimensions, use Haar moments to find a finite code with high entanglement fidelity, and pass to a half-dimensional subcode with uniform recovery. The last task is necessary because high average entanglement fidelity on a whole code is not already the project's half-diamond guarantee.

Now read the [finite-size theorem](../science/storage_theorem.md), followed by the numerical examples. The guard width, outer-code error, subcode loss, and integer rounding all contribute to the stated payload. A positive receiver/discarded dimension ratio alone does not establish a positive finite payload at a specified error.

Read [mean label escape](../science/mean_label_escape.md) next. In the Choi diagnostic for one output block, compare its actual incoming sites with vacuum and derive a Bell infidelity bound from the labels that left. Use Pauli averaging to express the whole channel as a correlated error distribution and bound the chance that its weight exceeds the distance code's correction radius. Linearity of entanglement fidelity supplies a single fixed Pauli choice for the endpoints. The same subcode argument then turns the resulting average fidelity into a uniform channel guarantee.

Finish with the [late-time bound](../science/late_time.md) and the [lifetime interpretation](../science/interpretation.md#payload-and-lifetime). Classical positional mixing gives a sufficient late time for the quantum channel to approach the full permutation twirl. Schur structure then bounds the recoverable coherent dimension. The achieved finite-time payload and this inherited upper bound together give the lifetime exponent for a specified logarithmic payload threshold. The optimal payload curve and a quantum cutoff profile remain open.

## Foundation and project-specific work

The selected book provides the mathematical foundation. The following load-bearing steps are developed in the scientific account rather than attributed to a textbook section:

- The local Poisson exchange model, its tagged backward trajectories, and the guard-width bound valid at all times.
- The reference-stable origin condition that turns a spatially guarded block into a symmetric-loss channel.
- The finite-size specialization of established random coding, followed by the explicit uniform subcode estimate and error budget.
- The vacuum and single-excitation block estimate, the open-path mean escape bound, and their use in the inherited Pauli averaging, distance coding, and fixed-key argument.
- The path-mixing normalization, the one-shot late-time comparison, and the precisely quantified lifetime conclusion.

The research papers behind inherited channel identities, coding tools, exchange dynamics, and mixing estimates are credited in [related work](../references/RELATED_WORK.md) and in the proofs. They remain scientific references; Watrous is the single educational anchor for this route. The [thirty milestones](MILESTONES.md) turn these dependencies into a sequence of standalone learning goals.
