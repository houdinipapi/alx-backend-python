#!/usr/bin/env python3

"""
A type-annotated function.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Takes a string and an int or float as input and returns a tuple.

    The first element of the tuple is the string `k`.
    The second element is the square of the int/float `v` as a float.

    Args:
        k (str): A string.
        v (Union[int, float]): An integer or float.

    Returns:
        Tuple[str, float]: A tuple containing the string `k` and
        the square of `v` as a float.
    """
    return (k, float(v**2))
