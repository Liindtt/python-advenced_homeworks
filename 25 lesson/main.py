import asyncio
from time import perf_counter


async def add_one(limit):
    num = 0
    while num < limit:
        print(f"{num=}")
        num += 1
        await asyncio.sleep(1)


async def main():
    start_time = perf_counter()
    first = asyncio.create_task(add_one(12))
    second = asyncio.create_task(add_one(8))
    await first
    await second
    print(f"Program ends in: {perf_counter() - start_time:.2f} seconds")


asyncio.run(main())
