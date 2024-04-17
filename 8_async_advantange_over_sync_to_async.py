import asyncio
import time

import aiohttp
import requests
from asgiref.sync import sync_to_async


def fetch_data_sync(url):
    response = requests.get(url)
    return response.text


async def fetch_data_async(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


async def main_async():
    start_time = time.time()

    # Fetch data from multiple URLs concurrently using pure asynchronous coroutines
    urls = ["https://jsonplaceholder.typicode.com/posts/1" for _ in range(200)]  # Increase the number of URLs
    tasks = [fetch_data_async(url) for url in urls]
    await asyncio.gather(*tasks)

    end_time = time.time()
    print(f"Total time taken for pure asynchronous execution: {end_time - start_time} seconds")


async def main_mixed():
    start_time = time.time()

    # Fetch data from multiple URLs concurrently using mixed execution
    urls = ["https://jsonplaceholder.typicode.com/posts/1" for _ in range(200)]  # Same number of URLs as main_async
    tasks = []
    for idx, url in enumerate(urls):
        if idx % 2 == 0:
            tasks.append(fetch_data_async(url))
        else:
            tasks.append(sync_to_async(fetch_data_sync)(url))  # Using synchronous function converted to asynchronous

    await asyncio.gather(*tasks)

    end_time = time.time()
    print(f"Total time taken for mixed execution: {end_time - start_time} seconds")


# Run the event loop for pure asynchronous execution
asyncio.run(main_async())
# Run the event loop for mixed execution
asyncio.run(main_mixed())
