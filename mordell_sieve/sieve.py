"""Small educational modular sieve for Mordell curves y^2 = x^3 + k.

This module is intentionally simple. It searches for integer points in a bounded
interval and uses modular quadratic-residue tests as a filter before doing the
exact integer-square check.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import isqrt
from typing import Iterable, List, Sequence, Tuple

Point = Tuple[int, int]


@dataclass(frozen=True)
class SieveStats:
    """Basic statistics for a bounded sieve run."""

    k: int
    x_min: int
    x_max: int
    primes: Tuple[int, ...]
    total_x_values: int
    candidates_after_sieve: int
    integer_points_found: int


def is_square(n: int) -> bool:
    """Return True if n is a non-negative perfect square."""
    if n < 0:
        return False
    r = isqrt(n)
    return r * r == n


def quadratic_residues_mod_p(p: int) -> set[int]:
    """Return the set of quadratic residues modulo p."""
    if p <= 1:
        raise ValueError("modulus p must be greater than 1")
    return {(a * a) % p for a in range(p)}


def passes_modular_sieve(x: int, k: int, primes: Iterable[int]) -> bool:
    """Check whether x^3 + k is a quadratic residue modulo every chosen prime."""
    value = x * x * x + k
    for p in primes:
        residues = quadratic_residues_mod_p(p)
        if value % p not in residues:
            return False
    return True


def find_integer_points(
    k: int,
    x_min: int,
    x_max: int,
    primes: Sequence[int] = (5, 7, 11, 13, 17, 19),
    return_stats: bool = False,
) -> List[Point] | tuple[List[Point], SieveStats]:
    """Find integer points on y^2 = x^3 + k for x_min <= x <= x_max.

    The method is a bounded search. It does not compute rank, prove finiteness,
    or make any BSD-related claim.
    """
    if x_min > x_max:
        raise ValueError("x_min must be <= x_max")

    points: List[Point] = []
    candidates_after_sieve = 0

    for x in range(x_min, x_max + 1):
        if not passes_modular_sieve(x, k, primes):
            continue
        candidates_after_sieve += 1
        rhs = x * x * x + k
        if is_square(rhs):
            y = isqrt(rhs)
            points.append((x, y))
            if y != 0:
                points.append((x, -y))

    points.sort()

    stats = SieveStats(
        k=k,
        x_min=x_min,
        x_max=x_max,
        primes=tuple(primes),
        total_x_values=x_max - x_min + 1,
        candidates_after_sieve=candidates_after_sieve,
        integer_points_found=len(points),
    )

    if return_stats:
        return points, stats
    return points
