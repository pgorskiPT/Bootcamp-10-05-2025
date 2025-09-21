import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# df = pd.read_csv('marketing_ok_date.csv', sep=",")
df = pd.read_csv('marketing_is_house_ads.csv', sep=",")
print(df.head(3))
print(df['date_served'].dtype)  # object
# df['date_served'] = pd.to_datetime(df['date_served'], format='%Y-%m-%d')
df['date_served'] = pd.to_datetime(df['date_served'], format='%m/%d/%y')
print(df.head(3))

email = df[df['marketing_channel'] == 'Email']
print(email.head().to_string())

# upewnienie się, ze grupy zostały odpowiednio zbalansowane
alloc = email.groupby(['variant'])["user_id"].nunique()
print(alloc.head())
# variant
# control            270
# personalization    284
# Name: user_id, dtype: int64
# alloc.plot(kind="bar")
# plt.title("Personalizacja trstu")
# plt.ylabel("liczba")
# plt.show()

subscribers = email.groupby(['user_id', 'variant'])['converted'].max()
print(subscribers.head())
# user_id     variant
# a100000526  personalization     True
# a100000530  personalization     True
# a100000534  personalization    False
# a100000538  personalization     True
# a100000542  personalization     True
# Name: converted, dtype: bool

subscribers_df = pd.DataFrame(subscribers.unstack(level=1))
control = subscribers_df['control'].dropna()
print(control.head())
# Name: converted, dtype: bool
# user_id
# a100000687    False
# a100000688     True
# a100000689     True
# a100000690     True
# a100000691     True
# Name: control, dtype: object
control.info()
# <class 'pandas.core.series.Series'>
# Index: 270 entries, a100000687 to a100007293
# Series name: control
# Non-Null Count  Dtype
# --------------  -----
# 270 non-null    object
# dtypes: object(1)
# memory usage: 4.2+ KB

personalization = subscribers_df['personalization'].dropna()
print(personalization.tail())
# user_id
# a100007273    True
# a100007274    True
# a100007275    True
# a100007276    True
# a100007277    True
# Name: personalization, dtype: object

print("Control conversion rate:", np.mean(control))  # średnia
print("Personalization conversion rate:", np.mean(personalization))
# Control conversion rate: 0.2814814814814815
# Personalization conversion rate: 0.3908450704225352
