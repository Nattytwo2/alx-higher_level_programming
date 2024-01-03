#!/usr/bin/python3
"""
add_integer module
Function that adds 2 integers

"""


def add_integer(a, b=98):
    """Function that adds 2 integers
    Args:
        a (int): First number.
        b (int): Second number.
    Raise: TypeError
    Return: Integer addition of a an b
    """
    if not(type(a) in [int, float]):
        raise TypeError('a must be an integer')
    if not(type(b) in [int, float]):
        raise TypeError('b must be an integer')
    return int(a) + int(b)
