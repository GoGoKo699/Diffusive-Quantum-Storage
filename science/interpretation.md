# What diffusion leaves available for quantum storage

[Model](model.md) · [Finite-time theorem](storage_theorem.md) · [Late-time bound](late_time.md)

## Protect a block, then keep its interior

A local SWAP destroys a position label while preserving the quantum state carried by that label. Encoding each block into its symmetric spin space removes sensitivity to all permutations within that block. Exchanges across block boundaries remain harmful because different blocks can contain different, mutually entangled logical information.

The decoder keeps a predetermined interior core and discards the surrounding guard sites. A label diffuses a distance of order the square root of time. With sufficiently wide guards, every retained output site is likely to have originated inside its own encoded block. Under that condition, the entire retained channel is exactly a product of symmetric partial traces. This identity holds even when the blocks are entangled with each other and with a reference.

No favorable event is observed or selected. The same decoder acts on every run; unfavorable trajectories contribute to its unconditional error. Discarding the guards costs physical width, and all guard spins are included in $`N`$.

## A symmetric block tolerates partial loss

A length-$`L`$ symmetric input has dimension $`L+1`$. After retaining $`k`$ spins, the receiver and discarded spaces have dimensions $`k+1`$ and $`L-k+1`$. When the retained fraction exceeds one half, their ratio stays greater than one. Finite-size random coding across the blocks converts that ratio into a positive constant logical payload per block, up to the global error overhead.

The [coding proof](one_shot_coding.md) uses established symmetric-loss geometry and random-subspace decoupling. Its explicit subcode step gives uniform recovery for reference-entangled inputs. The result is an existence theorem; the proof does not compile its general encoder or decoder efficiently.

## The finite-time consequence

At fixed small error, the construction supplies an achievable payload of order

```math
\frac{N}{\sqrt{\gamma t\ln N}+\ln N},
```

with explicit additive coding overhead in the [finite-size theorem](storage_theorem.md). In particular, at $`\gamma t=N`$ it supplies $`\Omega(\sqrt{N/\ln N})`$ logical qubits asymptotically. At $`\gamma t=N^{2-\zeta}`$ for fixed $`0\lt \zeta\lt 2`$, it still supplies $`\Omega(N^{\zeta/2}/\sqrt{\ln N})`$ qubits. These payloads grow polynomially, while the exact symmetric-space baseline grows logarithmically.

Classical path-shuffle mixing and Schur-Weyl structure give the complementary [late-time bound](late_time.md): by times of order $`N^2\ln N/\gamma`$, any fixed-small-error one-shot code has only $`O(\log N)`$ logical qubits. Those ingredients are inherited and are not a new quantum cutoff theorem.

This leaves a substantial intermediate storage interval that the stationary symmetry sector alone does not describe. It also leaves logarithmic and payload-dependent gaps: the achievable expression is not a matching formula for the optimal memory curve.

## A quantified lifetime statement

For a fixed $`A\gt 1`$, consider the last time at which a code can retain at least $`A\log_2 N`$ logical qubits, with a fixed $`0\lt \epsilon\lt 1/8`$. The finite-time construction and inherited late-time upper imply constants $`c_{A,\epsilon},C_\epsilon\gt 0`$ such that, for sufficiently large $`N`$,

```math
c_{A,\epsilon}\frac{N^2}{\gamma(\ln N)^3}
\le T_{A,\epsilon}(N)
\le C_\epsilon\frac{N^2\ln N}{\gamma}.
```

The lower follows by taking a sufficiently small fixed prefactor in the construction; its block count is then a sufficiently large multiple of $`\log N`$. For the upper, the [late-time inequality](late_time.md) gives a coefficient-one $`\log_2(N+1)`$ ceiling plus an error-dependent constant, which eventually lies below $`A\log_2N`$. The semigroup property makes the optimal storage payload nonincreasing in time, so these comparisons bound the last admissible time. Consequently

```math
\lim_{N\to\infty}
\frac{\ln[\gamma T_{A,\epsilon}(N)]}{\ln N}=2.
```

This is a lifetime exponent for a specified payload threshold. It does not determine the optimal logarithmic factors, the lifetime of every polynomial payload, or a cutoff profile of the quantum channel.

## Relation to existing protections

Permutation-invariant error correction, symmetric partial trace, noiseless spin factors and quantum-consensus dynamics predate this construction. The [related-work account](../references/RELATED_WORK.md) identifies what each supplies. The added step here is the spatially guarded reduction of finite-time local exchange to a product-loss channel, followed by a one-shot growing-payload guarantee.

The protection depends on the exact SWAP-noise structure. Independent dephasing, loss, imperfect endpoint controls or a coherent interaction that does not preserve the encoding would require a separate analysis. Nothing here establishes fault tolerance to generic local noise. The finite tests in [verification](../verification/README.md) support the stated identities within their tested sizes and do not replace the analytical proofs.
