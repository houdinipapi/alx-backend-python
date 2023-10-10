#!/usr/bin/env python3

"""
How to use async comprehensions
"""

import asyncio


# Define an asynchronous function that simulates an async operation
async def async_operation(x):
    await asyncio.sleep(1)
    return x * 2


# Use an async comprehension to collect results of async operations in a list
async def main():
    numbers = [1, 2, 3, 4, 5]
    results = [await async_operation(num) for num in numbers]
    print(results)


# Run the event loop to execute the async comprehension
asyncio.run(main())
