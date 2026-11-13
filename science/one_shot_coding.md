# A finite-size code with a uniform reference guarantee

[Guarded reduction](guarded_blocks.md) · [Storage theorem](storage_theorem.md)

The guarded construction reduces the favorable part of one physical memory use to a tensor product of symmetric partial traces. This page constructs a code for that finite product and then converts its entanglement-fidelity guarantee to the half-diamond criterion. No limit of repeated memory uses is required.

## The symmetric partial-trace isometry

Set $`q=L-k`$. Splitting the first $`k`$ and last $`q`$ physical factors restricts to an isometry

```math
W_L:V_L\longrightarrow V_k\otimes V_q.
```

Its receiver channel is $`\Phi_{L\to k}`$ and its complementary channel is $`\Phi_{L\to q}`$. This is the established symmetrized partial-trace channel associated with universal cloning; see Lemm and Wilde, [Phys. Rev. A 96, 012304 (2017)](https://doi.org/10.1103/PhysRevA.96.012304), Eq. (7).

For $`B\ge1`$ blocks, define the dimensions

```math
d=(L+1)^B,\qquad
b=(k+1)^B,\qquad
e=(q+1)^B.
```

Write $`\mathcal T=\Phi_{L\to k}^{\otimes B}`$ and let $`\mathcal N`$ be its complementary channel. The maximally mixed input is $`\pi_A=I_A/d`$. Covariance under independent $`SU(2)`$ rotations of the blocks and irreducibility of the symmetric spin representations imply

```math
\mathcal T(\pi_A)=\frac{I_B}{b},
\qquad
\mathcal N(\pi_A)=\frac{I_E}{e}.
```

If $`\omega_{RE}`$ is the normalized Choi state of $`\mathcal N`$, purification of the Stinespring-Choi state gives

```math
\mathrm{Tr}\omega_{RE}^2=\frac1b.
```

Indeed, its complementary receiver marginal is $`I_B/b`$, so its nonzero spectrum is flat of rank $`b`$.

## Finite-size random-subspace bound

For every integer $`1\le K\le d`$, there is a $`K`$-dimensional encoding subspace and a decoder such that

```math
F_e\!\left(\frac{I_K}{K},
\mathcal D\circ\mathcal T\circ\mathcal V\right)
\ge 1-\left(\frac{Ke}{b}\right)^{1/2}.
```

Here $`F_e`$ is the overlap of the recovered reference/output state with the normalized maximally entangled $`K`$-state, and $`\mathcal V`$ is an isometric encoder. This is a specialization of Klesse's finite-size random-code theorem, [Phys. Rev. A 75, 062315 (2007)](https://doi.org/10.1103/PhysRevA.75.062315), Sec. IV B, Eqs. (28) and (30). The receiver channel has Kraus rank at most $`e`$, and $`\lVert\mathcal T(\pi_A)\rVert_2=1/\sqrt b`$.

For completeness, the following direct Haar calculation proves the needed specialization and makes its dimension dependence explicit.

Choose the first $`K`$ columns $`|u_a\rangle`$ of a Haar unitary on the $`d`$-dimensional input space. Encoding half a maximally entangled state gives the reference/environment state

```math
\sigma_{RE}
=\frac1K\sum_{a,c=1}^K
|a\rangle\langle c|\otimes
\mathcal N(|u_a\rangle\langle u_c|).
```

The two Haar contractions needed for its purity are

```math
A:=\mathbb E\mathrm{Tr}
\mathcal N(|u_a\rangle\langle u_a|)^2
=\frac{d}{d+1}\left(\frac1e+\frac1b\right),
```

and, for $`a\ne c`$,

```math
C:=\mathbb E\mathrm{Tr}\!\left[
\mathcal N(|u_a\rangle\langle u_c|)
\mathcal N(|u_c\rangle\langle u_a|)\right]
=\frac{d^2/b-d/e}{d^2-1}.
```

These follow respectively from the Haar averages $`(I+F)/[d(d+1)]`$ and $`(F-I/d)/(d^2-1)`$. Therefore

```math
\mathbb E\mathrm{Tr}\sigma_{RE}^2
=\frac AK+\frac{K-1}{K}C,
```

which gives the exact identity

```math
\mathbb E\left\lVert\sigma_{RE}
-\frac{I_R}{K}\otimes\frac{I_E}{e}\right\rVert_2^2
=\frac{Kd-1}{K(d^2-1)}
\left(\frac db-\frac1e\right).
```

Cauchy-Schwarz on the $`Ke`$-dimensional reference/environment space and Jensen's inequality imply

```math
\begin{aligned}
\mathbb E\left\lVert\sigma_{RE}
-\frac{I_R}{K}\otimes\frac{I_E}{e}\right\rVert_1
&\le
\left[\frac{Kd-1}{d^2-1}
\left(\frac{de}{b}-1\right)\right]^{1/2}\\
&\le \left(\frac{Ke}{b}\right)^{1/2}.
\end{aligned}
```

The last inequality uses $`K\le d`$. At least one encoding subspace attains the average bound. Uhlmann's theorem gives a recovery from decoupling; the fidelity/trace-distance inequalities give entanglement infidelity at most the displayed trace error. This proves the finite-size coding statement.

In particular, for $`0\lt\eta\lt1`$ and

```math
K\le \eta^2\left(\frac{k+1}{q+1}\right)^B,
```

the ideal product-loss channel has a code with entanglement fidelity at least $`1-\eta`$. This bound remains valid when $`L`$ grows with $`N`$.

## Expurgation to a half-diamond guarantee

High entanglement fidelity on the maximally mixed input does not by itself assert a uniform guarantee on that entire code. The following subcode argument supplies the required guarantee with a dimension loss of at most a factor of two.

Let $`\mathcal M`$ be the recovered channel on an even-dimensional $`K`$-code, with

```math
F_e(I_K/K,\mathcal M)\ge1-\eta.
```

Take a Stinespring isometry $`W=\sum_j A_j\otimes|j\rangle`$ for $`\mathcal M`$. Define

```math
a_j=\frac{\mathrm{Tr}A_j}{K},
\qquad
F=\sum_j|a_j|^2=F_e(I_K/K,\mathcal M),
\qquad
|v\rangle=\frac1{\sqrt F}\sum_j a_j|j\rangle.
```

Since $`F\ge1-\eta\gt0`$, this environment vector is well defined. The positive input operator

```math
H=(W-I_K\otimes|v\rangle)^\dagger
(W-I_K\otimes|v\rangle)
```

satisfies

```math
\mathrm{Tr}H
=2K(1-\sqrt F)\le2K\eta.
```

Let $`P`$ project onto the lowest $`K/2`$ eigenvectors of $`H`$. At least $`K/2`$ eigenvalues are no larger than $`4\eta`$, so

```math
\lVert(W-I_K\otimes|v\rangle)P\rVert_\infty
\le2\sqrt\eta.
```

This is an operator-norm bound and is unchanged by tensoring an arbitrary reference. Channels induced by two isometries differ in diamond norm by at most twice their operator-norm distance. Restrict the input to $`P`$, and compress the decoder output back to that subspace. Explicitly, if $`J:\mathbb C^{K/2}\to\mathbb C^K`$ has image $`P`$, use the channel

```math
\mathcal C_J(X)
=J^\dagger XJ+
\mathrm{Tr}[(I-P)X]\,|0\rangle\langle0|.
```

It fixes the ideal subcode and cannot increase diamond distance. The resulting $`K/2`$-dimensional code obeys

```math
\frac12\lVert\mathcal C_J\circ\mathcal M\circ
(J\,\cdot\,J^\dagger)-\mathrm{id}_{K/2}\rVert_\diamond
\le2\sqrt\eta.
```

This bound includes arbitrary input entanglement with an external reference. The general equivalence between entanglement and subspace transmission is established in Barnum, Knill and Nielsen, [IEEE Trans. Inf. Theory 46, 1317 (2000)](https://doi.org/10.1109/18.850671). The explicit finite-size estimate above is sufficient here.

## Transfer to the physical exchange process

The [guarded reduction](guarded_blocks.md) gives half-diamond distance at most $`p_{\mathrm{bad}}`$ between the physical encoded/trimmed channel and the ideal product-loss channel. Compose both with the selected encoder, recovery, and subcode compression. The triangle inequality proves

```math
\frac12\lVert\mathcal D_{\mathrm{phys}}\circ
\mathcal E_{N,t}\circ\mathcal V_{\mathrm{phys}}
-\mathrm{id}_{K/2}\rVert_\diamond
\le p_{\mathrm{bad}}+2\sqrt\eta.
```

All ancillas used for encoding or recovery occur outside the storage interval. The proof establishes code existence; it does not supply an efficient circuit for the Haar encoding or its decoder. The [storage theorem](storage_theorem.md) chooses the finite parameters and counts the resulting logical qubits.
