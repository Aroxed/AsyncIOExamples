import asyncio
import random


# Coroutine to simulate work
async def work(id):
    await asyncio.sleep(random.uniform(0.5, 2.5))
    print(f"Task {id} finished")


# Coroutine to display progress
async def display_progress():
    for i in range(1, 6):
        print(f"Progress: {i * 20}%")
        await asyncio.sleep(1)


# Main coroutine
async def main():
    tasks = [asyncio.create_task(work(i)) for i in range(1, 6)]
    await asyncio.create_task(display_progress())
    await asyncio.gather(*tasks)


# Run the main coroutine
asyncio.run(main())
