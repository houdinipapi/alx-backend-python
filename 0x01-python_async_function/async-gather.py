import asyncio


async def coroutine1():
    await asyncio.sleep(2)
    print("Coroutine 1 finished")


async def coroutine2():
    await asyncio.sleep(1)
    print("Coroutine 2 finished")


async def main():
    await asyncio.gather(coroutine1(), coroutine2())


if __name__ == "__main__":
    asyncio.run(main())
