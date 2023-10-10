#!/usr/bin/env python3

"""
How to write an asynchronous generator
"""

import asyncio


# Define an asynchronous generator function
async def async_generator():
    for i in range(5):
        # Simulate an asynchronous operation, e.g.,
        # fetching data from a network
        await asyncio.sleep(1)

        # Yield a value asynchronously
        yield i


# Create an asynchronous generator object
async_gen = async_generator()


# Iterate over the values produced by the generator
async def main():
    async for value in async_gen:
        print(value)


# Run the event loop to execute the asynchronous generator
asyncio.run(main())
