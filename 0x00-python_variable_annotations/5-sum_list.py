#!/usr/bin/env python3

"""
A type-annotated function.
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Takes a list of floats as input and returns their sum as a float.

    Args:
        input_list (List[float]): A list of floating-point numbers.

    Returns:
        float: the sum of the numbers in the input list.
    """
    return sum(input_list)
