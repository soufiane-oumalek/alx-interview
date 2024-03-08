#!/usr/bin/python3
"""0. Island Perimeter
"""


def island_perimeter(grid):
    """returns the perimeter of the island described in grid
    """
    perimeter = 0
    if type(grid) != list:
        return 0
    num = len(grid)
    for i, row in enumerate(grid):
        meter = len(row)
        for j, cell in enumerate(row):
            if cell == 0:
                continue
            edges = (
                i == 0 or (len(grid[i - 1]) > j and grid[i - 1][j] == 0),
                j == meter - 1 or (meter > j + 1 and row[j + 1] == 0),
                i == num - 1 or (len(grid[i + 1]) > j and grid[i + 1][j] == 0),
                j == 0 or row[j - 1] == 0,
            )
            perimeter += sum(edges)
    return perimeter
