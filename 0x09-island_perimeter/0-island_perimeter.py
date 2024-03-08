#!/usr/bin/python3
"""Island Perimeter"""


def island_perimeter(grid):
    """Returns the perimeter of the island described in grid"""
    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                cnt = 0
                if j > 0 and grid[i][j - 1] == 1:
                    cnt += 1
                if j < len(grid[i]) - 1 and grid[i][j + 1] == 1:
                    cnt += 1
                if i > 0 and grid[i - 1][j] == 1:
                    cnt += 1
                if i < len(grid) - 1 and grid[i + 1][j] == 1:
                    cnt += 1
                perimeter += 4 - cnt
    return perimeter
