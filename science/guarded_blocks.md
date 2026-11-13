# From local exchanges to symmetric loss

[Model](model.md) · [Finite-size coding](one_shot_coding.md) · [Storage theorem](storage_theorem.md)

The noise moves quantum carriers without revealing their trajectories. This page proves a deterministic channel identity for favorable trajectories and bounds the probability of the others. Favorable trajectories are used only in the proof: the encoder and decoder receive no trajectory, success flag, or measurement record.

## Predetermined blocks and cores

Partition the first $`BL`$ sites of the path into $`B=\lfloor N/L\rfloor`$ consecutive blocks of length $`L`$. Initialize any remaining sites in a fixed state. Let

```math
V_L=\mathrm{Sym}^{L}(\mathbb C^2),
\qquad \dim V_L=L+1.
```

The encoded input is supported on $`V_L^{\otimes B}`$. It may be entangled between blocks and with an arbitrary external reference. For an integer guard width $`r\ge1`$ with $`2r\lt L`$, retain only the central $`k=L-2r`$ output sites of each block. All other output sites are discarded. These cores are fixed before the noise acts.

Write $`\Phi_{L\to k}`$ for ordinary partial trace from the symmetric input space to any fixed ordered set of $`k`$ tensor factors. Its output is supported on $`V_k`$. Permutation symmetry makes the selected ordered set immaterial.

## The deterministic channel identity

Fix one complete realization of the Poisson clocks, and hence its final permutation. Suppose every retained output site has its original label in the corresponding input block. Call this the **origin condition**.

Under the origin condition, the encoded-and-trimmed channel is exactly

```math
\Phi_{L\to k}^{\otimes B}.
```

To see this, let $`S_j`$ be the ordered set of original labels reaching core $`j`$. It consists of $`k`$ distinct sites of input block $`j`$. Complete the ordered identification of $`S_j`$ with a fixed $`k`$-site subset to a permutation of all $`L`$ sites in that input block. Every such permutation acts as the identity on $`V_L`$. Consequently selecting $`S_j`$, in its realized output order, induces exactly $`\Phi_{L\to k}`$ on that block.

This is an equality of linear maps on the full operator space, not a statement only about product input states. Expanding an arbitrary operator in a tensor-product operator basis therefore proves the tensor-product identity even for entangled blocks and after tensoring an arbitrary reference identity channel. The unused input sites are fully traced out under the origin condition and contribute no retained output.

## A favorable event defined by backward trajectories

For a retained output site $`y`$, trace its carrier backwards through the realized clocks over the interval $`[0,t]`$. Reversing a family of independent homogeneous Poisson clocks preserves its law. Thus the backward tagged trajectory has the same law as a continuous-time nearest-neighbor walk on the physical path, with rate $`\gamma`$ along each available incident edge.

Use the following sufficient event: every retained backward trajectory stays at displacement strictly less than $`r`$ from its starting site throughout the interval. Each retained site is at least $`r`$ lattice steps from a physical endpoint. Up to the first displacement $`+r`$ or $`-r`$, its walk is therefore identical to the full-line walk stopped on reaching one of those displacements. There is no uncharged reflection or infinite-chain approximation.

On this event, every tagged carrier remains inside its own block. In particular its original label belongs to that block, so the origin condition holds. Counting a trajectory that leaves and later returns as unfavorable only makes the probability bound more conservative.

## A tail bound valid at all times

Let $`X_s`$ be the full-line walk started at zero, with independent right and left jumps at rate $`\gamma`$. Its exponential moment is

```math
\mathbb E e^{\lambda X_s}
=\exp\!\left[2\gamma s(\cosh\lambda-1)\right].
```

For $`0\lt\lambda\lt3`$,

```math
\cosh\lambda-1
\le \frac{\lambda^2}{2(1-\lambda/3)}.
```

The inequality follows by comparing the power series; the right side also has nonnegative odd terms. Stop the exponential martingale at the first positive displacement $`r`$ or at time $`t`$. Optional stopping and the preceding bound give

```math
\Pr\!\left\{\sup_{0\le s\le t}X_s\ge r\right\}
\le
\exp\!\left[-\lambda r+
\frac{\gamma t\lambda^2}{1-\lambda/3}\right].
```

For $`\gamma t\gt0`$, choose $`\lambda=r/(2\gamma t+r/3)`$. Apply the same bound to $`-X_s`$ to obtain

```math
\Pr\!\left\{\sup_{0\le s\le t}|X_s|\ge r\right\}
\le
2\exp\!\left[-\frac{r^2}{4\gamma t+2r/3}\right].
```

At $`\gamma t=0`$ the failure probability is zero, so the same upper bound remains valid. A union bound over the $`Bk\le N`$ retained output sites yields

```math
p_{\mathrm{bad}}
\le
\min\!\left\{1,
2N\exp\!\left[-\frac{r^2}{4\gamma t+2r/3}\right]
\right\}.
```

No independence between tagged trajectories is assumed. Their strong correlations under the interchange process are compatible with this union bound.

For any prescribed $`0\lt\delta\lt1`$, put

```math
x=\ln\frac{2N}{\delta},
\qquad
r=\left\lceil 2\sqrt{\gamma t x}+\frac{2x}{3}\right\rceil.
```

Then $`r^2\ge x(4\gamma t+2r/3)`$, and hence $`p_{\mathrm{bad}}\le\delta`$. The additive logarithmic term is needed for a bound uniform in time. Keeping only the square-root term is justified only in a regime where it dominates.

## The physical channel is close to product loss

Let $`\mathcal A_t`$ denote the channel obtained by including the symmetric input space into the physical path, applying the noise, and retaining the predetermined cores. Conditioning mathematically on the favorable clock event gives

```math
\mathcal A_t
=(1-p_{\mathrm{bad}})\Phi_{L\to k}^{\otimes B}
+p_{\mathrm{bad}}\,\Xi,
```

where $`\Xi`$ is a channel on the same input and physical output spaces. If the unfavorable event has probability zero, choose $`\Xi`$ arbitrarily. The favorable event is independent of the quantum input, which is essential for this channel decomposition.

It follows that

```math
\frac12\left\lVert\mathcal A_t-
\Phi_{L\to k}^{\otimes B}\right\rVert_\diamond
\le p_{\mathrm{bad}}.
```

The ideal product-loss output is included into the physical core Hilbert spaces in this expression. The bound holds for all reference-entangled inputs. It survives arbitrary encoding and decoding by contraction of the diamond norm. The [coding page](one_shot_coding.md) uses this fact to transfer an ideal product-loss code to the actual unobserved exchange process.

The random-walk process and concentration tools are established ingredients. The contribution used here is the origin-based channel reduction: the number of boundary clock rings is irrelevant once the retained carriers' origins satisfy the stated condition.
