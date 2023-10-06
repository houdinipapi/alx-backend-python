#!/usr/bin/env python3

"""
A type-annotated function.
"""

from typing import Mapping, Any, TypeVar, Union

T = TypeVar("T")


def safely_get_value(
    dct: Mapping, key: Any, default: Union[T, None] = None
) -> Union[Any, T]:
    """
    Safely gets a value from a dictionary.

    Args:
        dct (Mapping): A mapping (dictionary-like object).
        key (Any): The key to look up in the dictionary.
        default (Optional[T]): The default value to return
        if the key is not found (default is None).

    Returns:
        Union[Any, T]: The value associated with the
        key if it exists, or the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
