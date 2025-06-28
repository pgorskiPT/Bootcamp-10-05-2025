import asyncio
import time
import aiohttp
from pydantic import with_config


async def fetch(url, sesion, index):
    async with sesion.get(url, ssl=False) as response:
        text = await response.text()
        print(f"Text: {text}")

        return response.status


async def measure_aiohttp():
    url = "https://api.nbp.pl/api/exchangerates/rates/A/EUR/"
    tasks = []

    # pomiar czasu dla wszystkich zapytań
    overall_start_time = time.time()

    async with aiohttp.ClientSession() as session:
        for i in range(100):
            tasks.append(fetch(url, session, i + 1))

        # przekazanie do asyncio zadań
        statuses = await asyncio.gather(*tasks)

    overall_elapsed_time = time.time() - overall_start_time
    print(f"Overall time for 100 requests: {overall_elapsed_time:.4f} seconds.")


asyncio.run(measure_aiohttp())
# Overall time for 100 requests: 0.1338 seconds.
# Overall time for 1 requests: 0.0667 seconds.
