from datetime import datetime
from typing import List

import requests
from pydantic import BaseModel

# kody walut https://pl.wikipedia.org/wiki/ISO_4217
# url = "https://api.nbp.pl/api/exchangerates/rates/A/EUR/?format=json"
url = "https://api.nbp.pl/api/exchangerates/rates/A/EUR/"

response = requests.get(url)
print(response)
print(response.text)

table = response.json()
print(table)
print(type(table))  # <class 'dict'>

print(f"Waluta: {table['currency']}")  # Waluta: euro
print(f"Rates: {table.get('rates')}")  # Rates: [{'no': '114/A/NBP/2025', 'effectiveDate': '2025-06-13', 'mid': 4.272}]

print(f"""
Kurs waluty: {table['currency']}
na dzien: {table['rates'][0]['effectiveDate']}
wynosi: {table['rates'][0]['mid']} zł.""")


# Kurs waluty: euro
# na dzien: 2025-06-13
# wynosi: 4.272 zł.

# Prerobic na obiekty

class Rate(BaseModel):
    no: str
    # effectiveDate: str
    effectiveDate: datetime
    mid: float


class CurrencyData(BaseModel):
    table: str
    currency: str
    code: str
    rates: List[Rate]


currency_data = CurrencyData(**table)
print(currency_data)
# Kurs waluty: euro
# na dzien: 2025-06-13
# wynosi: 4.272 zł.
# table='A' currency='euro' code='EUR' rates=[Rate(no='114/A/NBP/2025', effectiveDate='2025-06-13', mid=4.272)]

print(currency_data.currency)
print(currency_data.code)
print(currency_data.rates[0])
print(currency_data.rates[0].mid)
print(currency_data.rates[0].effectiveDate)
# euro
# EUR
# no='114/A/NBP/2025' effectiveDate='2025-06-13' mid=4.272
# 4.272
# 2025-06-13

# table='A' currency='euro' code='EUR' rates=[Rate(no='114/A/NBP/2025', effectiveDate=datetime.datetime(2025, 6, 13, 0, 0), mid=4.272)]
# euro
# EUR
# no='114/A/NBP/2025' effectiveDate=datetime.datetime(2025, 6, 13, 0, 0) mid=4.272
# 4.272
# 2025-06-13 00:00:00

print(type(currency_data.rates[0].effectiveDate))  # <class 'datetime.datetime'>
effectiveDate = currency_data.rates[0].effectiveDate
formated_date = effectiveDate.strftime("%d/%m/%Y")
print(f"Data tabeli: {formated_date}")  # Data tabeli: 13/06/2025
