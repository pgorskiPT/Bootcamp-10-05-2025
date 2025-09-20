import pandas as pd

# pip install pandas

print(pd.__version__)  # 2.3.2

# Series - odwzorowanie kolumny
name_dict = {"name": ["Radek", "Tomek"]}

a = [1, 2, 3]  # jednowymiarowe, jak kolumna
myvar = pd.Series(a)
print(myvar)
# 0    1
# 1    2
# 2    3
# dtype: int64

print(myvar[0])  # 1, wypisanie pierwszej wartości, pierwszy wiersz

# nadanie nazw
myvar = pd.Series(a, index=["x", "y", "z"])
print(myvar)
# x    1
# y    2
# z    3
# dtype: int64
print(myvar["y"])  # 2 uzycie indeksu po nazwie

calories = {'day1': 420, "day2": 380, "day3": 390}
myvar = pd.Series(calories)
print(myvar)
# day1    420
# day2    380
# day3    390
# dtype: int64

# wczytaniei części danych
myvar = pd.Series(calories, index=["day1", "day2"])
print(myvar)
# day1    420
# day2    380
# dtype: int64

# DataFrame - odwzorowanie kolumn
data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}

df = pd.DataFrame(data)
print(df)
#    calories  durtaion
# 0       420       50
# 1       380       40
# 2       390       45

# loc - dane z wiersza
print(df.loc[0])
# calories    420
# duration      50
# Name: 0, dtype: int64

print(type(df.loc[0]))  # <class 'pandas.core.series.Series'>

print(df.loc[[0, 1]])
#    calories  duration
# 0       420        50
# 1       380        40
print(type(df.loc[[0, 1]]))  # <class 'pandas.core.frame.DataFrame'>

df = pd.DataFrame(
    {
        "Name": [
            "Tomek",
            "Radek",
            "Zenek",
            "Anna"
        ],
        'Age': [22, 45, 35, 29],
        "Sex": ['male', 'male', 'female', 'female']
    }
)
