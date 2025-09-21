import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('marketing_ok_date.csv', sep=",")
print(df.head(3))

language = df.groupby(["date_served", "language_preferred"])["user_id"].count()
print(language.head())
# 2018-01-01   Arabic                  4
#              English               355
#              German                  5
#              Spanish                11
# 2018-01-02   Arabic                  4
# Name: user_id, dtype: int64

# zamiana kolumn z wierszami
language = pd.DataFrame(language.unstack(level=1))
print(language.head())
# language_preferred  Arabic  English  German  Spanish
# date_served
# 2018-01-01             4.0    355.0     5.0     11.0
# 2018-01-02             4.0    397.0     6.0     10.0
# 2018-01-03             3.0    374.0     3.0      8.0
# 2018-01-04             2.0    318.0     2.0     14.0
# 2018-01-05             1.0    314.0     2.0     14.0

# level - wskazuje kolumnę, która ma być nagłówkiem(wierszem 0)
# language = pd.DataFrame(language.unstack(level=0))
# print(language.head())
# date_served         2018-01-01  2018-01-02  ...  2018-01-30  2018-01-31
# language_preferred                          ...
# Arabic                     4.0         4.0  ...         6.0         8.0
# English                  355.0       397.0  ...       302.0       317.0
# German                     5.0         6.0  ...         3.0         5.0
# Spanish                   11.0        10.0  ...        19.0        17.0

language.plot()
plt.title("Dzienne preferencje językowe")
plt.xlabel("Data")
plt.ylabel("Użytkownicy")
plt.legend(loc="upper right", labels=language.columns.values)
plt.show()

# level - wskazuje kolumnę, która ma być nagłówkiem(wierszem 0)
language = df.groupby(["date_served", "language_preferred"])["user_id"].count()
language = pd.DataFrame(language.unstack(level=0))
print(language.head())
# date_served         2018-01-01  2018-01-02  ...  2018-01-30  2018-01-31
# language_preferred                          ...
# Arabic                     4.0         4.0  ...         6.0         8.0
# English                  355.0       397.0  ...       302.0       317.0
# German                     5.0         6.0  ...         3.0         5.0
# Spanish                   11.0        10.0  ...        19.0        17.0
language.plot()
plt.title("Dzienne preferencje językowe")
plt.xlabel("Data")
plt.ylabel("Użytkownicy")
plt.legend(loc="upper right", labels=language.columns.values)
plt.show()
