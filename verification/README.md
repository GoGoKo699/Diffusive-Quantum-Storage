# Numerical verification

Run from the repository root with Python and NumPy:

```bash
python verification/checks.py
python verification/check_mean_label_escape.py
```

The first script writes [`results.json`](results.json). The seed and NumPy version are recorded. Change the seed or sampling size explicitly with `--seed` and `--samples`; choose another output path with `--output`.

## What is checked

| Check | Independent finite calculation | Scope |
|---|---|---|
| Symmetric split | Construct Dicke-state Clebsch–Gordan coefficients; diagonalize the reference–environment Choi state; compute both output marginals | Lengths 2 through 9, retained sizes from half the block to one below its length |
| Guarded reduction | Permute the full eight-qubit physical state, then trace guards; compare against the fixed partial trace | A jointly encoded input entangled with an external reference; valid permutations include exchanges between discarded regions |
| Haar coding | Sample random input subspaces and calculate their reference–environment states | Consistency with the exact second-moment expression and its trace-norm bound; sampling uncertainty is reported |
| Expurgation | Construct a noisy channel with complex Kraus traces; compare its Stinespring operator with the common-environment identity; restrict to the lower half of its error spectrum | Checks the complex-conjugation convention and dimension-independent operator estimate |
| Walk tail | Exponentiate the finite absorbing random-walk generator by symmetric diagonalization | Compare first-exit probabilities with the stated stopped Bernstein upper bound |
| Finite parameters | Evaluate guard widths, block counts and the resulting logical-qubit bound | Arithmetic examples; large registers are not simulated |

The deliberately invalid permutation changes the reduced state substantially. This confirms that the guarded-reduction check exercises the membership condition rather than merely comparing identical states.

## Mean label escape checks

The second script runs two independent finite calculations using NumPy.

- It enumerates all permutations for four block layouts on four to six sites. It prepares the target reference and encoded qubit jointly, averages the other block inputs over vacuum and a uniform excitation, and applies the physical permutation before tracing the environment. Across 3,888 block and permutation cases it checks the recovered Bell infidelity bound and exact recovery when no target carrier leaves.
- It diagonalizes the finite reflecting path generator. Across 6,520 interval and time cases on paths of 2–16 sites it checks the expected number of escaping labels against the diffusion bound.

The finite checks exercise the inner channel and the one-tag diffusion estimate. The outer-code and subcode guarantees follow from the [analytical proof](../science/mean_label_escape.md).

## Recorded run

The default seed is `20261113`, with 1,024 random subspaces for each Haar example. All checks passed. The largest symmetric-isometry, marginal, Choi-spectrum or collision-factor discrepancy was below `5e-16`. The largest good-permutation Frobenius discrepancy was below `8e-17`; the invalid permutation had trace distance approximately `0.781`. Both sampled Haar second moments agreed with the analytical expression within their reported sampling uncertainty. The expurgation Hilbert–Schmidt identity agreed within `1.4e-15`. None of the tested first-exit probabilities exceeded its Bernstein bound.

The finite-parameter examples intentionally retain cases where the displayed lower bound is zero after coding overhead. This means that this conservative construction certifies no additional payload in that example. The global symmetric encoding still retains its independent `floor(log2(N+1))` noiseless baseline.

## Limits

These finite calculations do not prove the block-channel identity, coding theorem, random-walk bound, asymptotic scaling or novelty claim. Their proofs and assumptions are given in [`science/`](../science/). The random-subspace check is statistical, and its six-standard-error acceptance tolerance is a consistency check.

No efficient encoder or decoder is implemented here. The script does not test additional physical noise, imperfect controls, a device, or a matching finite-time converse. Its large-parameter rows are calculations of theorem bounds, not numerical demonstrations of large quantum memories.

## Hosted mathematical review

The [read-only hosted check](hosted/README.md) compares every Markdown page at the exact proposed commit with GitHub's actual mathematical rendering at wide and narrow viewports. Its captured output supports a separate visual review; it does not replace the scientific checks above.
