import time
import asyncio
import aiohttp


urls = [
    "https://fr.wikipedia.org/wiki/Henry_Cavill",
    "https://fr.wikipedia.org/wiki/Ben_Affleck",
    "https://fr.wikipedia.org/wiki/Gal_Gadot",
    "https://fr.wikipedia.org/wiki/Henry_Cavill",
    "https://fr.wikipedia.org/wiki/Ben_Affleck",
    "https://fr.wikipedia.org/wiki/Gal_Gadot",
    "https://fr.wikipedia.org/wiki/Henry_Cavill",
    "https://fr.wikipedia.org/wiki/Ben_Affleck",
    "https://fr.wikipedia.org/wiki/Gal_Gadot",
    "https://fr.wikipedia.org/wiki/Henry_Cavill",
    "https://fr.wikipedia.org/wiki/Ben_Affleck",
    "https://fr.wikipedia.org/wiki/Gal_Gadot",
    "https://fr.wikipedia.org/wiki/Henry_Cavill",
    "https://fr.wikipedia.org/wiki/Ben_Affleck",
    "https://fr.wikipedia.org/wiki/Gal_Gadot",
    "https://fr.wikipedia.org/wiki/Henry_Cavill",
    "https://fr.wikipedia.org/wiki/Ben_Affleck",
    "https://fr.wikipedia.org/wiki/Henry_Cavill",
    "https://fr.wikipedia.org/wiki/Ben_Affleck",
    "https://fr.wikipedia.org/wiki/Gal_Gadot",
    "https://fr.wikipedia.org/wiki/Henry_Cavill",
    "https://fr.wikipedia.org/wiki/Ben_Affleck",
    "https://fr.wikipedia.org/wiki/Gal_Gadot",
    "https://fr.wikipedia.org/wiki/Henry_Cavill",
    "https://fr.wikipedia.org/wiki/Ben_Affleck",
    "https://fr.wikipedia.org/wiki/Gal_Gadot",
    "https://fr.wikipedia.org/wiki/Henry_Cavill",
    "https://fr.wikipedia.org/wiki/Ben_Affleck",
    "https://fr.wikipedia.org/wiki/Gal_Gadot",
    "https://fr.wikipedia.org/wiki/Henry_Cavill",
    "https://fr.wikipedia.org/wiki/Ben_Affleck",
    "https://fr.wikipedia.org/wiki/Gal_Gadot",
    "https://fr.wikipedia.org/wiki/Henry_Cavill",
    "https://fr.wikipedia.org/wiki/Ben_Affleck",
    "https://fr.wikipedia.org/wiki/Henry_Cavill",
    "https://fr.wikipedia.org/wiki/Ben_Affleck",
    "https://fr.wikipedia.org/wiki/Gal_Gadot",
    "https://fr.wikipedia.org/wiki/Henry_Cavill",
    "https://fr.wikipedia.org/wiki/Ben_Affleck",
    "https://fr.wikipedia.org/wiki/Gal_Gadot",
    "https://fr.wikipedia.org/wiki/Henry_Cavill",
    "https://fr.wikipedia.org/wiki/Ben_Affleck",
    "https://fr.wikipedia.org/wiki/Gal_Gadot",
    "https://fr.wikipedia.org/wiki/Henry_Cavill",
    "https://fr.wikipedia.org/wiki/Ben_Affleck",
    "https://fr.wikipedia.org/wiki/Gal_Gadot",
    "https://fr.wikipedia.org/wiki/Henry_Cavill",
    "https://fr.wikipedia.org/wiki/Ben_Affleck",
    "https://fr.wikipedia.org/wiki/Gal_Gadot",
    "https://fr.wikipedia.org/wiki/Henry_Cavill",
    "https://fr.wikipedia.org/wiki/Ben_Affleck",
    "https://fr.wikipedia.org/wiki/Henry_Cavill",
    "https://fr.wikipedia.org/wiki/Ben_Affleck",
    "https://fr.wikipedia.org/wiki/Gal_Gadot",
    "https://fr.wikipedia.org/wiki/Henry_Cavill",
    "https://fr.wikipedia.org/wiki/Ben_Affleck",
    "https://fr.wikipedia.org/wiki/Gal_Gadot",
    "https://fr.wikipedia.org/wiki/Henry_Cavill",
    "https://fr.wikipedia.org/wiki/Ben_Affleck",
    "https://fr.wikipedia.org/wiki/Gal_Gadot",
    "https://fr.wikipedia.org/wiki/Henry_Cavill",
    "https://fr.wikipedia.org/wiki/Ben_Affleck",
    "https://fr.wikipedia.org/wiki/Gal_Gadot",
    "https://fr.wikipedia.org/wiki/Henry_Cavill",
    "https://fr.wikipedia.org/wiki/Ben_Affleck",
    "https://fr.wikipedia.org/wiki/Gal_Gadot",
    "https://fr.wikipedia.org/wiki/Henry_Cavill",
    "https://fr.wikipedia.org/wiki/Ben_Affleck",
    "https://fr.wikipedia.org/wiki/Henry_Cavill",
    "https://fr.wikipedia.org/wiki/Ben_Affleck",]


async def load_url(session: aiohttp.ClientSession, index: int) -> bytes:
    """Fetch the content of a URL asynchronously."""
    try:
        async with session.get(urls[index], timeout=20) as response:
            return await response.read()
    except Exception as e:
        print(f"Error loading URL {urls[index]}: {e}")
        return b""


async def main():
    n_jobs = len(urls)
    print("n_jobs", n_jobs)
    
    async with aiohttp.ClientSession() as session:

        start_time = time.time()
        results = await asyncio.gather(*[load_url(session, i) for i in range(n_jobs)])
        end_time = time.time()
        print(f"asyncio with all concurrent tasks, total time: {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    asyncio.run(main())