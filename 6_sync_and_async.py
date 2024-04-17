"""The purpose of sync_to_async is to convert synchronous operations (typically blocking operations) into
asynchronous operations. This is important in asynchronous web frameworks like Django Channels, where you want to
avoid blocking the event loop while waiting for I/O-bound operations like querying a database.

Event Loop: Within the asynchronous wrapper function, sync_to_async creates an event loop (if one doesn't already
exist) and runs the synchronous function within that event loop.

Concurrency: While the synchronous function is running within the event loop, other asynchronous tasks can continue
waiting when sync function is finished"""
import asyncio
import time


def greet_sync(name, delay):
    time.sleep(delay)
    print(f"Hello, {name}!")


async def greet_async(name, delay):
    await asyncio.sleep(delay)
    print(f"Hello, {name}!")


async def main():
    # Wait for Alice's greeting first
    greet_sync("Alice", 1)  # Synchronous call

    # Now greet Bob asynchronously
    await greet_async("Bob", 1)


# Run the event loop
asyncio.run(main())
