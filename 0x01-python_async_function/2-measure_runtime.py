#!/usr/bin/env python3

"""
Measure the runtime
"""

import asyncio
import time
from typing import List

# Import the wait_n coroutine from the previous file
wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the total execution time for wait_n(n, max_delay)
    and return total_time / n.

    Args:
        n (int): Number of times to call wait_n.
        max_delay (int): Maximum delay in seconds for each call to wait_n.

    Returns:
        float: Average execution time per call to wait_n.
    """
    start_time = time.time()

    # Use asyncio.run() to run the wait_n coroutine n times
    for _ in range(n):
        asyncio.run(wait_n(1, max_delay))

    end_time = time.time()
    total_time = end_time - start_time

    # Calculate and return the average execution time
    return total_time / n
