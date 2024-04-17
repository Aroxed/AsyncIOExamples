import asyncio


async def greet(name, delay):
    await asyncio.sleep(delay)
    print(f"Hello, {name}!")


async def main():
    # Create two coroutines with different delays
    coro1 = greet("Alice", 1)  # the order is not guaranteed!
    coro2 = greet("Bob", 1)

    # Gather both coroutines to run concurrently
    await asyncio.gather(coro1, coro2)


# Run the event loop
asyncio.run(main())
