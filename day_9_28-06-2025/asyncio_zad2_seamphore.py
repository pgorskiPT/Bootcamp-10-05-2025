import asyncio
import httpx

url = "https://naukajava.online"

# tworzymy semafor - dzielimy zadanie na paczki
sema = asyncio.Semaphore(100)


async def fetch(client, i):
    async with sema:
        resp = await client.get(url)
        # print(f"{i + 1}: status code: {resp.status_code}")


async def main():
    async with httpx.AsyncClient() as client:
        tasks = [fetch(client, i) for i in range(600)]
        await asyncio.gather(*tasks)


asyncio.run(main())
# time python asyncio_zad2_seamphore.py
# Measure-Command { python asyncio_zad2.py }
# python asyncio_zad2_seamphore.py  1.09s user 0.19s system 93% cpu 1.374 total dla 100
# python asyncio_zad2_seamphore.py  1.11s user 0.18s system 83% cpu 1.538 total dla 50
