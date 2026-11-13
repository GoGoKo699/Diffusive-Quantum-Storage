# Related work and attribution

The contribution is a finite-time achievable quantum-storage bound for **unobserved local exchange** on a path. It uses established quantum gossip dynamics, permutation symmetry, finite-size random coding, and classical interchange estimates. The new step is to retain separated output cores of symmetric input blocks: before labels diffuse across the guards, the complete channel on those cores is exactly a tensor product of symmetric partial traces. This yields a growing coherent payload before global mixing.

The comparison below keeps this result separate from stationary capacity formulas, exact permutation protection, and a classical mixing theorem. Bibliographic records, DOI links, and inspected preprint versions are collected in [references.bib](references.bib).

## Quantum gossip and the same local noise model

[Mazzarella, Sarlette, and Ticozzi, *Consensus for Quantum Networks: From Symmetry to Gossip Iterations*](https://doi.org/10.1109/TAC.2014.2336351), IEEE Transactions on Automatic Control **60**, 158--172 (2015), develops quantum consensus and gossip, including convergence to permutation symmetry and preservation of invariant observables.

[Shi, Dong, Petersen, and Johansson, *Reaching a Quantum Consensus: Master Equations That Generate Symmetrization and Synchronization*](https://doi.org/10.1109/TAC.2015.2434034), IEEE Transactions on Automatic Control **61**, 374--387 (2016), studies the continuous-time SWAP Lindbladian on an interaction graph and relates its evolution to classical consensus. The generator used here is a path instance of this established model.

The most direct prior capacity comparison is [Bardet, Junge, LaRacuente, Rouzé, and Stilck França, *Group Transference Techniques for the Estimation of the Decoherence Times and Capacities of Quantum Markov Semigroups*](https://doi.org/10.1109/TIT.2021.3065452), IEEE Transactions on Information Theory **67**, 2878--2909 (2021). Sections IV-D and V-F(d) explicitly treat nearest-neighbor random SWAP noise on a cycle, and Section V gives capacity bounds through the invariant algebra and classical convergence estimates. Finite-time capacity analysis of random exchange therefore predates this project.

The additional claim here is the **constructive growing-payload lower bound before spatial mixing**. The invariant-algebra lower bound alone gives the stationary order $`\log N`$ payload; convergence upper bounds do not supply the guarded-block encoding and its polynomial finite-time payload. The present proof uses a path, and its late-time comparison uses a path mixing theorem directly.

[Novotný, Štěrba, Jex, Kowalski, and Abedi, *Consensus And Information Redistribution In Quantum Networks*](https://arxiv.org/abs/2610.36391v1), arXiv:2610.36391v1 (2026), is a recent comparison concerning asymptotic random-unitary consensus and the recovery of globally encoded observables by cooperating nodes. Recovering selected excitation moments from local measurements is different from preserving an arbitrary reference-entangled logical register with a quantified one-shot error.

## Long-time capacities and exact storage

[Fawzi, Rahaman, and Taheri, *Capacities of Quantum Markovian Noise for Large Times*](https://doi.org/10.1109/TIT.2026.3707704), IEEE Transactions on Information Theory **72**, 6715--6727 (2026), characterizes long-time passive storage through the peripheral-space decomposition. Theorem 2.3 of [arXiv:2408.00116v2](https://arxiv.org/html/2408.00116v2) gives the relevant one-shot bounds; Proposition A.4 treats continuous-time semigroups. For ordinary permutation twirling, the largest retained spin representation has dimension $`N+1`$.

Their Proposition A.6 also establishes that the zero-error capacity of a finite-dimensional quantum Markov semigroup already equals its infinite-time zero-error capacity at every positive time. Thus **instantaneous exact-capacity collapse is inherited**, rather than a second discovery of this project. It does not imply immediate failure at a fixed nonzero storage error.

[Singh and Datta, *Information Storage and Transmission under Markovian Noise*](https://doi.org/10.1103/8rnj-667b), PRX Quantum **7**, 020312 (2026), establishes general long-time capacity formulas, strong-converse properties, and finite-time convergence estimates. Theorems 7, 14, and 16 distinguish peripheral structure, convergence, and storage consequences; their system-dimension and spectral parameters must not be silently replaced by a path's spatial diffusion scale. The present lower bound gives model-specific storage within the transient regime. It neither replaces that framework nor asserts a general bound for arbitrary Markovian noise.

The [late-time converse](../science/late_time.md) is a direct one-shot specialization: after a uniform twirl, the reference--output Schmidt number is at most $`N+1`$, so the entanglement fidelity of a $`K`$-dimensional code is at most $`(N+1)/K`$. Classical interchange mixing transfers this bound to finite time.

## Exchange-error protection and permutation-invariant codes

[Ruskai, *Pauli Exchange Errors in Quantum Computation*](https://doi.org/10.1103/PhysRevLett.85.194), Physical Review Letters **85**, 194--197 (2000), gives a nine-qubit code correcting exchange and single-qubit errors. Permutation protection is an established coding principle.

[Ouyang and Fitzsimons, *Permutation-invariant codes encoding more than one qubit*](https://doi.org/10.1103/PhysRevA.93.042340), Physical Review A **93**, 042340 (2016), constructs growing-dimension symmetric codes that suppress leading-order spontaneous decay. [Ouyang, *Permutation-invariant quantum coding for quantum deletion channels*](https://doi.org/10.1109/ISIT45174.2021.9518078), ISIT (2021), explains why erasures and deletions are equivalent on a permutation-invariant code and gives explicit constructions and encoding/decoding procedures.

Subsequent developments include [Aydin, Alekseyev, and Barg, *A family of permutationally invariant quantum codes*](https://doi.org/10.22331/q-2024-04-30-1321), Quantum **8**, 1321 (2024), and [Ouyang and Brennen, *A theory of quantum error correction for permutation-invariant codes*](https://arxiv.org/abs/2602.13638v1), arXiv:2602.13638v1 (2026).

These works provide exact error-correcting codes and recovery tools. They do not by themselves identify the finite-time channel produced by unobserved labels crossing between neighboring blocks. Here, every good permutation gives the same reduced channel on the retained cores, and a finite-size outer code protects against a **linear fraction of symmetric loss per block**. This approximate coding step differs from requiring each block to correct every deletion pattern exactly. No efficient implementation of the resulting outer code is claimed.

## Symmetric partial trace and finite-size random coding

The partial-trace channel on a symmetric input subspace is inherited. [Lemm and Wilde, *Information-theoretic limitations on approximate quantum cloning and broadcasting*](https://doi.org/10.1103/PhysRevA.96.012304), Physical Review A **96**, 012304 (2017), defines symmetrized partial trace and relates it to universal cloning; see Eq. (7) and the associated symmetric-space discussion.

[Symmetric-loss tools](https://github.com/GoGoKo699/Quantum-Permutation-Noise-Limits/blob/1ae12780408c9b120a90a6dd55b1ea1fe74d62cd/science/symmetric_loss.md) in *Quantum Permutation Noise Limits* reconstruct the qubit geometry and credit the symmetric-sector resource calculations and simulations of [Pirandola, *Energy-constrained two-way capacities of pure-loss and quantum-limited amplifier channels*](https://arxiv.org/abs/2610.06832v3), arXiv:2610.06832v3 (2026), Appendices B and G. These sector ingredients are not presented here as new results. The present achievable bound uses flat output and environment marginals and a finite-size coding theorem; it does not require the bosonic energy-constrained capacity theorem or an adaptive teleportation simulation.

[Klesse, *Approximate quantum error correction, random codes, and quantum channel capacity*](https://doi.org/10.1103/PhysRevA.75.062315), Physical Review A **75**, 062315 (2007), supplies the finite-size random-subspace bound used in the outer code. Equations (28) and (30) of [arXiv:quant-ph/0701102v2](https://arxiv.org/html/quant-ph/0701102v2) control code entanglement fidelity through Kraus number and output purity. This is essential here because the block channel itself grows with the physical system size: a bare appeal to a fixed-channel asymptotic coding theorem would leave a limiting-order gap. The [coding proof](../science/one_shot_coding.md) makes the specialization explicit.

The conversion from good entanglement transmission to a subspace with uniform channel control uses standard fidelity and dilation methods. [Barnum, Knill, and Nielsen, *On Quantum Fidelities and Channel Capacities*](https://doi.org/10.1109/18.850671), IEEE Transactions on Information Theory **46**, 1317--1329 (2000), establishes the entanglement/subspace-capacity equivalence. The dimension-independent dilation viewpoint is developed by [Kretschmann, Schlingemann, and Werner](https://doi.org/10.1109/TIT.2008.917696), IEEE Transactions on Information Theory **54**, 1708--1717 (2008). Trace-distance/fidelity conversion is credited to [Fuchs and van de Graaf](https://doi.org/10.1109/18.761271), IEEE Transactions on Information Theory **45**, 1216--1227 (1999). The finite constants needed here are derived in the coding account; a new general equivalence theorem is not claimed.

## Classical mixing and the late-time comparison

[Lacoin, *Mixing time and cutoff for the adjacent transposition shuffle and the simple exclusion*](https://doi.org/10.1214/15-AOP1004), Annals of Probability **44**, 1426--1487 (2016), proves the classical path interchange cutoff. Equation (1) uses unit rate per bond, and Theorem 2.2 gives mixing time $`N^2\ln N/(2\pi^2)`$ at every fixed total-variation error.

The [late-time argument](../science/late_time.md) combines that theorem with a complete-channel comparison and the stationary Schmidt-number bound. The classical cutoff location is a sufficient late-time bound for storage; it is **not** asserted to be the cutoff location of quantum capacity. The constructive lower bound and the late-time upper leave logarithmic and payload-dependent gaps.

## Related public scientific accounts

[*Quantum Permutation Noise Limits*](https://github.com/GoGoKo699/Quantum-Permutation-Noise-Limits/tree/1ae12780408c9b120a90a6dd55b1ea1fe74d62cd) studies a fresh **uniform** physical permutation twirl followed by independent local noise. Its Schur/symmetric-loss reduction and erasure benchmarks are relevant inherited tools. This project instead studies the distribution of **local** random permutations at a specified finite time, with no additional single-site noise in the stated theorem. A stationary capacity ceiling does not settle this transient channel.

[*Quantum Group Memory Laws*](https://github.com/GoGoKo699/Quantum-Group-Memory-Laws/tree/0d585db681ebc66fe0f2c7acb75f0c636869beef) derives local symmetry-preserving bond-kick dynamics and its full stationary projection, including the ordinary SWAP endpoint. Its local spin-autocorrelation account and its physical-erasure capacity account are separate observables. The existence of a local stationary realization or a slow correlation does not itself supply a finite-time quantum storage code.

## The consequential remainder

The supported addition is the reference-stable guarded-block reduction and its finite-size coding consequence: for every fixed $`0<\zeta<2`$, a polynomially growing logical register can survive until $`t=N^{2-\zeta}/\gamma`$ at fixed small error, without operations during storage. The known stationary payload remains only order $`\log N`$.

This is a statement about information-theoretic storage under the specified exchange noise. It does not establish the optimal finite-time payload, an efficient endpoint circuit, a general passive memory against additional local noise, or an experimental advantage. See the [model](../science/model.md), [main theorem](../science/storage_theorem.md), and [limitations](../science/interpretation.md).

