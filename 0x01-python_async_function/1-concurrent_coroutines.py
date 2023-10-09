#!/usr/bin/env python3

"""
Executing multiple coroutines at the same time with async.
"""

import asyncio
from typing import List

# Import the wait_random coroutine from the previous file
wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronously spawn wait_random n times with the specified max_delay.

    Args:
        n (int): Number of times to spawn wait_random.
        max_delay (int): Maximum delay in seconds for each call to wait_random.

    Returns:
        List[float]: List of delays (float values) in ascending order.
    """
    delays = []

    # Create a list of tasks by spawning wait_random n times
    tasks = [wait_random(max_delay) for _ in range(n)]

    # Wait for all tasks to complete and gather their results
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
