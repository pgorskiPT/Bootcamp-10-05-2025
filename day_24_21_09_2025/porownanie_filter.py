import time
import pandas as pd
import polars as pl
import dask.dataframe as dd

filename = "bigfile_polars.csv"

start = time.time()
df_polars = pl.read_csv(filename)
filtered_polars = df_polars.filter(pl.col("category") == "B")
print("Polars: liczba wierszy z kategorią 'B':", filtered_polars.height)
print("Polars filter czas:", time.time() - start)
# Polars: liczba wierszy z kategorią 'B': 250524
# Polars filter czas: 0.09737920761108398

# polars (scan, czyli lazy - nie tryma całego pliku w RAM
start = time.time()
df_polars = pl.scan_csv(filename)
filtered_polars = df_polars.filter(pl.col("category") == "B").collect()
print("Polars: liczba wierszy z kategorią 'B':", filtered_polars.height)
print("Polars filter czas:", time.time() - start)
# Polars: liczba wierszy z kategorią 'B': 250524
# Polars filter czas: 0.024580955505371094

# pandas - ładuje cały plik do pamięci RAM
start = time.time()
df_pandas = pd.read_csv(filename)
filtered_pandas = df_pandas[df_pandas['category'] == 'B']
print("Pandas: liczba wierszy z kategorią 'B':", len(filtered_pandas))
print("Pandas filter czas:", time.time() - start)
# Polars: liczba wierszy z kategorią 'B': 2500817
# Polars filter czas: 0.1224510669708252
# Polars: liczba wierszy z kategorią 'B': 2500817
# Polars filter czas: 0.10046219825744629
# Pandas: liczba wierszy z kategorią 'B': 2500817
# Pandas filter czas: 0.8019049167633057

# 600MB
# Polars: liczba wierszy z kategorią 'B': 24997100
# Polars filter czas: 2.6718451976776123
# Polars: liczba wierszy z kategorią 'B': 24997100
# Polars filter czas: 1.7272162437438965
# Pandas: liczba wierszy z kategorią 'B': 24997100
# Pandas filter czas: 8.673484086990356

# dask
df = dd.read_csv(filename)

filtered_dask = df[df["category"] == "B"]

start = time.time()
result = filtered_dask.shape[0].compute()
end = time.time()
print("Dask: liczba wierszy z kategorią 'B':", result)
print("Dask filter czas:", end - start)
