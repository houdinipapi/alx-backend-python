#!/usr/bin/env python3

"""
Run time for four parallel comprehensions.
"""

import asyncio
import time

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """
    Measure the total runtime of executing async_comprehension
    four times in parallel.

    Returns:
        float: Total runtime in seconds.
    """
    start_time = time.time()
    tasks = [async_comprehension() for i in range(4)]
    await asyncio.gather(*tasks)
    end_time = time.time()
    return end_time - start_time
