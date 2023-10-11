#!/usr/bin/env python3
"""
Async Comprehensions
"""

from asyncio import sleep
from random import uniform
from typing import AsyncGenerator, Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Asynchronous generator that yields random numbers between 0 and 10.

    Yields:
        float: A random number between 0 and 10.

    This coroutine loops 10 times, waiting for 1 second asynchronously
    on each iteration.
    """
    for _ in range(10):
        await sleep(1)
        yield uniform(0, 10)
