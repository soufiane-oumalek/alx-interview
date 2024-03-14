#!/usr/bin/python3
"""0. Prime Game.
"""


def isWinner(x, nums):
    """given the winner of a the prime game.
    """
    if x < 1 or not nums:
        return None
    marias = 0
    bens = 0
    num = max(nums)
    primes = [True for _ in range(1, num + 1, 1)]
    primes[0] = False
    for i, prime in enumerate(primes, 1):
        if i == 1 or not prime:
            continue
        for j in range(i + i, num + 1, i):
            primes[j - 1] = False
    for _, num in zip(range(x), nums):
        primes_count = len(list(filter(lambda x: x, primes[0: num])))
        bens += primes_count % 2 == 0
        marias += primes_count % 2 == 1
    if marias == bens:
        return None
    return 'Maria' if marias > bens else 'Ben'
