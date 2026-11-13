# Learn the storage mechanism

[Repository](../README.md) · [Scientific account](../science/README.md)

**How can an unknown quantum message survive when its physical carriers keep exchanging places?** The route starts with a small guarded block and ends with a finite-time code and a late-time limit. The educational foundation is John Watrous, *The Theory of Quantum Information* (2018), using the sections identified in the bridge.

| Entry point | Purpose |
|---|---|
| [Worked examples](WORKED_EXAMPLES.md) | See the physical block, the origin condition, the coding cost, and concrete finite-size arithmetic |
| [Watrous bridge](WATROUS_BRIDGE.md) | Connect the source's channel, symmetry, distance, and Haar tools to the project; translate fidelity and Choi normalizations |
| [Thirty milestones](MILESTONES.md) | Follow 12 background goals and 18 project goals in dependency order |
| [Scientific account](../science/README.md) | Read the model, full proofs, scope, and research attribution |

For a first pass, read the worked block example, then the bridge and milestones. Return to the corresponding proof page whenever a milestone points to an argument. The examples explain the mechanism and also show why a favorable block picture can still yield an unhelpful finite-size payload after the error overhead is included.

Keep four distinctions through the route: a carrier's position versus its quantum state; permutation-invariant vectors versus general invariant operators; overlap entanglement fidelity versus uniform channel error; and an achieved lower bound versus an optimal capacity formula. These distinctions connect the physical picture to the theorem's actual guarantee.

All guards and unused sites count toward the physical width. No trajectory is observed or postselected, and no operation occurs during storage. The code's existence allows arbitrary endpoint operations; efficient encoding, extra-noise protection, and a complete finite-time capacity law are outside the established result. The [interpretation](../science/interpretation.md) explains the resulting lifetime statement and its limits.
