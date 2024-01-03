#!/usr/bin/python3
"""
print_square module
Function that prints a square with the character #.

"""


def print_square(size):
    """
    Function that prints a square with the character #.
    Args:
        size (int): First input.
    Raise: TypeError
    Return: A square with the character #.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for x in range(size):
        print('#' * size)
