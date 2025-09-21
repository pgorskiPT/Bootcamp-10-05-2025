import numpy as np
import pandas as pd

# df = pd.read_csv('marketing_ok_date.csv', sep=",")
df = pd.read_csv('marketing_is_house_ads.csv', sep=",")
print(df.head(3))
print(df['date_served'].dtype)  # object
# df['date_served'] = pd.to_datetime(df['date_served'], format='%Y-%m-%d')
df['date_served'] = pd.to_datetime(df['date_served'], format='%m/%d/%y')
print(df.head(3))

