# What remains after the labels have mixed

The finite-time construction uses the locality of exchange before the whole chain has shuffled. At late times, the same physical memory approaches a uniform permutation channel. The following converse applies directly to one use of the memory, with arbitrary encoders, decoders, and entangled reference systems. It does not assume independent repeated uses or an efficient decoding circuit.

All logarithms measuring information are base two. The mixing-time expressions use the natural logarithm $`\ln`$.

## The exact path normalization

For the $`N`$-site path, write

```math
\mathcal L_N(\rho)
=\gamma\sum_{x=1}^{N-1}
\bigl(S_{x,x+1}\rho S_{x,x+1}-\rho\bigr),
\qquad
\mathcal E_{N,t}=e^{t\mathcal L_N}.
```

Let $`\mu_{N,t}`$ be the law of the corresponding interchange process, started at the identity, and let $`u_N`$ be uniform on $`S_N`$. Then

```math
\mathcal E_{N,t}(\rho)
=\sum_{\pi\in S_N}\mu_{N,t}(\pi)U_\pi\rho U_\pi^\dagger,
\qquad
\mathcal P_N(\rho)
=\frac1{N!}\sum_{\pi\in S_N}U_\pi\rho U_\pi^\dagger.
```

The classical distance that will enter the quantum bound is

```math
d_N(t)
=\lVert\mu_{N,t}-u_N\rVert_{\mathrm{TV}}
=\frac12\sum_{\pi\in S_N}
\left|\mu_{N,t}(\pi)-\frac1{N!}\right|.
```

Lacoin's [Theorem 2.2](https://arxiv.org/html/1309.3873v3) concerns this **path** process. Equation (1) of that paper uses one exchange per unit time on each bond, rather than one exchange per unit time on the whole chain. With the rate $`\gamma`$ above, its result is

```math
\lim_{N\to\infty}
\frac{2\pi^2\gamma\,T_{\mathrm{mix},N}(\delta)}
     {N^2\ln N}
=1,
\qquad 0\lt \delta\lt 1,
```

where $`T_{\mathrm{mix},N}(\delta)=\inf\{t:d_N(t)\le\delta\}`$. The error level $`\delta`$ is fixed in this limit. No bound uniform in an arbitrarily varying $`\delta_N`$ is inferred from this theorem.

## From classical mixing to a complete quantum-channel bound

The triangle inequality and the unit diamond norm of a unitary channel give

```math
\frac12\lVert\mathcal E_{N,t}-\mathcal P_N\rVert_\diamond
\le
\frac12\sum_{\pi\in S_N}
\left|\mu_{N,t}(\pi)-\frac1{N!}\right|
=d_N(t).
```

This includes inputs entangled with any reference. Composing with a CPTP encoder or decoder does not increase the diamond norm. In particular, the expectation of any binary test changes by at most $`d_N(t)`$.

For a code of dimension $`K`$, let $`\mathcal A:\mathcal B(\mathbb C^K)\to\mathcal B((\mathbb C^2)^{\otimes N})`$ and $`\mathcal D`$ be its CPTP encoder and decoder. Let

```math
F_e(\mathcal D\mathcal N\mathcal A)
=
\langle\Phi_K|
(\mathrm{id}\otimes\mathcal D\circ\mathcal N\circ\mathcal A)
(\Phi_K)
|\Phi_K\rangle,
\qquad
|\Phi_K\rangle=K^{-1/2}\sum_{a=1}^K|a,a\rangle,
\qquad \Phi_K=|\Phi_K\rangle\langle\Phi_K|.
```

Thus $`F_e`$ is an overlap with the normalized maximally entangled state, rather than its square root. The channel comparison implies

```math
F_e(\mathcal D\mathcal E_{N,t}\mathcal A)
\le
F_e(\mathcal D\mathcal P_N\mathcal A)+d_N(t).
```

## A uniform twirl cannot carry a large Schmidt rank

Schur--Weyl duality decomposes the physical register as

