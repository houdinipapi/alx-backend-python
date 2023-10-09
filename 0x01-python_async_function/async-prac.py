import asyncio

# Synchronous programming
# def foo():
#     return


# foo()
# print("Papi")


async def main():
    print("Papi")
    # await foo("text")
    task = asyncio.create_task(foo("text"))
    # await task
    await asyncio.sleep(2)
    print("Finished")


async def foo(text):
    print(text)
    await asyncio.sleep(1)


asyncio.run(main())
