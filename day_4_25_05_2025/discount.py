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

# tomorrow = today + 1  # TypeError: unsupported operand type(s) for +: 'datetime.date' and 'int'
# days=0, seconds=0, microseconds=0,
#                 milliseconds=0, minutes=0, hours=0, weeks=0
tomorrow = today + timedelta(days=1)
print("Jutro będzie:", tomorrow)  # Jutro będzie: 2025-05-26

print("---- Discount ----")
products = [
    {"sku": 1, 'exp_date': today, "price": 100},
    {"sku": 2, 'exp_date': today, "price": 200},
    {"sku": 3, 'exp_date': tomorrow, "price": 499.99},
    {"sku": 4, 'exp_date': today, "price": 50},
    {"sku": 5, 'exp_date': tomorrow, "price": 80},
]

print(products[0]['price'])  # 100

for product in products:
    # print(product) # {'sku': 1, 'exp_date': datetime.date(2025, 5, 25), 'price': 100}
    # print(product['exp_date'])

    # if product['exp_date'] == today:
    #     product['price'] *= 0.8
    #     print(product['price'])
    if product['exp_date'] != today:
        continue  #
        # końćzy bieżące wykonanie pętli, nakazuje pobrać kolejny eleemnt, wraca na początek

    product['price'] *= 0.8
    print(f"""Price for sku: {product['sku']}, date: {product['exp_date']}
is now: {product['price']}""")
# 100
# Price for sku: 1, date: 2025-05-25
# is now: 80.0
# Price for sku: 2, date: 2025-05-25
# is now: 160.0
# Price for sku: 4, date: 2025-05-25
# is now: 40.0
