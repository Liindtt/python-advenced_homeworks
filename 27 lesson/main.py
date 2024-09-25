import asyncio
import random
from aiohttp import ClientSession


async def make_request(delay):
    async with ClientSession() as session:
        url = f"https://httpbin.org/delay/{delay}"
        try:
            async with session.get(url, timeout=6) as response:
                status_code = response.status
                print(f"Status code for delay {delay}: {status_code}")
        except asyncio.TimeoutError:
            print(f"Request for delay {delay} timed out")


async def main():
    tasks = []
    for _ in range(20):
        delay = random.randint(0, 10)
        task = asyncio.create_task(make_request(delay))
        tasks.append(task)

    for task in asyncio.as_completed(tasks):
        await task

if __name__ == "__main__":
    asyncio.run(main())
