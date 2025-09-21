import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("marketing_ok_date.csv", sep=",")

language_age = df.groupby(['language_preferred', "age_group"])['user_id'].count()
language_age = pd.DataFrame(language_age.unstack(level=0))
print(language_age.head())
# language_preferred  Arabic  English  German  Spanish
# age_group
# 0-18 years              19     1421      31       68
# 19-24 years             26     1560      29       67
# 24-30 years             19     1442      35       72
# 30-36 years             19     1251      16       69
# 36-45 years             19     1260      19       55

# wykres słupkowy
# language_age.plot(kind="bar")
# plt.title("Język w zależności od wieku")
# plt.xlabel("Wiek")
# plt.ylabel("Użytkownicy")
# plt.legend(loc="upper right", labels=language_age.columns.values)
# plt.show()
#
# language_age.plot(kind='line', figsize=(12, 7))
# plt.title('Liczba użytkowników wg grupy wiekowej i preferowanego języka')
# plt.xlabel('Grupa wiekowa')
# plt.ylabel('Liczba użytkowników')
# plt.xticks(rotation=45)
# plt.legend(title='Język preferowany')
# plt.tight_layout()
# plt.show()

language_age = df.groupby(['age_group', "language_preferred"])['user_id'].count()
language_age = pd.DataFrame(language_age.unstack(level=0))
print(language_age)
# age_group           0-18 years  19-24 years  ...  45-55 years  55+ years
# language_preferred                           ...
# Arabic                      19           26  ...           21         22
# English                   1421         1560  ...         1240       1101
# German                      31           29  ...           25         12
# Spanish                     68           67  ...           67         52

language_age.plot(kind="bar")
plt.title("Język w zależności od wieku")
plt.xlabel("Wiek")
plt.ylabel("Użytkownicy")
plt.legend(loc="upper left", labels=language_age.columns.values)
plt.show()
