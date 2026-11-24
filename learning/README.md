# Learn the storage mechanism

[Repository](../README.md) · [Scientific account](../science/README.md)

**How can an unknown quantum message survive when its physical carriers keep exchanging places?** Follow two endpoint codes from individual carrier trajectories to finite-time storage. Guarded blocks keep interior sites and control the chance of any contaminated core. The mean-escape code keeps whole blocks and corrects correlated errors using a bound on the average number of carriers that leave. John Watrous, *The Theory of Quantum Information* (2018), supplies the channel, distance, and symmetry tools.

| Entry point | Purpose |
|---|---|
| [Worked examples](WORKED_EXAMPLES.md) | Follow the guarded origin map and the vacuum and one-excitation encoding through concrete exchanges and finite-size arithmetic |
| [Watrous bridge](WATROUS_BRIDGE.md) | Translate fidelity and Choi normalizations and trace the channel tools shared by both proofs |
| [Thirty milestones](MILESTONES.md) | Follow 12 background goals and 18 project goals in dependency order |
| [Scientific account](../science/README.md) | Read the model, full proofs, scope, and research attribution |

Start with the [guarded origin map](WORKED_EXAMPLES.md#two-blocks-of-eight-sites) and the [mean-escape example](WORKED_EXAMPLES.md#correcting-average-escape-across-blocks). Then use the bridge and milestones to compare the finite guarantees and the common late-time bound. At fixed error and exposure $`\gamma t=N^{2-\zeta}`$ for fixed $`0\lt\zeta\lt2`$, the mean-escape code certifies $`\Omega_\epsilon(N^{\zeta/2})`$ logical qubits. Evaluate the finite formulas when choosing a code at a particular system size.

Keep four distinctions through the route: a carrier's position versus its quantum state; permutation-invariant vectors versus general invariant operators; overlap entanglement fidelity versus uniform channel error; and an achieved lower bound versus an optimal capacity formula. These distinctions connect the physical picture to the theorem's actual guarantee.

All occupied sites, including guards and unused sites, count toward the physical width. Both codes use fixed endpoints with an unconditional reference-preserving guarantee. The [interpretation](../science/interpretation.md) connects the achieved payloads to the lifetime statement and identifies the remaining questions about endpoint efficiency, noise beyond exchange, and the optimal finite-time payload.
