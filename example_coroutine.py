import asyncio

async def example_coroutine():
    print("Start Coroutine")
    await asyncio.sleep(2)  # Simulate an asynchronous operation (sleep for 2 seconds)
    print("Coroutine resumed after sleep")

async def main():
    await asyncio.gather(example_coroutine(), example_coroutine())

if __name__ == "__main__":
    asyncio.run(main())
