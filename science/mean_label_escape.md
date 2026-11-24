# Passive storage from mean label escape

[Model](model.md) · [Guarded-block bound](storage_theorem.md) · [Source comparison](../references/RELATED_WORK.md)

Unobserved exchanges move excitation amplitudes between storage blocks. A block can still retain most of a logical qubit even when some of its carriers crossed a boundary. A code across blocks turns the mean amount of leakage into a guarantee for the full quantum memory. The proof uses the complete exchange channel, with all correlations between blocks intact.

## Finite bound for arbitrary random permutations

Partition $`BL`$ of the $`N`$ sites into $`B\ge4`$ disjoint assigned blocks $`I_1,\ldots,I_B`$ of size $`L\ge1`$. Prepare each unused site in the vacuum. Let $`\pi`$ be a random permutation of all $`N`$ sites, with $`\pi(i)`$ the destination of the label initially at $`i`$. Define the number of departures from block $`j`$ and the mean escape fraction by

```math
u_j(\pi)=|\pi(I_j)\setminus I_j|,\qquad
q=\frac{1}{BL}\sum_{j=1}^B \mathbb E_\pi u_j(\pi).
```

If $`30q\lt1`$, there are deterministic endpoints storing $`\lfloor B/4\rfloor-1`$ logical qubits with unconditional half-diamond error at most

```math
2\sqrt{30q}.
```

The law of $`\pi`$ can have arbitrary correlations. The code is selected for the given channel and can depend on its law. Each use has the same fixed endpoints. No trajectory or permutation record enters either endpoint, and no extra memory carrier or classical key is retained through storage. The bound protects an unknown payload entangled with any inaccessible reference.

## The logical channel of one block

Encode a qubit in an $`L`$-site block as

```math
|0\rangle\longmapsto|0^L\rangle,\qquad
|1\rangle\longmapsto |W_L\rangle
=\frac1{\sqrt L}\sum_{i=1}^L|1_i\rangle.
```

Here $`|1_i\rangle`$ has one excitation, at site $`i`$. The block decoder compresses the output onto the same two-dimensional subspace and sends the orthogonal complement to the logical vacuum. This is a trace-preserving channel. Let $`\mathcal M`$ be the full $`B`$-qubit channel given by these inner encoders, storage, and block decoders.

To compute its marginal Bell fidelity $`F_j`$, feed half of a normalized Bell pair into block $`j`$ and the maximally mixed logical state into every other block. Keep the reference and decoded output of block $`j`$. These are precisely the two-system marginals of the normalized Choi state of $`\mathcal M`$, because that state is formed from a product of Bell pairs. The Bell inputs here define a channel diagnostic. The storage protocol uses its outer-coded logical inputs.

Fix $`\pi`$ for this diagnostic and put $`u=u_j(\pi)`$. Exactly $`L-u`$ sites of the output block came from its own input block. Each of the remaining $`u`$ sites came from another block or from the unused tail. The state on these incoming sites is independent of the test block and commutes with their total excitation number. Indeed, each other input is the equal mixture of vacuum and its one-excitation state, which commutes with excitation number, and partial trace and permutations preserve this property. The unused tail is in vacuum. Every incoming site has expected excitation at most $`1/(2L)`$. Consequently the incoming state has probability at most $`u/(2L)`$ of lying outside the vacuum, since the excitation-number operator dominates the projection onto its nonzero sectors. The vacuum sector is one-dimensional, so substituting the vacuum changes the incoming state by at most $`u/(2L)`$ in trace distance. The decoded Bell overlap changes by at most that amount under this substitution.

With the incoming sites set to vacuum, tracing out the departed sites attenuates the surviving single-excitation amplitude by $`\sqrt{(L-u)/L}`$. Compressing the surviving uniform mode onto $`|W_L\rangle`$ attenuates it by the same factor again. The combined qubit channel is amplitude damping with transmission amplitude $`a=(L-u)/L`$ and vacuum output on loss. Its Kraus operators are $`|0\rangle\langle0|+a|1\rangle\langle1|`$ and $`\sqrt{1-a^2}|0\rangle\langle1|`$. The case $`u=L`$ gives the vacuum-replacement channel directly. Its normalized Bell overlap is $`(1+a)^2/4=(1-u/(2L))^2`$, so its Bell infidelity is at most $`u/L`$.

