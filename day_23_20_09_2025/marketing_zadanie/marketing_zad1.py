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
print(df['converted'].dtype) # object

