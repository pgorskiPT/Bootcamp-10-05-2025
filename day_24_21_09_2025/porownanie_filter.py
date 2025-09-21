import time
import pandas as pd
import polars as pl

filename = "bigfile_polars.csv"

# Polars (read)
start = time.time()
df_polars = pl.read_csv(filename)
filtered_polars = df_polars.filter(pl.col("category") == "B")
print("Polars: liczba wierszy z kategorią 'B':", filtered_polars.height)
print("Polars filter czas:", time.time() - start)
# Polars: liczba wierszy z kategorią 'B': 250524
# Polars filter czas: 0.11478114128112793

# polars (scan, czyli lazy - nie tryma całego pliku w RAM
start = time.time()
df_polars = pl.scan_csv(filename)
filtered_polars = df_polars.filter(pl.col("category") == "B").collect()
print("Polars: liczba wierszy z kategorią 'B':", filtered_polars.height)
print("Polars filter czas:", time.time() - start)
# Polars: liczba wierszy z kategorią 'B': 250524
# Polars filter czas: 0.024580955505371094
