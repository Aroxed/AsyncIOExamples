import asyncio


async def greet(name, delay):
    await asyncio.sleep(delay)
    print(f"Hello, {name}!")


async def main():
    # Create coroutines with the same delays
    coro1 = greet("1)Alice", 1)
    coro2 = greet("2)Bob", 1)
    coro3 = greet("3)John", 1)
    coro5 = greet("4)Mark", 1)
    coro4 = greet("5)Paul", 1)
    coro6 = greet("6)Helen", 1)

    # Gather all coroutines to run concurrently
    await asyncio.gather(coro1, coro2, coro3, coro4, coro5, coro6)


# Run the event loop
asyncio.run(main())
