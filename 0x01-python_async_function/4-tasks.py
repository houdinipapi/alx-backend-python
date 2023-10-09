#!/usr/bin/env python3

"""
Tasks
"""

import asyncio
from typing import List

# Import the wait_random coroutine
wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create and return an asyncio.Task for wait_random(max_delay).

    Args:
        max_delay (int): Maximum delay in seconds for wait_random.

    Returns:
        asyncio.Task: A task representing the execution of
        wait_random(max_delay).
    """
    return asyncio.create_task(wait_random(max_delay))


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronously spawn task_wait_random n times with the specified max_delay.

    Args:
        n (int): Number of times to spawn task_wait_random.
        max_delay (int): Maximum delay in seconds for each call
        to task_wait_random.

    Returns:
        List[float]: List of delays (float values) in ascending order.
    """
    delays = []

    # Create a list of tasks by spawning task-wait_random n times
    tasks = [task_wait_random(max_delay) for _ in range(n)]

    # Wait for all tasks to complete and gather their results
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
