#!/usr/bin/env python3

"""
Tasks
"""

import asyncio

# Import the wait_random coroutine from 0-basic_async_syntax
wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create and return an asyncio.Task for wait_random(max_delay).

    Args:
        max_delay (int): Maximum delay in seconds for wait_random.

    Returns:
        asyncio.Task: A task representing the
        execution of wait_random(max_delay).
    """
    return asyncio.create_task(wait_random(max_delay))
