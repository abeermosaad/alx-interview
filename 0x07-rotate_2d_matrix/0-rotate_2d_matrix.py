#!/usr/bin/python3
"""Rotate a 2D matrix by 90 degrees"""


def rotate_2d_matrix(matrix: list):
    """Rotate a 2D matrix by 90 degrees"""
    matrix[:] = [list(row) for row in zip(*matrix[::-1])]
