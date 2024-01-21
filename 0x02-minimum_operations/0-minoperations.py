#!/usr/bin/python3
'''The minimum operations'''


def minOperations(n):
    '''method that calculates the fewest number of operations'''

    if n < 2:
        return 0

    operations = 0
    r = 2

    while r <= n:
        if n % r == 0:
            operations += r
            n //= r
            r -= 1
        r += 1

    return operations
