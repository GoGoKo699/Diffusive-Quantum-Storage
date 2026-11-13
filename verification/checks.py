#!/usr/bin/env python3
"""Finite numerical checks for diffusive storage; NumPy and Python only."""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np


def symmetric_split(length: int, retained: int) -> np.ndarray:
    """Return V[w,b,e] for the normalized Dicke-state split isometry."""
    erased = length - retained
    v = np.zeros((length + 1, retained + 1, erased + 1), dtype=complex)
    for w in range(length + 1):
        for b in range(retained + 1):
            e = w - b
            if 0 <= e <= erased:
                v[w, b, e] = math.sqrt(
                    math.comb(retained, b) * math.comb(erased, e)
                    / math.comb(length, w)
                )
    return v


def tensor_split(v: np.ndarray, blocks: int) -> np.ndarray:
    if blocks == 1:
        return v
    if blocks != 2:
        raise ValueError("This finite check uses one or two blocks.")
    d, b, e = v.shape
    return np.einsum("ibe,jcf->ijbcef", v, v).reshape(d * d, b * b, e * e)


def partial_re(state: np.ndarray) -> np.ndarray:
    """Trace B out of a pure vector with axes R,B,E."""
    r, b, e = state.shape
    return np.einsum("ibe,jbf->iejf", state, state.conj()).reshape(r * e, r * e)


def haar_columns(rng: np.random.Generator, dimension: int, columns: int) -> np.ndarray:
    z = rng.normal(size=(dimension, columns)) + 1j * rng.normal(size=(dimension, columns))
    q, r = np.linalg.qr(z)
    phases = np.diag(r)
    return q * (phases / np.abs(phases)).conj()[None, :]


def trace_norm_hermitian(a: np.ndarray) -> float:
    return float(np.abs(np.linalg.eigvalsh((a + a.conj().T) / 2)).sum())


