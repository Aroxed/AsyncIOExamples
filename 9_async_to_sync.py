"""Event Loop: Within the synchronous wrapper function, async_to_sync creates an event loop (if one doesn't already
exist) and runs the asynchronous function within that event loop.
Blocking Wait: The synchronous wrapper function then waits for the asynchronous function to complete. This means that
the synchronous code will be blocked until the asynchronous operation finishes."""
import asyncio
import time

from asgiref.sync import async_to_sync


async def async_function():
    print("async_function - 1")
    await asyncio.sleep(3)
    print("async_function - 2")


def sync_function():
    print("sync_function - 1")
    time.sleep(1)
    print("sync_function - 2")
    async_to_sync(async_function)() # Crea
    print("sync_function - 3")
    time.sleep(1)
    print("sync_function - 4")


sync_function()
