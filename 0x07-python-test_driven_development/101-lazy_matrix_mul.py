#!/usr/bin/python3
"""Module that multiplies 2 matrices
"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Function that multiplies 2 matrices.
    Args:
        m_a (list): First input.
        m_b (list): Second input.
    Raise:
        TypeError
        ValueError
    Return: Matrix Product.
    """
    result = np.matmul(m_a, m_b)
    return result
