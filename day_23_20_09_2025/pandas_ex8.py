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

df = pd.DataFrame({'Miasto': ['Warszawa', 'Kraków', "Łódź", "Warszawa", "Gliwice"]})
print(df)

# df['Miasto'].replace("Warszawa", "Warszawa-Stolica", inplace=True) # starsze podejście
df['Miasto'] = df['Miasto'].replace("Warszawa", "Warszawa-Stolica")  # dla nowszych pandasów
print(df.to_string())
#              Miasto
# 0  Warszawa-Stolica
# 1            Kraków
# 2              Łódź
# 3  Warszawa-Stolica
# 4           Gliwice

df = pd.DataFrame({'Miasto': ['Warszawa', 'Kraków', "Łódź", "Warszawa", "Gliwice"]})
df['Miasto'] = df['Miasto'].replace({"Warszawa": "Warszawa-Stolica", "Kraków": "Kraków - Zamkowy"})
print(df)
# 0  Warszawa-Stolica
# 1  Kraków - Zamkowy
# 2              Łódź
# 3  Warszawa-Stolica
# 4           Gliwice

df = pd.DataFrame({"Wiek": [18, 25, 30, 15, 40]})
print(df)
#    Wiek
# 0    18
# 1    25
# 2    30
# 3    15
# 4    40
df["Kategoria"] = "Dorosły"
print(df)
#    Wiek Kategoria
# 0    18   Dorosły
# 1    25   Dorosły
# 2    30   Dorosły
# 3    15   Dorosły
# 4    40   Dorosły
df.loc[df['Wiek'] < 18, "Kategoria"] = "Niepełnoletni"
print(df)
#    Wiek      Kategoria
# 0    18        Dorosły
# 1    25        Dorosły
# 2    30        Dorosły
# 3    15  Niepełnoletni
# 4    40        Dorosły

df = pd.DataFrame({'Miasto': ['Warszawa', 'Kraków', "Łódź", "Warszawa", "Gliwice"]})
# df['Miasto'] = df['Miasto'].replace(r"Łódź", "Łódź Przemysłowa", regex=True)
# df['Miasto'] = df['Miasto'].replace(r"^Ł", "Łódź Przemysłowa", regex=True)
df['Miasto'] = df['Miasto'].replace(r"^Ł.*", "Łódź Przemysłowa", regex=True)
print(df.to_string())
# 0          Warszawa
# 1            Kraków
# 2  Łódź Przemysłowa
# 3          Warszawa
# 4           Gliwice
# regex
# ^ - zaczynające się od
# ^Ł - zaczynajćae sie od Ł
# 	•	^
# → oznacza początek tekstu.
# Dzięki temu wzorzec szuka tylko takich napisów, które zaczynają się od określonego fragmentu.
# 	•	Ł
# → dosłowna litera „Ł”.
# Czyli szukamy napisów zaczynających się od „Ł”.
# 	•	.
# → kropka oznacza dowolny pojedynczy znak (litera, cyfra, spacja, znak specjalny).
# 	•	*
# → gwiazdka oznacza „zero lub więcej wystąpień” poprzedniego elementu.
# W tym przypadku „dowolny znak powtarzany dowolną liczbę razy (albo wcale)”.

df = pd.DataFrame({"Wiek": [18, 25, 30, 15, 40, 65]})
df['Kategoria'] = df['Wiek'].apply(lambda x: "Senior" if x > 60 else "Dorosły")
print(df)


#    Wiek Kateogoria
# 0    18    Dorosły
# 1    25    Dorosły
# 2    30    Dorosły
# 3    15    Dorosły
# 4    40    Dorosły
# 5    65     Senior

def zmien(x):
    if x > 60:
        return "Senior"
    else:
        return "Dorosły"


df['Kategoria'] = df["Wiek"].apply(zmien)  # podajemy tylko adres funkcji
print(df)
#    Wiek Kategoria
# 0    18   Dorosły
# 1    25   Dorosły
# 2    30   Dorosły
# 3    15   Dorosły
# 4    40   Dorosły
# 5    65    Senior

df = pd.DataFrame({'Miasto': ['Warszawa123', 'Kraków456', "Łódź", "Warszawa789", "Gliwice"]})
df['Miasto'] = df['Miasto'].replace(r"\d+", "", regex=True)
print(df)
# df = pd.DataFrame({'Miasto': ['Warszawa', 'Kraków', "Łódź", "Warszawa", "Gliwice"]})
# 	•	\d
# Oznacza dowolną cyfrę (0–9).
# (\d ≈ [0-9])
# 	•	+
# Oznacza jeden lub więcej wystąpień poprzedniego elementu.
# 	•	\d+ = „ciąg złożony z co najmniej jednej cyfry”
#      Miasto
# 0  Warszawa
# 1    Kraków
# 2      Łódź
# 3  Warszawa
# 4   Gliwice
