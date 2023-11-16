import asyncio

async def example_coroutine():
    print("Start Coroutine")
    await asyncio.sleep(2)
    print("Coroutine resumed after sleep")

async def main():
    task1 = asyncio.create_task(example_coroutine())
    task2 = asyncio.create_task(example_coroutine())

    await asyncio.gather(task1, task2)

if __name__ == "__main__":
    asyncio.run(main())
