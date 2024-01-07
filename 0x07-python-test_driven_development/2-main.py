#!/usr/bin/python3
"""
This module defines a function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number.

    Args:
        matrix (list of lists): The matrix to be divided.
        div (int or float): The number to divide the matrix by.

    Returns:
        list of lists: The new matrix with elements rounded to 2 decimal places.

    Raises:
        TypeError: If the matrix is not a list of lists of integers or floats.
        TypeError: If each row of the matrix does not have the same size.
        TypeError: If div is not a number.
        ZeroDivisionError: If div is equal to 0.
    """
    # Validate matrix
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Validate each row has the same size
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Validate div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Validate div is not equal to 0
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Divide matrix elements by div and round to 2 decimal places
    new_matrix = [[round(element / div, 2) for element in row] for row in matrix]

    return new_matrix
