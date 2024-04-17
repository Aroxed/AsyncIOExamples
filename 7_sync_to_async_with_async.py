import asyncio
import time
from asgiref.sync import sync_to_async


def greet_sync(name, delay):
    time.sleep(delay)
    print(f"Hello, {name}!")


async def main():
    # Wait for Alice's greeting first
    await sync_to_async(greet_sync)("Alice", 1)

    # Now greet Bob asynchronously
    await greet("Bob", 1)


async def greet(name, delay):
    await asyncio.sleep(delay)
    print(f"Hello, {name}!")


# Run the event loop
asyncio.run(main())
