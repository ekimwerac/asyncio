import asyncio
import aiohttp

async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def main():
    urls = ['http://example.com', 'http://example.org', 'http://example.net']

    # Gather tasks for fetching each URL concurrently
    tasks = [fetch(url) for url in urls]

    # Use asyncio.gather to run the tasks concurrently
    responses = await asyncio.gather(*tasks)

    # Process the responses
    for url, response in zip(urls, responses):
        print(f"Content from {url}: {response[:100]}...")

if __name__ == "__main__":
    asyncio.run(main())
