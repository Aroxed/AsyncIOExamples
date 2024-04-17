import asyncio


async def display_progress():
    for i in range(1, 6):
        print(f"Progress: {i * 20}%")
        await asyncio.sleep(1)


# Main coroutine
async def main():
    await asyncio.gather(display_progress())


# Run the main coroutine
asyncio.run(main())
