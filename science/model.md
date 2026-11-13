# Memory model and operational error

[Scientific route](README.md) · [Storage theorem](storage_theorem.md) · [Late-time bound](late_time.md)

## A path with unrecorded local exchanges

There are $`N\ge1`$ addressable qubit sites on an open path. Let $`S_i`$ swap sites $`i`$ and $`i+1`$. Each edge has an independent homogeneous Poisson clock of rate $`\gamma>0`$. A clock ring applies that SWAP. There is no additional coherent Hamiltonian or other noise. The averaged storage channel is

```math
\mathcal E_{N,t}=e^{t\mathcal L_N},\qquad
\mathcal L_N(\rho)=\gamma\sum_{i=1}^{N-1}
\bigl(S_i\rho S_i^\dagger-\rho\bigr).
```

Equivalently, if $`\mu_{N,\gamma t}`$ is the adjacent-transposition distribution started from the identity,

```math
\mathcal E_{N,t}(\rho)
=\sum_{\pi\in S_N}\mu_{N,\gamma t}(\pi)
U_\pi\rho U_\pi^\dagger.
```

The convention is rate $`\gamma`$ **per edge**; the total event rate is $`(N-1)\gamma`$. Thus the dimensionless storage time is $`\gamma t`$. The trajectory, final permutation and clock records are inaccessible. The decoder knows the model, the physical site addresses and the chosen storage time.

Random-SWAP semigroups and their convergence are established models in quantum consensus and group-transference theory. The [related-work account](../references/RELATED_WORK.md) credits those sources and distinguishes the finite-time code proved here.

## One memory use

An encoder $`\mathcal V`$ maps a logical register of dimension $`K=2^m`$ into the $`N`$ physical qubits. Only those qubits remain during the interval $`[0,t]`$. A decoder $`\mathcal D`$ acts on them afterwards and returns a $`K`$-dimensional register. General CPTP endpoint operations are permitted. The constructive encoder is an isometry into symmetric block spaces, with unused sites initialized in a fixed pure state.

There are no controls, measurements, resets, fresh ancillas, side communications or protected auxiliary registers during storage. Ancillas used to implement endpoint channels are discarded before storage or introduced after it. An external reference can be entangled with the input and is left untouched; it is unavailable as a recovery resource. No preshared entanglement or noiseless quantum bypass is supplied.

Define the recovered channel and its error by

```math
\Lambda=\mathcal D\circ\mathcal E_{N,t}\circ\mathcal V,
\qquad
\operatorname{err}(\Lambda)
=\frac12\|\Lambda-\operatorname{id}_K\|_\diamond.
```

The diamond norm makes this a uniform guarantee over all logical inputs, including inputs entangled with any external reference. Let

```math
m_\epsilon(N,t)
=\max\left\{m\in\{0,\ldots,N\}:
\operatorname{err}(\Lambda)\le\epsilon
\text{ for some endpoint code}\right\}.
```

This is a finite-time, one-use storage quantity. No repeated-channel capacity limit is part of its definition. The theorem uses $`0<\epsilon<1/8`$.

For comparison, the entanglement fidelity of a code is

```math
F_e=\langle\Phi_K|
(\operatorname{id}_R\otimes\Lambda)
(|\Phi_K\rangle\langle\Phi_K|)
|\Phi_K\rangle,
\qquad
|\Phi_K\rangle=K^{-1/2}\sum_{a=1}^K|a,a\rangle.
```

Half-diamond error at most $`\epsilon`$ implies $`F_e\ge1-\epsilon`$. A high value of $`F_e`$ alone supplies an average-code criterion; the [subcode argument](one_shot_coding.md#expurgation-to-a-half-diamond-guarantee) explicitly upgrades the constructed code to the uniform criterion used here.

## Resources and limits

| Resource | Convention |
|---|---|
| Persistent quantum width | All $`N`$ spins, including discarded guards and unused sites, are counted |
| Storage time | $`t`$, with noise strength $`\gamma`$ fixed; endpoint operations lie outside this interval |
| Intervention during storage | None |
| Encoder and decoder | Arbitrary finite endpoint channels; their gates, temporary width and runtime are unoptimized |
| Classical side information | Model and code parameters only; no trajectory, herald or clock record |
| Error | Unconditional half-diamond distance; no postselection |
| Extra physical noise | Outside this model |

The result is a quantum-memory capability under the stated noise, rather than a total-runtime or hardware-cost advantage. It does not require QRAM or a data-loading oracle. The numerical checks implement finite mathematical identities and bound arithmetic, rather than a large-register encoder or memory device.

## Exact all-time baseline

The fully symmetric space $`\operatorname{Sym}^N(\mathbb C^2)`$ has dimension $`N+1`$, and every permutation acts as its identity. It therefore stores $`\lfloor\log_2(N+1)\rfloor`$ logical qubits exactly for every $`t`$. At $`t=0`$, the whole register stores $`N`$ qubits. At every positive time the interchange distribution has full permutation support; exact zero-error storage is then restricted to the largest Schur spin factor of dimension $`N+1`$. This inherited exact-error statement is separate from the finite nonzero-error construction.

All payload logarithms use base two. Natural logarithms appear in the random-walk probability bounds.
