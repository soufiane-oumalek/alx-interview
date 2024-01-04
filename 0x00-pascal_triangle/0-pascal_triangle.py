#!/usr/bin/python3
"""
Pascal's Triangle
"""


def pascal_triangle(n):
    """
        return a list of integers that
        is representing the Pascal
        triangle of number
    """
    if n <= 0:
        return []
    tri = [[1]]
    for i in range(1, n):
        r = [1]
        for j in range(1, i):
            r.append(tri[i - 1][j - 1] + tri[i - 1][j])
        r.append(1)
        tri.append(r)
    return tri
