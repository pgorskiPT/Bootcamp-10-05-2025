import asyncio
import httpx

url = "https://naukajava.online"


async def fetch(client, i):
    resp = await client.get(url)
    # print(f"{i + 1}: status code: {resp.status_code}")


async def main():
    async with httpx.AsyncClient() as client:
        tasks = [fetch(client, i) for i in range(600)]
        await asyncio.gather(*tasks)


asyncio.run(main())
# time python asyncio_zad1.py
# Measure-Command { python asyncio_zad1.py }
# python asyncio_zad1.py  6.44s user 0.22s system 99% cpu 6.726 total
