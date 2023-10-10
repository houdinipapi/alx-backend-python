#!/usr/bin/env python3

"""
How to type-annotate generators
"""

from typing import Generator


# Define a generator function with type annotations
def count_up_to(n: int) -> Generator[int, None, None]:
    i = 1
    while i <= n:
        yield i
        i += 1


# Create a generator
gen = count_up_to(5)

# Iterate through the generator and get type checking benefits
for num in gen:
    print(num)

# Type check the generator function's return type
reveal_type(count_up_to)
