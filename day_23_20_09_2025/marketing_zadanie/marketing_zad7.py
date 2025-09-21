import marketing_zad6 as fun
import pandas as pd

# df = pd.read_csv('marketing_ok_date.csv', sep=",")
df = pd.read_csv('marketing_is_house_ads.csv', sep=",")
print(df.head(3))
print(df['date_served'].dtype)  # object
# df['date_served'] = pd.to_datetime(df['date_served'], format='%Y-%m-%d')
df['date_served'] = pd.to_datetime(df['date_served'], format='%m/%d/%y')
print(df.head(3))
#    Unnamed: 0     user_id date_served  ... is_retained is_house_ads  channel_code
# 0           0  a100000029  2018-01-01  ...        True         True           1.0
# 1           1  a100000030  2018-01-01  ...        True         True           1.0
# 2           2  a100000031  2018-01-01  ...        True         True           1.0
#
# [3 rows x 15 columns]

house_ads = df[df['subscribing_channel'] == "House Ads"]
print(house_ads.head(3))

house_ads_b = house_ads[house_ads['date_served'] < '2018-01-11']
print(house_ads_b)
lang_conv = fun.conversion_rate(house_ads_b, ['language_displayed'])
print("lang_conv:\n", lang_conv)
#  language_displayed
# Arabic     1.000000
# English    0.865854
# German     0.857143
# Spanish    0.894737
# Name: user_id, dtype: float64

spanish_index = lang_conv['Spanish'] / lang_conv["English"]
arabic_index = lang_conv['Arabic'] / lang_conv['English']
german_index = lang_conv['German'] / lang_conv['English']
print("Spanish index:", spanish_index)
print("Arabic index:", arabic_index)
print("German index:", german_index)
# Spanish index: 1.033358042994811
# Arabic index: 1.1549295774647887
# German index: 0.9899396378269617

converted = (house_ads.groupby(['date_served', 'language_preferred'])
             .agg({"user_id": "unique", "converted": "sum"}))
print(converted.head(3))
#                                                                           user_id  converted
# date_served language_preferred
# 2018-01-01  Arabic                                       [a100000041, a100000044]          2
#             English             [a100000029, a100000030, a100000031, a10000003...         13
#             German                                       [a100000034, a100000060]          1
converted = pd.DataFrame(converted.unstack(level=1))
print(converted.head(3))
# language_preferred                    Arabic  ...   Spanish
# date_served                                   ...
# 2018-01-01          [a100000041, a100000044]  ...       NaN
# 2018-01-02                               NaN  ...       NaN
# 2018-01-03                               NaN  ...       1.0
