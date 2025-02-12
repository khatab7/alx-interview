#!/usr/bin/python3
"""
rotate 2D matrix
"""


def rotate_2d_matrix(matrix):
    """
    two dimension matrix 90 degrees clockwise
    """
    ln = len(matrix)
    for i in range(int(ln / 2)):
        y = (ln - i - 1)
        for j in range(i, y):
            x = (ln - 1 - j)

            tmp = matrix[i][j]
            matrix[i][j] = matrix[x][i]

            matrix[x][i] = matrix[y][x]

            matrix[y][x] = matrix[j][y]
            matrix[j][y] = tmp