Restoring the incoming sites and averaging over $`\pi`$ gives

```math
1-F_j\le \frac{3}{2L}\mathbb E_\pi u_j(\pi).
```

For example, take two length-two blocks and transpose a single site from each. The first block retains one of its own sites. With vacuum at the incoming site the Bell overlap is $`9/16`$. With the actual incoming marginal $`(3/4)|0\rangle\langle0|+(1/4)|1\rangle\langle1|`$, the overlaps conditional on the incoming vacuum and excitation are $`9/16`$ and $`3/16`$, giving $`15/32`$ overall. The bound gives an infidelity at most $`3/4`$, in agreement with the actual $`17/32`$.

## Correlated errors and deterministic endpoints

The outer step uses the marginal Bell fidelity, Pauli averaging, and fixed-key subcode argument from [Inhomogeneous Collective Memory, Sections 6–9](https://github.com/GoGoKo699/Inhomogeneous-Collective-Memory/blob/b6bbf3cae33b300d0c793628e168616dc4919bdc/science/storage_theorem.md#6-global-pauli-twirling-and-correlated-error-correction). Its input here is the exchange-specific estimate above. Unlike a marginal channel on the original physical block, that estimate accounts for other blocks' carriers entering the block.

Average the maps $`\mathrm{Ad}_P\circ\mathcal M\circ\mathrm{Ad}_P`$ over all $`B`$-qubit tensor-product Paulis, with phases ignored. In the normalized Choi state this kills off-diagonal Pauli terms in the product Bell basis. The averaged channel is thus a probability distribution on Pauli strings, with possible correlations across every block. If $`W`$ is the number of nonidentity positions in a random string from this distribution, the probability of a nonidentity at $`j`$ is $`1-F_j`$. This holds because the local Bell reference/output projector is diagonal in the product Bell basis. Therefore

```math
\mathbb E W=\sum_j (1-F_j)\le \frac32 Bq.
```

There exists a stabilizer code on $`B`$ qubits encoding $`k=\lfloor B/4\rfloor`$ qubits with distance at least $`2d+1`$, where $`d=\lfloor B/20\rfloor`$. To see this, conjugate a fixed $`[[B,k]]`$ stabilizer by a uniformly random Clifford. Every fixed nonidentity Pauli string belongs to the conjugated normalizer with probability $`(2^{B+k}-1)/(4^B-1)\lt 2^{-(B-k)}`$, by transitivity on nonidentity Paulis. The number of strings of weight at most $`2d`$ is at most $`2^{B(h_2(1/10)+(1/10)\log_2 3)}`$, by the binomial entropy bound and $`2d\le B/10`$. Here $`h_2`$ is binary entropy in bits. Since $`h_2(1/10)+(1/10)\log_2 3\lt3/4`$ and $`B-k\ge3B/4`$, there is a choice of stabilizer with no nonidentity normalizer element of weight at most $`2d`$. A distance-$`2d+1`$ code corrects every error of weight at most $`d`$ using a fixed recovery.

With that recovery the probability of an uncorrectable Pauli in the averaged channel is bounded by

```math
\Pr(W\ge d+1)\le \frac{(3/2)Bq}{d+1}\le30q.
```

It follows that the recovered averaged channel has entanglement fidelity at least $`1-30q`$ on the maximally mixed $`k`$-qubit code input. Entanglement fidelity for that input is linear in the channel. Therefore some single $`P`$ gives at least this fidelity with the same outer recovery. Fix that $`P`$ in the encoder and decoder. Apply the [Stinespring subcode lemma](one_shot_coding.md#expurgation-to-a-half-diamond-guarantee) with $`\eta=30q`$. It loses one logical qubit and gives half-diamond error at most $`2\sqrt{30q}`$; at $`q=0`$, fidelity one already gives the identity channel. The selected Pauli and subcode are parts of the specified endpoints. This existence argument gives no runtime estimate for selecting them or compiling the complete endpoints.

## A crossover between local leakage and the global guard event

Take $`B=80`$, $`L=768`$, and mark one central site in each block. In each history swap the marked sites of one uniformly chosen pair of distinct blocks. Exactly two blocks lose one label, so $`q=2/(80\cdot768)=1/30720`$. The theorem certifies 19 logical qubits at half-diamond error at most $`1/16`$. The permutation-invariant fully symmetric subspace on these 61,440 sites certifies 15 logical qubits exactly.

Every history violates the [origin condition](guarded_blocks.md#the-deterministic-channel-identity) for predetermined aligned cores containing the marked sites. The guard argument on that partition therefore gives no small-error comparison with the ideal product of symmetric partial traces. The mean-escape bound remains small because it measures the number of labels that leave, averaged over all assigned sites. This example uses the arbitrary permutation law of the theorem. The path result next uses the displacement of tagged labels to bound the same quantity.

## Diffusive storage on an open path

Take $`I_j`$ to be consecutive intervals, and write $`\tau=\gamma t`$. Each tagged label moves as a reflecting nearest-neighbor walk on the path, regardless of the other labels. It can be represented by folding an integer walk of displacement $`S`$ with independent left and right Poisson counts of mean $`\tau`$. The folding map $`\{1,\ldots,2N\}\to\{1,\ldots,N\}`$ is $`a\mapsto a`$ on $`1\le a\le N`$ and $`a\mapsto2N+1-a`$ on $`N+1\le a\le2N`$, extended periodically. It is 1-Lipschitz on the integers. Its doubled endpoints turn the outward jump into a null transition and give the path's rate-$`\gamma`$ inward jump.

For a common integer displacement $`s`$, only starts within $`|s|`$ of an end of an interval can leave it under the fold. At most $`2|s|`$ initial sites of that interval qualify. Using the common displacement here sums the one-label marginals, rather than specifying a common realization of the interchange process. Thus every interval has

```math
\mathbb E_\pi u_j(\pi)\le2\mathbb E|S|\le2\sqrt{2\tau},
\qquad q\le\frac{2\sqrt{2\tau}}{L}.
```

For any $`0\lt\epsilon\lt1/8`$, choose

```math
L=\max\!\left\{1,\left\lceil\frac{240\sqrt{2\gamma t}}{\epsilon^2}\right\rceil\right\},
\qquad B=\left\lfloor\frac NL\right\rfloor.
```

When $`B\ge4`$, the theorem gives $`30q\le\epsilon^2/4`$ and stores $`\lfloor B/4\rfloor-1`$ logical qubits at error at most $`\epsilon`$. When $`B\lt4`$, use the zero-qubit option for this formula. Together with the exact symmetric-space code, this proves

```math
m_\epsilon(N,t)\ge
\max\left\{\lfloor\log_2(N+1)\rfloor,\ \lfloor B/4\rfloor-1\right\}.
```

In particular, at fixed error the new construction gives at least $`c_\epsilon N/(1+\sqrt{\gamma t})-C`$ qubits, for a constant $`c_\epsilon\gt0`$ and an absolute $`C`$. At $`\gamma t=N^{2-\zeta}`$ with fixed $`0\lt\zeta\lt2`$, it gives an achievable payload of order at least $`N^{\zeta/2}`$. This improves the guaranteed payload by a factor of order $`\sqrt{\ln N}`$ over the earlier guarded scaling in that regime. The new bound certifies growth above the logarithmic invariant-space scale for $`\gamma t=o(N^2/(\ln N)^2)`$. At small sizes the finite guarded or symmetric-space bound can give a larger certified payload. Any of the three codes can be chosen for a specified exposure.

The intermediate-time converse remains open. The [late-time comparison](late_time.md) still starts from the separate mixing estimate, and the endpoint decoder can depend on the exposure. This result concerns unobserved exchanges on the specified path, with all physical sites charged and general CPTP endpoint operations.