```math
(\mathbb C^2)^{\otimes N}
=
\bigoplus_j V_j\otimes M_j,
\qquad
\dim V_j=2j+1\le N+1.
```

Here $`V_j`$ is a spin representation and $`M_j`$ is its permutation multiplicity space. Twirling removes coherence between different $`j`$ sectors and replaces each multiplicity state:

```math
\mathcal P_N(\rho)
=
\bigoplus_j
\mathrm{Tr}_{M_j}(P_j\rho P_j)
\otimes\frac{I_{M_j}}{\dim M_j}.
```

The same identity holds with an untouched reference. In each sector, the only output subsystem that can remain entangled with that reference is $`V_j`$, of dimension at most $`N+1`$. The total reference--output state therefore has Schmidt number at most $`N+1`$: it is a convex combination of pure states of Schmidt rank at most that number. Replaced multiplicity registers, local sector flags, and a local decoding channel do not increase Schmidt number.

A normalized pure state of Schmidt rank at most $`r`$ has overlap at most $`r/K`$ with $`\Phi_K`$, by Cauchy--Schwarz on its Schmidt coefficients. Convexity extends the bound to mixed states. Consequently, for every encoder and decoder,

```math
\boxed{
F_e(\mathcal D\mathcal P_N\mathcal A)
\le
\min\left\{1,\frac{N+1}{K}\right\}.
}
```

This is the permutation instance of the peripheral-space bounds of [Fawzi, Rahaman, and Taheri](../references/RELATED_WORK.md#long-time-capacities-and-exact-storage). The proof here makes its one-shot and reference-preserving content explicit.

## The finite-time one-shot converse

Combining the preceding two bounds yields

```math
\boxed{
F_e(\mathcal D\mathcal E_{N,t}\mathcal A)
\le
\min\left\{1,\frac{N+1}{K}+d_N(t)\right\}.
}
```

In particular, if $`F_e\ge1-\varepsilon`$ and $`d_N(t)\lt 1-\varepsilon`$, then

```math
\boxed{
\log_2K
\le
\log_2(N+1)
-\log_2\bigl(1-\varepsilon-d_N(t)\bigr).
}
```

The same bound holds for the stronger complete-channel storage criterion

```math
\frac12
\lVert\mathcal D\circ\mathcal E_{N,t}\circ\mathcal A-\mathrm{id}_K\rVert_\diamond
\le\varepsilon,
```

because that criterion implies $`F_e\ge1-\varepsilon`$. The converse therefore applies to both entanglement transmission at the stated overlap fidelity and half-diamond storage error.

Fix $`0\lt \varepsilon\lt 1`$ and $`a\gt 0`$. At times

```math
t_N\ge
\frac{(1+a)N^2\ln N}{2\pi^2\gamma},
```

Lacoin's theorem gives $`d_N(t_N)\to0`$, and hence

```math
\log_2K
\le
\log_2(N+1)-\log_2(1-\varepsilon)+o(1).
```

For a finite statement, choose a fixed $`0\lt \delta\lt 1-\varepsilon`$ and assume $`d_N(t)\le\delta`$. Then the right-hand side is simply $`\log_2[(N+1)/(1-\varepsilon-\delta)]`$.

## What this comparison establishes

The bound shows that a fully mixed set of positional labels leaves only order $`\log N`$ coherent qubits at any fixed error. The [finite-time construction](storage_theorem.md) retains a polynomially larger payload at $`t=N^{2-\zeta}/\gamma`$ for every fixed $`0\lt \zeta\lt 2`$. Together, these statements distinguish the diffusive transient from the stationary symmetry sector.

The upper bound uses **classical** permutation mixing as a sufficient condition for the quantum memory to approach its stationary payload. It does not prove that the quantum storage capacity has a cutoff at the same location, determine its exact finite-time value, or close the logarithmic gap between the construction and this late-time comparison. Exact zero-error collapse at every positive time is an inherited, separate statement; it is not evidence of immediate failure at a fixed nonzero error.

Return to the [scientific index](README.md) or the [related-work comparison](../references/RELATED_WORK.md).

