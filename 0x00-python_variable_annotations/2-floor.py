#!/usr/bin/env python3

"""
A type-annotated functiion.
"""

import math


def floor(n: float) -> int:
    """
    Returns the floor of a floating-point number as an integer.

    Args:
        n (float): The input float nuber.

    Returns:
        int: The floor value of `n`.
    """
    return math.floor(n)
