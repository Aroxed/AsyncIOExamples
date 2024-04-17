import asyncio


async def greet(name, delay):
    await asyncio.sleep(delay)
    print(f"Hello, {name}!")


async def main():
    # Wait for Alice's greeting first
    await greet("Alice", 1)

    # Now greet Bob
    await greet("Bob", 1)


# Run the event loop
asyncio.run(main())
