import numpy as np
import pandas as pd

# df = pd.read_csv('marketing_r.csv')
# print(df.head().to_string())
df = pd.read_csv('marketing_r.csv', sep=",")
# print(df.head(1).to_string())

# sprawdzmy jaki typ m kolumna 'converted'
print(df['converted'].dtype)  # object

df['is_house_ads'] = np.where(df['marketing_channel'] == "House Ads", True, False)
# print(df.is_house_ads.head(3))

# zmienić typ kolumny na typ bool
df['converted'] = df['converted'].astype('bool')
print(df['converted'].dtype)  # bool


df['date_served'] = pd.to_datetime(df['date_served'], errors='coerce', format='mixed')
# print(df['date_served'].head(3))

channel_dict = {"House Ads": 1, "Instagram": 2, "Facebook": 3, "Email": 4, "Push": 5}
df['channel_code'] = df['marketing_channel'].map(channel_dict)
# print(df['channel_code'].head(3))

daily_users = df.groupby(['date_served'])['user_id'].nunique()
# print("Dziennie:", daily_users)
df.info()

df.to_csv("marketing_ok_date.csv")

