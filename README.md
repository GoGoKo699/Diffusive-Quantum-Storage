# Diffusive Quantum Storage

**Local random swaps can erase position labels while leaving a growing quantum memory available for long times.**

Consider $`N`$ qubits on a path, with an unobserved rate-$`\gamma`$ SWAP clock on every adjacent edge. Encoding takes place before storage and decoding afterwards. No control, reset, measurement or protected auxiliary memory acts during storage.

Guarded symmetric blocks give a finite-time, one-use code with an error guarantee that includes arbitrary entanglement with an external reference. At fixed small error, its achievable logical payload satisfies

```math
m_\epsilon(N,t)
\ge c\frac{N}{\sqrt{\gamma t\ln N}+\ln N}-C_\epsilon,
```

in the asymptotic regime, with explicit finite-size constants and integer rounding in the [storage theorem](science/storage_theorem.md). The independent exact symmetric-space code retains $`\lfloor\log_2(N+1)\rfloor`$ qubits at every time.

## What this enables

| Storage regime | Supported payload |
|---|---|
| $`\gamma t=N`$ | Achievable $`\Omega(\sqrt{N/\ln N})`$ logical qubits at fixed small error |
| $`\gamma t=N^{2-\zeta}`$, fixed $`0<\zeta<2`$ | Achievable $`\Omega(N^{\zeta/2}/\sqrt{\ln N})`$ logical qubits |
| $`\gamma t\ge(1+a)N^2\ln N/(2\pi^2)`$, fixed $`a>0`$, asymptotically | Inherited mixing tools give an all-code $`O(\log N)`$ late-time upper bound |

The first two rows are achievable bounds. They do not give the optimal payload at every time. The late-time comparison uses established adjacent-shuffle mixing and Schur-Weyl symmetry; it does not assert a quantum-capacity cutoff.

## Why guards help

Each input block lies in its fully symmetric spin space, so its internal permutations are harmless. At decoding, only its central core is retained. If every retained output site originated inside its own block, the full channel on all cores is exactly a product of symmetric partial traces, including reference correlations. A diffusion bound controls the probability that this condition fails. Finite-size coding across the blocks then recovers the logical input unconditionally.

The favorable event is used only in the proof. The protocol receives no particle trajectory, permutation record or success flag.

## Read the result

Start with the [model and resources](science/model.md), then the [finite-time theorem](science/storage_theorem.md). The [scientific index](science/README.md) connects the guard argument, one-shot coding, late-time comparison and physical interpretation. [Related work](references/RELATED_WORK.md) separates the new finite-time construction from established exchange-error correction, symmetric loss, consensus and mixing results.

All $`N`$ stored spins, including guards and unused sites, are counted. Endpoint gates, transient width and runtime are unoptimized. The present theorem covers the specified SWAP noise; generic additional local noise needs a separate analysis. An efficient encoder or decoder is not supplied.

## Reproduce the finite checks

```bash
python -m pip install -r requirements.txt
python verification/checks.py
```

The [verification guide](verification/README.md) explains the exact small-system calculations, random-subspace consistency tests and bound arithmetic. These checks support the proof within their declared scope and do not simulate a large quantum memory.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
