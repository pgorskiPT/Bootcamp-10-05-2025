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
language_age.plot(kind="bar")
plt.title("Język w zależności od wieku")
plt.xlabel("Wiek")
plt.ylabel("Użytkownicy")
plt.legend(loc="upper right", labels=language_age.columns.values)
plt.show()

language_age.plot(kind='line', figsize=(12, 7))
plt.title('Liczba użytkowników wg grupy wiekowej i preferowanego języka')
plt.xlabel('Grupa wiekowa')
plt.ylabel('Liczba użytkowników')
plt.xticks(rotation=45)
plt.legend(title='Język preferowany')
plt.tight_layout()
plt.show()
