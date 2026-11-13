# Scientific account

**How much quantum information survives before local random exchanges mix an entire spin chain?**

The storage model has independent Poisson SWAPs on adjacent sites, arbitrary encoding and decoding at the endpoints, and no intervention during the storage interval. The contribution is a finite-size code whose payload grows polynomially with system size for algebraically long times.

| Read in order | Purpose |
|---|---|
| [Model and error](model.md) | Physical noise, one-use reference-preserving criterion and counted resources |
| [Storage theorem](storage_theorem.md) | Explicit finite-size bound, integer rounding and scaling |
| [Guarded blocks](guarded_blocks.md) | Deterministic channel identity and uniform tagged-walk bound |
| [One-shot coding](one_shot_coding.md) | Symmetric loss, finite random coding and uniform subcode recovery |
| [Late-time bound](late_time.md) | Inherited mixing and symmetry tools give the eventual logarithmic ceiling |
| [Physical interpretation](interpretation.md) | Mechanism, lifetime exponent, assumptions and remaining gaps |

The proofs credit inherited tools in place. [Related work](../references/RELATED_WORK.md) gives the model-level comparisons; [verification](../verification/README.md) supplies finite reproducible checks and their limits.
