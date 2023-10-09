#!/usr/bin/env python3

import asyncio
import random

"""
The basics of async
"""


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronously wait for a random delay between
    0 and max_delay seconds (inclusive).

    Args:
        max_delay (int): Maximum delay in seconds (default is 10).

    Returns:
        float: The random delay in seconds.
    """
    random_delay = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)
    return random_delay
