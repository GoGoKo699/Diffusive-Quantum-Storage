# What diffusion leaves available for quantum storage

[Model](model.md) · [Mean escape theorem](mean_label_escape.md) · [Guarded code](storage_theorem.md) · [Late-time upper bound](late_time.md)

## A few carriers can leave each block

A SWAP exchanges two address labels while preserving the states they carry. The vacuum and uniform one-excitation state store one logical qubit invariantly under permutations within a block. If some carriers leave, both the missing portion of the excitation and an excitation entering from another block can affect recovery.

The [mean escape theorem](mean_label_escape.md) bounds both contributions in a marginal Bell test. On the full encoded register, a Pauli average makes the sum of the marginal error probabilities equal the expected error weight. The outer code corrects any pattern up to its distance threshold. A fixed choice of the endpoint Paulis and a subcode then give the uniform half-diamond guarantee.

## Two ways to use spatial blocks

The original [guarded construction](guarded_blocks.md) places sacrificial spins around every retained core. When each retained carrier comes from its original block, the channel on all cores is exactly a product of symmetric partial traces. Finite-size random coding converts their retained-to-discarded dimension ratio into a positive amount of information per block. The proof pays a union bound to control the event across every core.

The mean escape code uses entire blocks and needs a small average fraction of misplaced carriers. Block correlations can persist. This lets the block length scale with the diffusion length alone at fixed error. The explicit bounds can favor different codes at finite size. Endpoint computational efficiency is open for both constructions.

## Payload and lifetime

At $`\gamma t=N^{2-\zeta}`$ for fixed $`0\lt\zeta\lt2`$, the new code stores $`\Omega_\epsilon(N^{\zeta/2})`$ logical qubits. More generally, the guarantee grows parametrically faster than $`\log N`$ for $`\gamma t=o(N^2/(\ln N)^2)`$.

For fixed $`A\gt1`$ and $`0\lt\epsilon\lt1/8`$, let $`T_{A,\epsilon}(N)`$ be the last admissible storage time for a payload of at least $`A\log_2 N`$ qubits. The [finite-size construction](mean_label_escape.md) and [late-time bound](late_time.md) give, for sufficiently large $`N`$,

```math
c_{A,\epsilon}\frac{N^2}{\gamma(\ln N)^2}
\le T_{A,\epsilon}(N)
\le C_\epsilon\frac{N^2\ln N}{\gamma}.
```

Take a sufficiently small fixed prefactor on the left so that the number of blocks exceeds the required multiple of $`\log N`$. On the right, the late-time upper bound is $`\log_2(N+1)`$ plus an error-dependent constant. The semigroup makes optimal payload nonincreasing because the decoder at an earlier time can append the remaining evolution at that endpoint. The lifetime exponent for this payload threshold is therefore two. The logarithmic gap and optimal intermediate-time storage curve remain open.

Both codes assume exactly the specified exchange dynamics. Additional loss or dephasing during storage needs a separate analysis. The [related-work account](../references/RELATED_WORK.md) traces the symmetry, coding, and mixing ingredients.
