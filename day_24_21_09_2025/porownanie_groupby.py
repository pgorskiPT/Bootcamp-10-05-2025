import time
import dask.dataframe as dd
import pandas as pd
import polars as pl

filename = 'bigfile_polars.csv'

start = time.time()
df = pd.read_csv(filename)
result = df.groupby("category")['value'].sum()
print("Pandas groupby:", result)
print("Czas:", time.time() - start)

# polars
start = time.time()
df = pl.read_csv(filename)
result = df.group_by("category").agg(pl.col("value").sum())
print("Polars groupby:", result)
print("Czas:", time.time() - start)

# polars lazy, scan
start = time.time()
# wczytywanie lazy - nie ładuje calego pliku do pamięci

result = (
    pl.scan_csv(filename)
    .group_by("category")
    .agg(pl.col("value").sum())
    .collect()  # <-- TO JEST KLUCZ!
)
print("Polars groupby (lazy):", result)
print("Czas:", time.time() - start)

# dask
start = time.time()
df = dd.read_csv(filename)
result = df.groupby("category")['value'].sum().compute()
print("Dask groupby:", result)
print("Czas:", time.time() - start)
# Pandas mean: 5000.35136653
# Czas: 5.997074127197266
# Polars mean: 5000.35136653
# Czas: 0.9032130241394043
# Polars mean (lazy): 5000.35136653
# Czas: 0.5055980682373047
# Dask mean: 5000.35136653
# Czas: 3.138678789138794

# Czas: 7.388631105422974 - pandas
# Czas: 1.9825000762939453 - polars
# Czas: 2.427572011947632 - polars lazy
# Czas: 4.624889135360718 - dask
