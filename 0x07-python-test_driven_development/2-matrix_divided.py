#!/usr/bin/python3
"""
matrix_divided module
Function that divides all elements of a matrix

"""


def matrix_divided(matrix, div):
    """
    Function that divides all elements of a matrix
    Args:
        matrix (matrix): First input.
        div (int): Second input.
    Raise: TypeError
    Return: A new matrix
    """
    if (len(matrix) == 0 or
        matrix == [] or
        not isinstance(matrix, list) or
        not all(isinstance(row, list) for row in matrix) or
        not all(isinstance(x, (int, float))
                for x in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not(type(div) in [int, float]):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
