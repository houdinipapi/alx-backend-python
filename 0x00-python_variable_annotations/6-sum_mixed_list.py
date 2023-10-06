#!/usr/bin/env python3

"""
A type-annotated function.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Takes a list of integers and floats as input and
    returns their sum as a float.

    Args:
        mxd_lst (List[Union[int, float]]): A list containing
        integers and floats.

    Returns:
        float: The sum of the numbers in the input list.
    """
    return float(sum(mxd_lst))
