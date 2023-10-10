#!/usr/bin/env python3

"""
A coroutine that takes no argument.
"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Asynchronous generator that yields random numbers between 0 and 10.

    Yields:
        float: A random number between 0 and 10.

    This coroutine loops 10 times, waiting for 1 second asynchronously
    on each iteration.
    """

    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
