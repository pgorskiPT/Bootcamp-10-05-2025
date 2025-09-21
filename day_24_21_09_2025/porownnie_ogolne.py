import time
import dask.dataframe as dd
import pandas as pd
import polars as pl

filename = 'bigfile_polars.csv'

start = time.time()
df = pd.read_csv(filename)
mean = df["value"].mean()
print("Pandas mean:", mean)
print("Czas:", time.time() - start)

# polars
start = time.time()
df = pl.read_csv(filename)
mean = df["value"].mean()
print("Polars mean:", mean)
print("Czas:", time.time() - start)

# polars lazy, scan
start = time.time()
# wczytywanie lazy - nie ładuje calego pliku do pamięci
df = pl.scan_csv(filename)

# dwa podejścia do wyświetlania
mean = df.select(pl.col("value").mean()).collect()
mean_lazy = mean[0, 0]
# mean = df.select(pl.col("value").mean()).collect().item()  # item() by tylko wartosc sredniej była a nie obiekt
# print("Polars mean (lazy):", mean)
print("Polars mean (lazy):", mean_lazy)
print("Czas:", time.time() - start)

# dask
start = time.time()
df = dd.read_csv(filename)
mean = df["value"].mean().compute()
print("Dask mean:", mean)
print("Czas:", time.time() - start)
# Pandas mean: 5000.35136653
# Czas: 5.997074127197266
# Polars mean: 5000.35136653
# Czas: 0.9032130241394043
# Polars mean (lazy): 5000.35136653
# Czas: 0.5055980682373047
# Dask mean: 5000.35136653
# Czas: 3.138678789138794
