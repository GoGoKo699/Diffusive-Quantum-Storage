from itertools import permutations, product

import numpy as np


def check_block_marginals(n, length):
    blocks = [tuple(range(i, i + length)) for i in range(0, n - length + 1, length)]
    w = np.zeros(1 << length)
    w[[1 << i for i in range(length)]] = length**-0.5
    vacuum = np.eye(1 << length)[0]
    orthogonal = np.eye(1 << length) - np.outer(w, w) - np.outer(vacuum, vacuum)
    counts = 0
    for perm in permutations(range(n)):
        for target in blocks:
            other = [block for block in blocks if block != target]
            environment = tuple(i for i in range(n) if i not in target)
            crossing = sum(perm[i] not in target for i in target)
            full_fidelity = 0.0
            for occupations in product((0, 1), repeat=len(other)):
                basis = [(0, 1.0)]
                for block, occupied in zip(other, occupations):
                    if occupied:
                        basis = [
                            (bits | (1 << perm[j]), weight / np.sqrt(length))
                            for bits, weight in basis
                            for j in block
                        ]
                amplitude = np.zeros((2, 1 << length, 1 << len(environment)))
                for bits, weight in basis:
                    states = [(0, bits, weight / np.sqrt(2))]
                    states.extend(
                        (1, bits | (1 << perm[j]), weight / np.sqrt(2 * length))
                        for j in target
                    )
                    for ref, mask, value in states:
                        out = sum(((mask >> j) & 1) << i for i, j in enumerate(target))
                        env = sum(((mask >> j) & 1) << i for i, j in enumerate(environment))
                        amplitude[ref, out, env] += value
                a0, a1 = amplitude
                overlap = vacuum @ a0 + w @ a1
                full_fidelity += (overlap @ overlap + np.sum(a0 * (orthogonal @ a0))) / 2
            full_fidelity /= 2 ** len(other)
            assert 1 - full_fidelity <= 1.5 * crossing / length + 1e-12
            if crossing == 0:
                assert abs(full_fidelity - 1.0) <= 1e-12
            counts += 1
    return counts


def check_heat_content():
    counts = 0
    for n in range(2, 17):
        generator = np.zeros((n, n))
        for x in range(n - 1):
            generator[x, x + 1] = generator[x + 1, x] = 1
        generator -= np.diag(generator.sum(axis=1))
        eigenvalues, eigenvectors = np.linalg.eigh(generator)
        for time in (0.0, 0.01, 0.1, 0.5, 1.0, 4.0, 16.0, 64.0):
            heat = (eigenvectors * np.exp(time * eigenvalues)) @ eigenvectors.T
            for start in range(n):
                for stop in range(start + 1, n + 1):
                    escaped = heat[start:stop, :start].sum() + heat[start:stop, stop:].sum()
                    assert escaped <= 2 * np.sqrt(2 * time) + 1e-12
                    counts += 1
    return counts


if __name__ == "__main__":
    cases = [(4, 2), (5, 2), (6, 2), (6, 3)]
    print("Permutation/block Choi tests:", sum(check_block_marginals(*case) for case in cases))
    print("Tagged-walk interval heat-content tests:", check_heat_content())
