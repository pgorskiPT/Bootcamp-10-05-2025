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

df.fillna(130, inplace=True)
print(df.info())
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 169 entries, 0 to 168
# Data columns (total 4 columns):
#  #   Column    Non-Null Count  Dtype
# ---  ------    --------------  -----
#  0   Duration  169 non-null    int64
#  1   Pulse     169 non-null    int64
#  2   Maxpulse  169 non-null    int64
#  3   Calories  169 non-null    float64
# dtypes: float64(1), int64(3)
# memory usage: 5.4 KB
# None

print(df.loc[141])
# Duration     60.0
# Pulse        97.0
# Maxpulse    127.0
# Calories    130.0
# Name: 141, dtype: float64

# nowsze podejscie
df = pd.read_csv('data.csv')
df.fillna({"Calories": 130}, inplace=True)
df.info()
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 169 entries, 0 to 168
# Data columns (total 4 columns):
#  #   Column    Non-Null Count  Dtype
# ---  ------    --------------  -----
#  0   Duration  169 non-null    int64
#  1   Pulse     169 non-null    int64
#  2   Maxpulse  169 non-null    int64
#  3   Calories  169 non-null    float64
# dtypes: float64(1), int64(3)
# memory usage: 5.4 KB
print(df.loc[141])
# Duration     60.0
# Pulse        97.0
# Maxpulse    127.0
# Calories    130.0
# Name: 141, dtype: float64

# bezpieczna metoda
df = pd.read_csv('data.csv')
df['Calories'] = df['Calories'].fillna(130)
df.info()
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 169 entries, 0 to 168
# Data columns (total 4 columns):
#  #   Column    Non-Null Count  Dtype
# ---  ------    --------------  -----
#  0   Duration  169 non-null    int64
#  1   Pulse     169 non-null    int64
#  2   Maxpulse  169 non-null    int64
#  3   Calories  169 non-null    float64
# dtypes: float64(1), int64(3)
# memory usage: 5.4 KB

# df['Calories'].fillna(130, inplace=True)
df.info()
# /Users/radoslawjaniak/PycharmProjects/Bootcamp-10-05-2025/day_23_20_09_2025/pandas_ex6.py:79: FutureWarning: A value is trying to be set on a copy of a DataFrame or Series through chained assignment using an inplace method.
# The behavior will change in pandas 3.0. This inplace method will never work because the intermediate object on which we are setting values always behaves as a copy.
# print(df.loc[141])
# Duration     60.0
# Pulse        97.0
# Maxpulse    127.0
# Calories    130.0
# Name: 141, dtype: float64

# mean() - średnia arytmetyczna
df = pd.read_csv('data.csv')

x = df['Calories'].mean()
print("Średnia wynosi:", x)  # Średnia wynosi: 375.79999999999995

# zamiana NaN w danych na wartości średnie
df['Calories'] = df['Calories'].fillna(x)
print(df.loc[141])
# Duration     60.0
# Pulse        97.0
# Maxpulse    127.0
# Calories    375.8
# Name: 141, dtype: float64

# median() - mediana, wartość środkowa
data = {"Wiek": [25, 30, 35, 40, 45, 50, 55, 60, 65]}

df = pd.DataFrame(data)
mediana_wiek = df["Wiek"].median()
print("Mediana wieku:", mediana_wiek)  # Mediana wieku: 45.0

df = pd.read_csv('data.csv')

median_data = df['Calories'].median()
print("Mediana:", median_data)  # Mediana: 318.6
df['Calories'] = df['Calories'].fillna(median_data)  # fillna - wypęłnij NaN
print(df.loc[141])
# Duration     60.0
# Pulse        97.0
# Maxpulse    127.0
# Calories    318.6
# Name: 141, dtype: float64
