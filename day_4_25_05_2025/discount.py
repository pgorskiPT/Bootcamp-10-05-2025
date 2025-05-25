from datetime import date, datetime, timedelta

today = date.today()
print("Dzisiejsza data:", today)  # Dzisiejsza data: 2025-05-25

time = datetime.now()
print('Aktualny czas:', time)  # Aktualny czas: 2025-05-25 10:05:44.859823
print(type(time))  # <class 'datetime.datetime'>

print("Godzina:", time.hour)  # Godzina: 10
print("Dzień:", today.day)  # Dzień: 25

formated_date = datetime.now().strftime("%d/%m/%Y")
print("Dzisiejsza data (sformatowana):", formated_date)
# Dzisiejsza data (sformatowana): 25/05/2025

# 10:10
formated_time = datetime.now().strftime("%H:%M")
print("Aktualna godzina:", formated_time)  # Aktualna godzina: 10:14 -> 09:14 -> 9:14
print("Aktualna godzina:", formated_time.removeprefix("0"))  # Aktualna godzina: 10:14 -> 09:14 -> 9:14

formated_time_usa = datetime.now().strftime("%I:%M %p")
print("Aktualna godzina (USA):", formated_time_usa)  # Aktualna godzina (USA): 10:18 AM
print(type(formated_time_usa))  # <class 'str'>

time_from_str = datetime.now().strptime("25/05/2025", "%d/%m/%Y")
print("data ze stringa:", time_from_str)  # data ze stringa: 2025-05-25 00:00:00
print(type(time_from_str))  # <class 'datetime.datetime'>
