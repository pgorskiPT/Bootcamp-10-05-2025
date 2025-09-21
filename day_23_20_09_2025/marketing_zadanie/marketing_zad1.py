import numpy as np
import pandas as pd

# df = pd.read_csv('marketing_r.csv')
# print(df.head().to_string())
df = pd.read_csv('marketing_r.csv', sep=",")
# print(df.head(1).to_string())

print(df.describe())
#            user_id date_served  ... subscribing_channel is_retained
# count        10037       10021  ...                1856        1856
# unique        7309          31  ...                   5           2
# top     a100000882     1/15/18  ...           Instagram        True
# freq            12         789  ...                 600        1279
#
# [4 rows x 12 columns]

df.info()
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 10037 entries, 0 to 10036
# Data columns (total 12 columns):
#  #   Column               Non-Null Count  Dtype
# ---  ------               --------------  -----
#  0   user_id              10037 non-null  object
#  1   date_served          10021 non-null  object
#  2   marketing_channel    10022 non-null  object
#  3   variant              10037 non-null  object
#  4   converted            10022 non-null  object
#  5   language_displayed   10037 non-null  object
#  6   language_preferred   10037 non-null  object
#  7   age_group            10037 non-null  object
#  8   date_subscribed      1856 non-null   object
#  9   date_canceled        577 non-null    object
#  10  subscribing_channel  1856 non-null   object
#  11  is_retained          1856 non-null   object
# dtypes: object(12)
# memory usage: 941.1+ KB

# sprawdzmy jaki typ m kolumna 'converted'
print(df['converted'].dtype)  # object

# zmienić typ kolumny na typ bool
df['converted'] = df['converted'].astype('bool')
print(df['converted'].dtype)  # bool
df.info()
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 10037 entries, 0 to 10036
# Data columns (total 12 columns):
#  #   Column               Non-Null Count  Dtype
# ---  ------               --------------  -----
#  0   user_id              10037 non-null  object
#  1   date_served          10021 non-null  object
#  2   marketing_channel    10022 non-null  object
#  3   variant              10037 non-null  object
#  4   converted            10037 non-null  bool
#  5   language_displayed   10037 non-null  object
#  6   language_preferred   10037 non-null  object
#  7   age_group            10037 non-null  object
#  8   date_subscribed      1856 non-null   object
#  9   date_canceled        577 non-null    object
#  10  subscribing_channel  1856 non-null   object
#  11  is_retained          1856 non-null   object
# dtypes: bool(1), object(11)
# memory usage: 872.5+ KB
print(df.head(1).to_string())

df['is_house_ads'] = np.where(df['marketing_channel'] == "House Ads", True, False)
print(df.is_house_ads.head(3))
# 0    True
# 1    True
# 2    True
# Name: is_house_ads, dtype: bool
df.to_csv('marketing_is_house_ads.csv', sep=",", index=False)

# zamiana dat na typ datetime
df['date_served'] = pd.to_datetime(df['date_served'], errors='coerce', format='mixed')
print(df['date_served'].head(3))
# 0   2018-01-01
# 1   2018-01-01
# 2   2018-01-01
# Name: date_served, dtype: datetime64[ns]

# # dni tygodnia numerycznie
# df['date_served'] = df['date_served'].dt.dayofweek
# print(df['date_served'].head(3))
# # 0    0.0 - poniedziałek
# # 1    0.0
# # 2    0.0
# # Name: date_served, dtype: float64

# nazwy dni tygodnia
# df['day_name'] = df['date_served'].dt.day_name()
# print(df['day_name'].head(3))
# 0    Monday
# 1    Monday
# 2    Monday
# Name: day_name, dtype: object
# dodanie kolumny channel_code, zmapowanie nazw  marketing_channel na channel_code
channel_dict = {"House Ads": 1, "Instagram": 2, "Facebook": 3, "Email": 4, "Push": 5}
df['channel_code'] = df['marketing_channel'].map(channel_dict)
print(df['channel_code'].head(3))
# 0    1.0
# 1    1.0
# 2    1.0
# Name: channel_code, dtype: float64

# unikalni uzytkownicy dziennie
daily_users = df.groupby(['date_served'])['user_id'].nunique()
print("Dziennie:", daily_users)
# Dziennie: date_served
# 2018-01-01    362
# 2018-01-02    374
# 2018-01-03    348
# 2018-01-04    323
# 2018-01-05    319
# 2018-01-06    308
# 2018-01-07    275
# 2018-01-08    312
# 2018-01-09    312
# 2018-01-10    337
# 2018-01-11    310
# 2018-01-12    301
# 2018-01-13    306
# 2018-01-14    305
# 2018-01-15    767
# 2018-01-16    388
# 2018-01-17    369
# 2018-01-18    318
# 2018-01-19    305
# 2018-01-20    311
# 2018-01-21    229
# 2018-01-22    178
# 2018-01-23    172
# 2018-01-24    190
# 2018-01-25    184
# 2018-01-26    222
# 2018-01-27    320
# 2018-01-28    320
# 2018-01-29    319
# 2018-01-30    317
# 2018-01-31    340
# Name: user_id, dtype: int64

import matplotlib.pyplot as plt

daily_users.plot()

plt.title("Zasięg dzienny kampani marketingowej")
plt.xlabel("Data")
plt.ylabel("Liczba użytkowników")
plt.xticks(rotation=45)

plt.show()
