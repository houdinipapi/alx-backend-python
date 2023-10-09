import asyncio

async def print_hello():
    await asyncio.sleep(1)  # Simulate an asynchronous task
    print("Hello")

async def print_world():
    await asyncio.sleep(1)  # Simulate another asynchronous task
    print("World")

async def main():
    await asyncio.gather(print_hello(), print_world())

if __name__ == "__main__":
    asyncio.run(main())