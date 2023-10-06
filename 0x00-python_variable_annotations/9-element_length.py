#!/usr/bin/env python3

"""
A type-annotated function.
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Takes an iterable of sequences as input and
    returns a list of tuples.

    Each tuple contains a sequence from the input and its
    corresponding length.

    Args:
        lst (Iterable[Sequence]): An iterable of sequences.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples,
        each containing a sequence and its length.
    """
    return [(i, len(i)) for i in lst]
