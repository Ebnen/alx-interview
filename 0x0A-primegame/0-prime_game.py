#!/usr/bin/python3
"""Prime Game"""


def isWinner(x, nums):
    """Prime Game"""
    if x == 0 or x == 1:
        return None

    n = max(nums)
    primes = [True for _ in range(max(n + 1, 2))]
    primes[0], primes[1] = False, False
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False

    primes_count = sum(1 for i in primes if i)
    winner = 0
    for i in range(x):
        winner += sum(1 for j in nums if primes[j])
        if winner % 2 == 0:
            return "Ben"
        return "Maria"