def check_split_spectra() -> dict:
    max_isometry = max_marginal = max_spectrum = max_collision = 0.0
    configurations = []
    for length in range(2, 10):
        for retained in range((length + 1) // 2, length):
            v = symmetric_split(length, retained)
            d, b, e = v.shape
            flat = v.reshape(d, b * e)
            max_isometry = max(max_isometry, float(np.max(np.abs(flat @ flat.conj().T - np.eye(d)))))
            state = v / math.sqrt(d)
            rho_re = partial_re(state)
            rho_b = np.einsum("ibe,ice->bc", state, state.conj())
            rho_e = np.einsum("ibe,ibf->ef", state, state.conj())
            max_marginal = max(max_marginal, float(np.max(np.abs(rho_b - np.eye(b) / b))),
                               float(np.max(np.abs(rho_e - np.eye(e) / e))))
            spectrum = np.linalg.eigvalsh(rho_re)
            expected = np.r_[np.zeros(d * e - b), np.ones(b) / b]
            max_spectrum = max(max_spectrum, float(np.max(np.abs(spectrum - expected))))
            collision = e * float(np.trace(rho_re @ rho_re).real)
            max_collision = max(max_collision, abs(collision - e / b))
            configurations.append([length, retained])
    passed = max(max_isometry, max_marginal, max_spectrum, max_collision) < 2e-12
    return {"passed": passed, "length_range": [2, 9],
            "retained_range": "ceil(L/2) through L-1",
            "max_isometry_entry_error": max_isometry,
            "max_uniform_marginal_entry_error": max_marginal,
            "max_flat_choi_spectrum_error": max_spectrum,
            "max_collision_factor_error": max_collision}


def dicke_embedding(length: int) -> np.ndarray:
    out = np.zeros((2 ** length, length + 1), dtype=complex)
    for basis in range(2 ** length):
        weight = basis.bit_count()
        out[basis, weight] = 1 / math.sqrt(math.comb(length, weight))
    return out


def reduce_physical(state: np.ndarray, kept: list[int], sites: int) -> np.ndarray:
    reference = state.shape[0]
    discarded = [j for j in range(sites) if j not in kept]
    axes = [0] + [j + 1 for j in kept] + [j + 1 for j in discarded]
    a = state.reshape([reference] + [2] * sites).transpose(axes)
    a = a.reshape(reference * 2 ** len(kept), -1)
    return a @ a.conj().T


def check_good_permutations(rng: np.random.Generator) -> dict:
    length, blocks, reference = 4, 2, 2
    sites = length * blocks
    kept = [1, 2, 5, 6]
    code = rng.normal(size=(reference, length + 1, length + 1))
    code = code + 1j * rng.normal(size=code.shape)
    code /= np.linalg.norm(code)
    embedding = dicke_embedding(length)
    physical = np.einsum("rij,ai,bj->rab", code, embedding, embedding).reshape(reference, 2 ** sites)
    ideal = reduce_physical(physical, kept, sites)
    errors = []
    crossed_discarded_examples = 0
    for _ in range(80):
        origins = np.full(sites, -1, dtype=int)
        for block in range(blocks):
            outputs = [j for j in kept if j // length == block]
            origins[outputs] = rng.choice(np.arange(block * length, (block + 1) * length),
                                           size=len(outputs), replace=False)
        remaining_outputs = np.flatnonzero(origins < 0)
        remaining_origins = np.array([j for j in range(sites) if j not in origins])
        origins[remaining_outputs] = rng.permutation(remaining_origins)
        assert sorted(origins.tolist()) == list(range(sites))
        assert all(origins[j] // length == j // length for j in kept)
        crossed_discarded_examples += int(any(origins[j] // length != j // length
                                               for j in remaining_outputs))
        moved = physical.reshape([reference] + [2] * sites).transpose([0] + (origins + 1).tolist())
        actual = reduce_physical(moved.reshape(reference, -1), kept, sites)
        errors.append(float(np.linalg.norm(actual - ideal, ord="fro")))
    bad = np.arange(sites)
    bad[1], bad[5] = bad[5], bad[1]
    moved = physical.reshape([reference] + [2] * sites).transpose([0] + (bad + 1).tolist())
    bad_reduced = reduce_physical(moved.reshape(reference, -1), kept, sites)
    bad_trace_distance = trace_norm_hermitian(bad_reduced - ideal) / 2
    rho_reference = physical @ physical.conj().T
    reference_purity = float(np.trace(rho_reference @ rho_reference).real)
    passed = max(errors) < 2e-12 and bad_trace_distance > 1e-3 and reference_purity < 0.99
    return {"passed": passed, "physical_sites": sites, "block_length": length,
            "retained_sites": kept, "reference_dimension": reference,
            "max_good_permutation_frobenius_error": max(errors),
            "good_examples_with_cross_block_discarded_labels": crossed_discarded_examples,
            "deliberately_bad_permutation_trace_distance": bad_trace_distance,
            "input_reference_purity": reference_purity,
            "scope": "Generic jointly encoded pure input with external reference; finite valid permutations."}


def check_haar_identity(rng: np.random.Generator, samples: int) -> dict:
    rows = []
    for length, retained, blocks, logical in [(3, 2, 2, 2), (5, 4, 2, 2)]:
        v = tensor_split(symmetric_split(length, retained), blocks)
        d, b, e = v.shape
        target = np.eye(logical * e) / (logical * e)
        hs_values, trace_values = [], []
        for _ in range(samples):
            enc = haar_columns(rng, d, logical)
            state = np.einsum("dbe,di->ibe", v, enc) / math.sqrt(logical)
            delta = partial_re(state) - target
            hs_values.append(float(np.trace(delta @ delta).real))
            trace_values.append(trace_norm_hermitian(delta))
        expected = ((logical * d - 1) / (logical * (d * d - 1))) * (d / b - 1 / e)
        mean = float(np.mean(hs_values))
        standard_error = float(np.std(hs_values, ddof=1) / math.sqrt(samples))
        trace_mean = float(np.mean(trace_values))
        trace_bound = math.sqrt(logical * e / b)
        passed = abs(mean - expected) <= max(6 * standard_error, 1e-12)
        passed = passed and trace_mean <= trace_bound + 6 * float(np.std(trace_values, ddof=1) / math.sqrt(samples))
        rows.append({"L": length, "k": retained, "blocks": blocks, "K": logical,
                     "d_b_e": [d, b, e], "samples": samples,
                     "analytic_mean_squared_hs_error": expected,
                     "observed_mean_squared_hs_error": mean,
                     "sampling_standard_error": standard_error,
                     "observed_mean_trace_error": trace_mean,
                     "analytic_trace_error_upper_bound": trace_bound, "passed": passed})
    return {"passed": all(row["passed"] for row in rows), "examples": rows,
            "scope": "Monte Carlo consistency of the exact Haar identity; sampling does not prove it."}


def check_expurgation(rng: np.random.Generator) -> dict:
    dimension, probability, phase = 8, 0.02, 0.37
    unitary = haar_columns(rng, dimension, dimension)
    kraus = [math.sqrt(1 - probability) * np.exp(1j * phase) * np.eye(dimension),
             math.sqrt(probability) * unitary]
    amplitudes = np.array([np.trace(a) / dimension for a in kraus])
    fidelity = float(np.vdot(amplitudes, amplitudes).real)
    environment = amplitudes / math.sqrt(fidelity)
    stinespring = np.stack(kraus, axis=1).reshape(dimension * len(kraus), dimension)
    ideal = np.kron(np.eye(dimension), environment[:, None])
    delta = stinespring - ideal
    positive = delta.conj().T @ delta
    eigenvalues, eigenvectors = np.linalg.eigh(positive)
    subspace = eigenvectors[:, :dimension // 2]
    operator_error = float(np.linalg.norm(delta @ subspace, ord=2))
    eta = 1 - fidelity
    hs_identity_error = abs(float(np.trace(positive).real) - 2 * dimension * (1 - math.sqrt(fidelity)))
    trace_preserving_error = float(np.max(np.abs(sum(a.conj().T @ a for a in kraus) - np.eye(dimension))))
    passed = hs_identity_error < 2e-12 and trace_preserving_error < 2e-12
    passed = passed and operator_error <= 2 * math.sqrt(eta) + 2e-12
    return {"passed": passed, "input_dimension": dimension,
            "subcode_dimension": dimension // 2, "entanglement_fidelity": fidelity,
            "complex_environment_vector": [[float(z.real), float(z.imag)] for z in environment],
            "hs_identity_absolute_error": hs_identity_error,
            "trace_preserving_entry_error": trace_preserving_error,
            "subcode_stinespring_operator_error": operator_error,
            "proven_operator_error_upper_bound": 2 * math.sqrt(eta),
            "induced_diamond_error_upper_bound": 2 * operator_error,
            "scope": "Finite channel with nonreal Kraus traces checks conjugations and half-dimension estimate."}


def check_walk_tail() -> dict:
    rows = []
    max_excess = 0.0
    for radius in [2, 3, 5, 9, 12]:
        interior = 2 * radius - 1
        generator = -2 * np.eye(interior)
        generator += np.diag(np.ones(interior - 1), 1) + np.diag(np.ones(interior - 1), -1)
        eigenvalues, eigenvectors = np.linalg.eigh(generator)
        for time in [0.1, 0.5, 2.0, 8.0, 20.0]:
            start = np.zeros(interior)
            start[radius - 1] = 1
            evolved = eigenvectors @ (np.exp(time * eigenvalues) * (eigenvectors.T @ start))
            exit_probability = float(np.clip(1 - evolved.sum(), 0, 1))
            bound = min(1.0, 2 * math.exp(-radius * radius / (4 * time + (2 / 3) * radius)))
            max_excess = max(max_excess, exit_probability - bound)
            rows.append({"radius": radius, "gamma_t": time,
                         "absorbing_generator_exit_probability": exit_probability,
                         "bernstein_upper_bound": bound})
    return {"passed": max_excess < 2e-12, "maximum_positive_excess": max_excess,
            "examples": rows, "scope": "Exact finite absorbing walk generator; rate one per direction."}


def finite_bound_examples() -> dict:
    error = 0.05
    eta = error * error / 16
    rows = []
    for power in [20, 28, 36, 44]:
        sites = 2 ** power
        time = float(sites)
        x = math.log(4 * sites / error)
        radius = math.ceil(2 * math.sqrt(time * x) + (2 / 3) * x)
        length, retained = 8 * radius, 6 * radius
        blocks = sites // length
        ratio = (retained + 1) / (length - retained + 1)
        logical = max(0, math.floor(blocks * math.log2(ratio) - 2 * math.log2(1 / eta)) - 1)
        log_bad_bound = math.log(2 * sites) - radius * radius / (4 * time + (2 / 3) * radius)
        rows.append({"N": sites, "gamma_t": time, "target_half_diamond_error": error,
                     "radius": radius, "L": length, "k": retained, "blocks": blocks,
                     "logical_qubit_lower_bound_after_expurgation": logical,
                     "stationary_baseline_qubits": math.floor(math.log2(sites + 1)),
                     "log_bad_event_upper_bound": log_bad_bound,
                     "bad_event_bound_at_most_half_error": log_bad_bound <= math.log(error / 2) + 1e-12})
    return {"passed": all(row["bad_event_bound_at_most_half_error"] for row in rows),
            "examples": rows,
            "scope": "Arithmetic illustrations of the finite theorem, not simulated large memories or an asymptotic proof."}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=20261113)
    parser.add_argument("--samples", type=int, default=1024)
    parser.add_argument("--output", type=Path, default=Path(__file__).with_name("results.json"))
    args = parser.parse_args()
    if args.samples < 2:
        parser.error("--samples must be at least two")
    rng = np.random.default_rng(args.seed)
    checks = {"symmetric_split": check_split_spectra(),
              "good_permutation_reduction": check_good_permutations(rng),
              "haar_second_moment": check_haar_identity(rng, args.samples),
              "reference_stable_expurgation": check_expurgation(rng),
              "stopped_walk_bernstein_tail": check_walk_tail(),
              "finite_bound_arithmetic": finite_bound_examples()}
    results = {"seed": args.seed, "numpy_version": np.__version__,
               "all_passed": all(check["passed"] for check in checks.values()),
               "checks": checks,
               "limits": ["Finite checks support only their stated examples.",
                          "They do not prove asymptotics, coding existence or prior-work novelty.",
                          "They do not simulate an efficient encoder or decoder or additional physical noise."]}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(results, indent=2) + "\n")
    print(json.dumps({"all_passed": results["all_passed"], "output": str(args.output),
                      "seed": args.seed, "samples_per_haar_case": args.samples}, indent=2))
    raise SystemExit(0 if results["all_passed"] else 1)


if __name__ == "__main__":
    main()
