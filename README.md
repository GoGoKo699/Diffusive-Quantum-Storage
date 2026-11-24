# Diffusive Quantum Storage

**How much quantum information can a spin chain store while neighboring carriers exchange places?**

Consider $`N`$ qubits on an open path. Independent rate-$`\gamma`$ SWAP clocks exchange adjacent spins. Encoding and decoding occur at the endpoints of the storage interval. During storage, the chain evolves without intervention or an accessible record of the swaps.

At fixed half-diamond error $`0\lt\epsilon\lt1/8`$, a deterministic endpoint code gives

```math
m_\epsilon(N,t)\ge c_\epsilon\frac{N}{1+\sqrt{\gamma t}}-C,
```

with a positive error-dependent constant and an absolute additive constant. This is a one-use guarantee for arbitrary inputs entangled with a reference. The [finite-size theorem](science/mean_label_escape.md) gives explicit constants and block counts.

## Storage regimes

| Storage regime | Supported payload |
|---|---|
| Fixed $`\gamma t`$ | Achievable payload grows linearly with $`N`$ at fixed error |
| $`\gamma t=N`$ | Achievable $`\Omega_\epsilon(\sqrt N)`$ logical qubits |
| $`\gamma t=N^{2-\zeta}`$, fixed $`0\lt\zeta\lt2`$ | Achievable $`\Omega_\epsilon(N^{\zeta/2})`$ logical qubits |
| $`\gamma t\ge(1+a)N^2\ln N/(2\pi^2)`$, fixed $`a\gt0`$, asymptotically | Inherited all-code upper bound $`O(\log N)`$ |

The [exact symmetric-space code](science/model.md#exact-all-time-baseline) stores $`\lfloor\log_2(N+1)\rfloor`$ qubits at every time. The [late-time bound](science/late_time.md) follows from classical adjacent-shuffle mixing and Schur–Weyl symmetry. The optimal intermediate-time payload remains open.

## How the code works

Each spatial block uses the all-zero state and an excitation spread uniformly across the block. The root-mean-square displacement of a carrier is at most $`\sqrt{2\gamma t}`$. The mean fraction of carriers that leave their assigned block bounds the average error weight on the corresponding logical qubits. An outer stabilizer code corrects errors of sufficiently small weight, including correlated errors. The Pauli average in the proof selects fixed endpoint operations. The deployed code uses neither a stored key nor a permutation record.

The [original guarded construction](science/storage_theorem.md) gives a second finite-size lower bound, based on keeping interior cores. Its proof controls a single event across all the cores. The new code removes the resulting square-root logarithmic loss at polynomial storage times. Either code can be selected from its finite numerical guarantee. All physical spins, including any unused sites, count toward $`N`$. Endpoint circuit size, temporary width and runtime are unoptimized.

Start with the [model](science/model.md), [proofs and interpretation](science/README.md), and [related work](references/RELATED_WORK.md).

## Learn the project

The educational anchor is **John Watrous, *The Theory of Quantum Information* (2018)**. The [worked examples](learning/WORKED_EXAMPLES.md), [Watrous bridge](learning/WATROUS_BRIDGE.md), and [30 milestones](learning/MILESTONES.md) connect the two constructions to quantum channels, coding and reference-preserving error.

## Reproduce the finite checks

```bash
python -m pip install -r requirements.txt
python verification/checks.py
python verification/check_mean_label_escape.py
```

The [verification guide](verification/README.md) describes the small-system checks and their scope.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
