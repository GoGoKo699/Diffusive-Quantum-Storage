# Finite-time storage under local exchange noise

[Model and error criterion](model.md) · [Guarded reduction](guarded_blocks.md) · [Finite-size coding](one_shot_coding.md) · [Interpretation](interpretation.md)

There are $`N`$ physical qubits on a path. Independent rate-$`\gamma`$ Poisson clocks apply a SWAP across each adjacent edge. The channel after time $`t`$ is $`\mathcal E_{N,t}`$. There is no control, protected auxiliary memory, reset, or measurement during storage. Encoding before storage and decoding afterwards may be arbitrary.

Let $`m_\epsilon(N,t)`$ be the largest integer number of logical qubits whose recovered channel has half-diamond distance at most $`\epsilon`$ from the identity. Thus the guarantee holds uniformly for inputs entangled with any external reference.

## General finite-size construction

Choose integers $`r\ge1`$, $`L\ge4r+1`$, and $`B=\lfloor N/L\rfloor\ge1`$. Put

```math
k=L-2r,\qquad
R=\frac{k+1}{2r+1},
\qquad
p_*=
\min\!\left\{1,
2N\exp\!\left[-\frac{r^2}{4\gamma t+2r/3}\right]
\right\}.
```

For any $`0\lt\eta\lt1`$ and integer $`s\ge1`$ satisfying

```math
s\le B\log_2R-2\log_2\frac1\eta,
```

there exists a code storing $`s-1`$ logical qubits with

```math
\frac12\lVert\mathcal D\circ\mathcal E_{N,t}\circ\mathcal V
-\mathrm{id}_{2^{s-1}}\rVert_\diamond
\le p_*+2\sqrt\eta.
```

**Proof.** Encode into the product of $`B`$ length-$`L`$ symmetric spaces and retain $`k`$ core sites per block. The [guard argument](guarded_blocks.md) bounds the unfavorable-history probability by $`p_*`$ and makes the physical core channel that close in half-diamond norm to $`\Phi_{L\to k}^{\otimes B}`$. With $`K=2^s`$, the stated condition is precisely $`K\le\eta^2R^B`$. The [finite-size code](one_shot_coding.md) has entanglement infidelity at most $`\eta`$. Its half-dimensional subcode stores $`s-1`$ logical qubits with ideal half-diamond error at most $`2\sqrt\eta`$. Composition and the triangle inequality add at most $`p_*`$. No repeated-channel limit or trajectory record is used. $`\square`$

## An explicit bound with one error parameter

Fix $`0\lt\epsilon\lt1/8`$. Define

```math
\begin{aligned}
x&=\ln\frac{4N}{\epsilon},\\
r&=\left\lceil2\sqrt{\gamma t x}+\frac{2x}{3}\right\rceil,\\
L&=8r,\qquad
B=\left\lfloor\frac{N}{8r}\right\rfloor,\\
R_r&=\frac{6r+1}{2r+1},\\
h_\epsilon&=8+4\log_2\frac1\epsilon.
\end{aligned}
```

Then, for every $`N\ge1`$ and $`t\ge0`$,

```math
\boxed{
m_\epsilon(N,t)\ge
\max\!\left\{
\left\lfloor\log_2(N+1)\right\rfloor,
\left\lfloor B\log_2R_r-h_\epsilon\right\rfloor-1
\right\}.}
```

If the second term is nonpositive, it contributes no improvement; a zero-qubit code is always available. If $`B=0`$, the bound uses only the first term.

To verify the constants, choose $`\delta=\epsilon/2`$ in the guard bound and $`\eta=\epsilon^2/16`$ in the coding theorem. The prescribed $`r`$ gives $`p_{\mathrm{bad}}\le\epsilon/2`$, while

```math
2\sqrt\eta=\frac\epsilon2,
\qquad
2\log_2\frac1\eta
=8+4\log_2\frac1\epsilon=h_\epsilon.
```

When $`s=\lfloor B\log_2R_r-h_\epsilon\rfloor\ge1`$, the general theorem gives the second term with total error at most $`\epsilon`$. The first term follows by using the entire fully symmetric space, on which every permutation acts as the identity. An arbitrary $`2^{\lfloor\log_2(N+1)\rfloor}`$-dimensional subspace of that space is therefore protected exactly at all times. The maximum combines two alternative codes; it does not add their payloads.

## Scaling that follows from the finite bound

The logarithms in the guard use the natural base; payload logarithms use base two. For $`r\ge1`$,

```math
R_r\ge\frac73.
```

Writing $`a=\log_2(7/3)`$, the block part of the theorem is at least

```math
\frac{aN}{8r}-a-h_\epsilon-2.
```

Since

```math
r\le2\sqrt{\gamma t x}+\frac{2x}{3}+1,
```

there are absolute positive constants $`c,C`$ such that

```math
m_\epsilon(N,t)
\ge
c\frac{N}{\sqrt{\gamma t\ln(4N/\epsilon)}
+\ln(4N/\epsilon)}
-C\left(1+\log_2\frac1\epsilon\right).
```

This last display is a lower bound with constants, not an assertion that the capacity has the displayed order. The exact all-time symmetric-space code remains available whenever it is better.

For fixed $`\epsilon`$ and fixed $`0\lt\zeta\lt2`$, choosing

```math
\gamma t=N^{2-\zeta}
```

gives

```math
m_\epsilon(N,t)
=\Omega\!\left(\frac{N^{\zeta/2}}{\sqrt{\ln N}}\right)
```

as an achievable payload. It is polynomially larger than the $`O(\log N)`$ invariant-space baseline. The storage interval grows algebraically with $`N`$, and no action occurs during that interval.

More generally, at fixed error the block construction is parametrically larger than $`\log N`$ whenever

```math
\gamma t=o\!\left(\frac{N^2}{(\ln N)^3}\right).
```

This sufficient window follows from the global union bound. It is not claimed to be optimal.

## What the bound establishes

The achieved result is a finite-$`N`$, finite-time, one-use code with a uniform reference guarantee. Known mixing results give a complementary late-time $`O(\log N)`$ upper bound; their attribution and assumptions are kept with that separate argument. The construction and those inherited bounds place the lifetime of a payload above the invariant-space scale near the diffusive exponent, up to logarithmic factors.

The theorem does not give the optimal payload at each time, a quantum-capacity cutoff profile, an efficient encoder or decoder, or protection against additional generic single-site noise. Those claims are not used in its proof or its scientific consequence.
