# A guarded memory, from carrier origins to a finite bound

[Learning route](README.md) · [Model and error](../science/model.md) · [Finite-time theorem](../science/storage_theorem.md)

This example follows one construction through its geometry, quantum channel, error budget and numerical bound. The background anchor is John Watrous, [*The Theory of Quantum Information* (2018)](https://cs.uwaterloo.ca/~watrous/TQI/): reductions and purifications in §2.1.3, channel representations in §2.2.2, fidelity in §3.2, the completely bounded trace norm in §3.3.2, and permutation symmetry in §7.1. The finite-time statements below follow the repository's linked proofs.

## Two blocks of eight sites

Take a path of $`N=16`$ qubits. Encode into the symmetric space of each length-eight block. With guard width $`r=1`$, the retained core has $`k=6`$ sites:

| Block | Input sites | Retained output sites | Discarded output guards |
|---|---|---|---|
| $`A`$ | $`1,\ldots,8`$ | $`2,\ldots,7`$ | $`1,8`$ |
| $`B`$ | $`9,\ldots,16`$ | $`10,\ldots,15`$ | $`9,16`$ |

All sixteen qubits occupy the memory during storage. The guards are discarded only afterwards. The decoder chooses these output cores in advance.

Here is one possible final origin map. The second row specifies which initial carrier is found at each output site:

| Output site | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| Initial carrier | 1 | 7 | 3 | 6 | 4 | 2 | 5 | 9 |

| Output site | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 |
|---|---|---|---|---|---|---|---|---|
| Initial carrier | 8 | 15 | 11 | 14 | 12 | 10 | 13 | 16 |

Carriers 8 and 9 have crossed the block boundary. Nevertheless, every retained site of core $`A`$ originated in input block $`A`$, and the analogous statement holds for $`B`$. This is the [origin condition](../science/guarded_blocks.md#the-deterministic-channel-identity). Internal permutations act as the identity on a symmetric input, so the retained channel for this map is exactly

```math
\Phi_{8\to6}\otimes\Phi_{8\to6},
```

where $`\Phi_{8\to6}`$ traces out any two factors of a symmetric eight-qubit input. Boundary exchanges need not be absent: their effect is harmless for this map because only discarded carriers cross between blocks.

The identity holds as a linear map, including when the two block inputs are entangled with each other and with an untouched reference. It does not depend on identifying a separate quantum state for each carrier.

## An explicit input with a reference

Let $`|D_n^j\rangle`$ denote the normalized symmetric state of $`n`$ qubits with $`j`$ excitations. In particular, $`|D_n^0\rangle=|0\rangle^{\otimes n}`$ and $`|D_n^1\rangle`$ is the uniform superposition of the $`n`$ single-excitation basis states. Use the input

```math
|\Psi\rangle_{RAB}
=\frac{|0\rangle_R|D_8^0\rangle_A|D_8^0\rangle_B
       +|1\rangle_R|D_8^1\rangle_A|D_8^1\rangle_B}{\sqrt2}.
```

The reference $`R`$ is inaccessible to the decoder. Splitting a symmetric eight-qubit block into six retained and two discarded qubits gives

```math
\begin{aligned}
W|D_8^0\rangle
&=|D_6^0\rangle|D_2^0\rangle,\\
W|D_8^1\rangle
&=\frac{\sqrt3}{2}|D_6^1\rangle|D_2^0\rangle
  +\frac12|D_6^0\rangle|D_2^1\rangle.
\end{aligned}
```

After tracing the two-qubit environment, write $`P_j=|D_6^j\rangle\langle D_6^j|`$. Then

```math
\begin{aligned}
\Phi_{8\to6}(|D_8^0\rangle\langle D_8^0|)&=P_0,\\
\Phi_{8\to6}(|D_8^1\rangle\langle D_8^1|)
&=\tfrac34P_1+\tfrac14P_0,\\
\Phi_{8\to6}(|D_8^0\rangle\langle D_8^1|)
&=\tfrac{\sqrt3}{2}|D_6^0\rangle\langle D_6^1|.
\end{aligned}
```

Define $`|00\rangle=|D_6^0\rangle_A|D_6^0\rangle_B`$ and $`|11\rangle=|D_6^1\rangle_A|D_6^1\rangle_B`$. For the displayed origin map, the full reference/core output is therefore

```math
\begin{aligned}
\rho_{RAB}'=\frac12\Big[&
|0\rangle\langle0|_R\otimes P_0\otimes P_0\\
&+|1\rangle\langle1|_R\otimes
 (\tfrac34P_1+\tfrac14P_0)^{\otimes2}\\
&+\tfrac34|0\rangle\langle1|_R\otimes|00\rangle\langle11|\\
&+\tfrac34|1\rangle\langle0|_R\otimes|11\rangle\langle00|
\Big].
\end{aligned}
```

This calculation retains the off-diagonal reference correlations. The reduction to partial trace describes a quantum channel on entangled inputs, rather than only a transition rule for excitation probabilities. This input illustrates the identity; it is not the final random-subspace code promised by the theorem.

## Dimensions and the cost of a reliable code

The splitting isometry has the following dimensions:

| Register | One block | Two blocks |
|---|---|---|
| Symmetric input | $`8+1=9`$ | $`d=9^2=81`$ |
| Symmetric retained output | $`6+1=7`$ | $`b=7^2=49`$ |
| Symmetric discarded environment | $`2+1=3`$ | $`e=3^2=9`$ |

Thus the one-block receiver/environment ratio is $`7/3`$. The input occupies a nine-dimensional subspace of the $`7\times3`$ receiver/environment space; the dimensions need not multiply to nine. The ratio greater than one supplies coding room when many blocks are available. It does not certify a high-fidelity logical qubit in one small block.

The [finite-size coding proof](../science/one_shot_coding.md) states that an ideal product of $`B`$ such partial traces admits a $`K`$-dimensional code with entanglement infidelity at most $`\eta`$ whenever

```math
K\le\eta^2(7/3)^B.
```

Taking $`K=2^s`$ and retaining a half-dimensional subcode gives $`s-1`$ logical qubits with ideal half-diamond error at most $`2\sqrt\eta`$. This subcode step is needed to obtain a uniform guarantee over reference-entangled inputs; high entanglement fidelity on the original maximally mixed code does not alone provide that guarantee.

For a target half-diamond error $`\epsilon=0.05`$, the explicit theorem uses

```math
\eta=\frac{\epsilon^2}{16}=\frac1{6400},
\qquad
2\sqrt\eta=0.025,
\qquad
h_\epsilon=2\log_2\frac1\eta
=8+4\log_2 20\simeq25.2877.
```

With only two eight-site blocks, $`2\log_2(7/3)\simeq2.4448`$, which cannot pay this coding overhead. The finite-size theorem supplies no positive block-code payload at this error even for the ideal product channel. This is a limitation of the certificate, not an upper bound on the best small code. The independent whole-register symmetric code already stores $`\lfloor\log_2 17\rfloor=4`$ qubits exactly.

## Turning the origin identity into an unconditional guarantee

The decoder does not learn the displayed origin map, the clock history or whether a run satisfied any favorable event. To control the actual unobserved noise, the [guard proof](../science/guarded_blocks.md#a-favorable-event-defined-by-backward-trajectories) uses a sufficient event: every retained carrier's backward trajectory stays within distance strictly less than $`r`$ of its output site throughout storage. This implies the origin condition. It is more restrictive: the displayed internal rearrangements can satisfy the origin condition while failing this sufficient trajectory event.

The event depends only on classical clock histories, independently of the quantum input. Averaging the physical core channel gives

```math
\mathcal A_t=(1-p_{\mathrm{bad}})\Phi_{L\to k}^{\otimes B}
             +p_{\mathrm{bad}}\,\Xi,
\qquad
\frac12\lVert\mathcal A_t-\Phi_{L\to k}^{\otimes B}\rVert_\diamond
\le p_{\mathrm{bad}},
```

with

```math
p_{\mathrm{bad}}
\le\min\left\{1,
2N\exp\left[-\frac{r^2}{4\gamma t+2r/3}\right]\right\}.
```

The same decoder acts on all runs. This mixture is a proof decomposition, with no postselection, observed success flag or trajectory-dependent recovery. Contraction and the triangle inequality add the physical error to the ideal code error:

```math
\mathrm{err}_{\mathrm{physical}}
\le p_{\mathrm{bad}}+2\sqrt\eta.
```

The $`L=8,k=6,r=1`$ example illustrates channel geometry, rather than a certified global error budget. For $`N=16`$ and $`\gamma t=1`$, its stated union bound is already capped at one. The theorem's error-budget choice instead gives

```math
x=\ln\frac{4N}{\epsilon}=\ln1280\simeq7.1546,
\qquad
r=\left\lceil2\sqrt{\gamma t x}+\frac{2x}{3}\right\rceil=11.
```

Then $`L=8r=88`$ exceeds the sixteen available sites and $`B=0`$. The explicit guarded construction therefore certifies no improvement over the four-qubit exact baseline here. It does not assert that sixteen sites can store only four qubits at that time. At $`t=0`$, for example, all sixteen qubits can be stored exactly.

## Evaluating the actual finite-size theorem

For general $`N,t`$, the [explicit theorem](../science/storage_theorem.md#an-explicit-bound-with-one-error-parameter) chooses

```math
\begin{aligned}
x&=\ln(4N/\epsilon),&
r&=\left\lceil2\sqrt{\gamma t x}+\frac{2x}{3}\right\rceil,\\
L&=8r,&
k&=6r,&
B&=\lfloor N/(8r)\rfloor,&
R_r&=(6r+1)/(2r+1).
\end{aligned}
```

It guarantees $`p_{\mathrm{bad}}\le\epsilon/2`$. Its block-code payload certificate is

```math
m_{\mathrm{block}}
=\max\left\{0,
\left\lfloor B\log_2R_r-h_\epsilon\right\rfloor-1\right\}.
```

The final lower bound is the maximum of this quantity and the exact all-time baseline. The two payloads belong to alternative codes and are not added.

The following arithmetic uses $`\epsilon=0.05`$ and $`\gamma t=N`$ in every row:

| Physical sites $`N`$ | Guard $`r`$ | Blocks $`B`$ | Certified block qubits | Exact baseline | Final certified qubits |
|---|---:|---:|---:|---:|---:|
| $`2^{20}=1,048,576`$ | 8,761 | 14 | 0 | 20 | 20 |
| $`2^{28}=268,435,456`$ | 159,843 | 209 | 304 | 28 | 304 |
| $`2^{36}=68,719,476,736`$ | 2,839,674 | 3,024 | 4,766 | 36 | 4,766 |

For the middle row, for example,

```math
\begin{aligned}
x&\simeq23.79015,& L&=1,278,744,\\
R_r&=\frac{959059}{319687}\simeq2.999993744,&
B\log_2R_r&\simeq331.25653,\\
m_{\mathrm{block}}
&=\lfloor331.25653-25.28771\rfloor-1=304.
\end{aligned}
```

The bad-event upper bounds for the three rows are approximately $`0.024275`$, $`0.024936`$ and $`0.024995`$. Each is at most $`0.025`$; adding the ideal subcode error $`0.025`$ gives the target half-diamond error $`0.05`$.

These are evaluations of the theorem, not simulations of large memories or compiled devices. The same entries appear in [the finite verification record](../verification/results.json), produced by [the verification script](../verification/checks.py). All physical sites, guards and unused remainders are charged to $`N`$. Endpoint encoding and decoding costs are unoptimized. The large sizes and the inactive first-row block certificate make the finite overhead visible.

## Comparing transient storage with late times

The early and late statements use different arguments. The block construction above is an achievable lower bound. For a late-time upper bound, let $`d_N(t)`$ be total-variation distance between the adjacent-swap permutation law and the uniform permutation law. The [late-time proof](../science/late_time.md) gives, for every $`K`$-dimensional code,

```math
F_e\le\min\{1,(N+1)/K+d_N(t)\}.
```

Consequently, if half-diamond error is at most $`\epsilon=0.05`$ and $`d_N(t)\le0.01`$,

```math
\log_2K\le\log_2(N+1)-\log_2(0.94)
\simeq\log_2(N+1)+0.08927.
```

This is a finite implication whenever the stated mixing-distance hypothesis is known. For $`N=2^{28}`$, that implication allows at most 28 whole logical qubits, whereas the finite-time construction certifies 304 at $`\gamma t=N`$. This comparison does not compute a finite mixing time for that particular $`N`$.

The inherited classical mixing theorem establishes that, for fixed $`a\gt 0`$, the hypothesis $`d_N(t)\le0.01`$ eventually holds as $`N\to\infty`$ at

```math
\gamma t\ge\frac{(1+a)N^2\ln N}{2\pi^2}.
```

It supplies a late-time $`O(\log N)`$ ceiling. It does not assert a quantum-capacity cutoff at this location. Between this comparison and the constructive lower bound, logarithmic and payload-dependent gaps remain.

One precise lifetime consequence fixes a threshold $`A\log_2N`$ with $`A\gt 1`$, a fixed error $`0\lt \epsilon\lt 1/8`$, and asks for the last storage time $`T_{A,\epsilon}(N)`$ at which that threshold is achievable. The [lifetime argument](../science/interpretation.md#a-quantified-lifetime-statement) gives, for sufficiently large $`N`$,

```math
c_{A,\epsilon}\frac{N^2}{\gamma(\ln N)^3}
\le T_{A,\epsilon}(N)
\le C_\epsilon\frac{N^2\ln N}{\gamma}.
```

Thus $`\ln[\gamma T_{A,\epsilon}(N)]/\ln N\to2`$. The exponent concerns this specified logarithmic payload threshold. It does not fix optimal logarithmic factors, the lifetime of every polynomial payload, or robustness to extra single-site noise.
