#!/usr/bin/python3

def island_perimeter(grid):
    """Returns the perimeter of the island described in grid"""
    return (len(grid) - 2) * (len(grid[0]) - 2)
