import asyncio
import asyncpg


async def fetch_data():
    # conn = await asyncpg.connect(
    #     host="localhost",
    #     port=5432,
    #     database="mydatabase",
    #     user="myuser",
    #     password="mypassword"
    # )

    conn = await asyncpg.connect(
        host="",
        port=5432,
        database="",
        user="",
        password=""
    )

    try:
        rows = await conn.fetch("SELECT * FROM persons;")
        for row in rows:
            print(row)

        # pojedynczy wiersz
        single_row = await conn.fetchrow("SELECT * FROM persons WHERE id=$1;", 1)  # <Record id=1 name='Radek'>
        if single_row:
            print(f"Single Row -> ID: {single_row['id']}, {single_row}")
            # Single Row -> ID: 1, <Record id=1 name='Radek'>
    finally:
        await conn.close()


asyncio.run(fetch_data())
# <Record id=1 name='Radek'>
# <Record id=2 name='Radek'>
# <Record id=3 name='Radek'>
# Single Row -> ID: 1, <Record id=1 name='Radek'>
