import pandas as pd

data = pd.read_csv('data_with_date.csv')
print(data)

data.loc[7, "Duration"] = 45
print(data.loc[7])
# Duration              45
# Date        '2020/12/08'
# Pulse                104
# Maxpulse             134
# Calories           253.3
# Name: 7, dtype: object

data = pd.read_csv('data_with_date.csv')

for x in data.index:
    if data.loc[x, "Duration"] > 120:
        data.loc[x, "Duration"] = 120

print(data)

data = pd.read_csv('data_with_date.csv')

for x in data.index:
    if data.loc[x, "Duration"] > 120:
        data.drop(x, inplace=True)  # usunie ten wiersz, inplace=True - zmienia oryginał

print(data)

# te same zadania w sposób pandasowy
# jeżeli wartości będą powyżej 120, zostaną wyrównane do wartości 120
data = pd.read_csv('data_with_date.csv')
data['Duration'] = data["Duration"].clip(upper=120)  # clip - przyciecie
print(45 * "-")
print("Clip:", data)

data = pd.read_csv('data_with_date.csv')
data['Duration'] = data["Duration"].where(data["Duration"] <= 120, 120)
# wyszukaj spęłniające warunek, pozostałe 120
print(45 * "-")
print("where:", data)

data = pd.read_csv('data_with_date.csv')
data["Duration"] = data["Duration"].mask(data["Duration"] > 120, 120)
# zamaskuj spełniajace warunek, ustaw 120 dla nich
print(45 * "-")
print("mask:", data)

# filtrowanie
data = pd.read_csv('data_with_date.csv')
data = data[data["Duration"] <= 120]
print(data)

data = pd.read_csv('data_with_date.csv')
data = data.query("Duration <= 120")
print(data)
# Method               Rows in    Time [s]   Rows remaining
# for + drop(per-row)  10000      0.973      6103
# boolean filter       1000000    0.0119     602352
# mask + drop(once)    1000000    0.0271     601573
