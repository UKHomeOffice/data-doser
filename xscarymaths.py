# !/usr/bin/env python3
"""
I lifted this straight from: https://stackoverflow.com/a/40250841/106590
"""

__author__ = "David Morris"
__version__ = "0.1.0"
__license__ = "MIT"

import functools
import random


@functools.lru_cache(1 << 10)
def C1(n, k, a, b):
    """Counts the compositions of `n` into `k` parts bounded by `a` and `b`"""
    return C2(n - k * (a - 1), k, b - (a - 1))


def C2(n, k, b):
    """Computes C(n, k, 1, b) using binomial coefficients"""
    total = 0
    sign = +1

    for i in range(0, k + 1):
        total += sign * choose(k, i) * choose(n - i * b - 1, k - 1)
        sign = -sign

    return total


def choose(n, k):
    """Computes the binomial coefficient of (n, k)"""
    if k < 0 or k > n:
        return 0

    if k == 0 or k == n:
        return 1

    k = min(k, n - k)
    c = 1

    for i in range(k):
        c = c * (n - i) // (i + 1)
    return c


def check_pre_and_post_conditions(f):
    def wrapper(n, k, a, b):
        assert 1 <= k <= n, (n, k)
        assert 1 <= a <= b <= n, (n, a, b)
        assert k * a <= n <= k * b, (n, k, a, b)

        comp = f(n, k, a, b)

        assert len(comp) == k, (len(comp), k, comp)
        assert sum(comp) == n, (sum(comp), n, comp)
        assert all(a <= x <= b for x in comp), (a, b, comp)

        return comp

    return functools.wraps(f)(wrapper)


@check_pre_and_post_conditions
def random_restricted_composition(n, k, a, b):
    """Produces a random composition of `n` into `k` parts bounded by `a` and `b`"""
    total = C1(n, k, a, b)
    which = random.randrange(total)
    comp = []

    while k:
        for x in range(a, min(b, n) + 1):
            count = C1(n - x, k - 1, a, b)

            if count > which:
                break

            which -= count

        comp.append(x)
        n -= x
        k -= 1
    return comp
