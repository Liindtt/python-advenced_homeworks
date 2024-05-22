import asyncio


async def add_one(limit):
    num = 0
    while num < limit:
        num += 1
        print(f"{num=}")
        await asyncio.sleep(1)


async def main():
    first = asyncio.create_task(add_one(12))
    second = asyncio.create_task(add_one(8))
    await first
    await second


asyncio.run(main())
