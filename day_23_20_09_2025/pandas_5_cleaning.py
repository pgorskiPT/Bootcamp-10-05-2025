import pandas as pd

df = pd.read_csv('data.csv')
print(df.info())
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 169 entries, 0 to 168
# Data columns (total 4 columns):
#  #   Column    Non-Null Count  Dtype
# ---  ------    --------------  -----
#  0   Duration  169 non-null    int64
#  1   Pulse     169 non-null    int64
#  2   Maxpulse  169 non-null    int64
#  3   Calories  164 non-null    float64
# dtypes: float64(1), int64(3)
# memory usage: 5.4 KB
# None

# zwraca nowy DataFrame z danymi bez NaN
new_df = df.dropna()  # wyciagniej wszystkie bez NaN
print(new_df.to_string())
print(new_df.info())
# <class 'pandas.core.frame.DataFrame'>
# Index: 164 entries, 0 to 168
# Data columns (total 4 columns):
#  #   Column    Non-Null Count  Dtype
# ---  ------    --------------  -----
#  0   Duration  164 non-null    int64
#  1   Pulse     164 non-null    int64
#  2   Maxpulse  164 non-null    int64
#  3   Calories  164 non-null    float64
# dtypes: float64(1), int64(3)
# memory usage: 6.4 KB
# None

# zamieni w oryginnalnej DataFrame
df.dropna(inplace=True)  # inplace - zmien oryginał
print(df.info())
# <class 'pandas.core.frame.DataFrame'>
# Index: 164 entries, 0 to 168
# Data columns (total 4 columns):
#  #   Column    Non-Null Count  Dtype
# ---  ------    --------------  -----
#  0   Duration  164 non-null    int64
#  1   Pulse     164 non-null    int64
#  2   Maxpulse  164 non-null    int64
#  3   Calories  164 non-null    float64
# dtypes: float64(1), int64(3)
# memory usage: 6.4 KB
# None

print(df.to_string())
