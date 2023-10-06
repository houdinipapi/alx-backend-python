#!/usr/bin/env python3

"""
A type-annotated function.
"""

from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Returns the first element of a sequence if it exists,
    or None if the sequence is empty.

    Args:
        lst (Sequence[Any]): A sequence (can be of any type).

    Returns:
        Union[Any, NoneType]: The first element of the sequence,
        if it exists, or None if the sequence is empty.
    """
    if lst:
        return lst[0]
    else:
        return None
