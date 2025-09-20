import pandas as pd

df = pd.read_csv('data_with_date.csv')
print(df)

df['Date'] = pd.to_datetime(df['Date'], errors='coerce', format='mixed')
print(df.to_string())
# errors='coerce' - gdy nie potrafi zamienic (NaN) na datę to wstawi NaT (Not a Time)
# format='mixed' - jeśłi data w innym formacie zamieni na włąściwy -> %Y-%m-%d

df = pd.read_csv('data_with_date.csv')
df.dropna(subset=["Date"], inplace=True)
print(df.to_string())
