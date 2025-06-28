from datetime import datetime

import requests
import xml.etree.ElementTree as ET
from pydantic import BaseModel
from typing import List

url = "https://api.nbp.pl/api/exchangerates/tables/A/?format=xml"

response = requests.get(url)
print(response)  # <Response [200]>
print(response.text)

#             <Rate>
#                 <Currency>dolar amerykański</Currency>
#                 <Code>USD</Code>
#                 <Mid>3.6177</Mid>
#             </Rate>

xml_data = response.content

root = ET.fromstring(xml_data)
print(root)  # <Element 'ArrayOfExchangeRatesTable' at 0x103e04720>

table_name = root.find(".//Table").text
print(f"Tabela: {table_name}")  # Tabela: A

date = root.find(".//EffectiveDate").text
print(f"Data tabeli: {date}")  # Data tabeli: 2025-06-27

no = root.find(".//No").text
print(f"Numer tabeli: {no}")  # Numer tabeli: 123/A/NBP/2025

rates = root.findall(".//Rate")
print(rates)  # [<Element 'Rate' at 0x104770950>,...

for rate in rates:
    # print(rate)
    currency = rate.find("Currency").text
    code = rate.find("Code").text
    mid = rate.find("Mid").text
    print(f"{code} : {currency} - {mid}")  # # THB : bat (Tajlandia) - 0.1109

    # THB : bat (Tajlandia) - 0.1109
    # USD : dolar amerykański - 3.6177
    # AUD : dolar australijski - 2.3700
    # HKD : dolar Hongkongu - 0.4608
    # CAD : dolar kanadyjski - 2.6521
    # NZD : dolar nowozelandzki - 2.1968
    # SGD : dolar singapurski - 2.8350
    # EUR : euro - 4.2362
    # HUF : forint (Węgry) - 0.010606
    # CHF : frank szwajcarski - 4.5307
    # GBP : funt szterling - 4.9721
    # UAH : hrywna (Ukraina) - 0.0869
    # JPY : jen (Japonia) - 0.025049
    # CZK : korona czeska - 0.1713
    # DKK : korona duńska - 0.5678
    # ISK : korona islandzka - 0.029832
    # NOK : korona norweska - 0.3604
    # SEK : korona szwedzka - 0.3829
    # RON : lej rumuński - 0.8346
    # BGN : lew (Bułgaria) - 2.1659
    # TRY : lira turecka - 0.0906
    # ILS : nowy izraelski szekel - 1.0696
    # CLP : peso chilijskie - 0.003883
    # PHP : peso filipińskie - 0.0640
    # MXN : peso meksykańskie - 0.1917
    # ZAR : rand (Republika Południowej Afryki) - 0.2025
    # BRL : real (Brazylia) - 0.6603
    # MYR : ringgit (Malezja) - 0.8555
    # IDR : rupia indonezyjska - 0.00022326
    # INR : rupia indyjska - 0.042312
    # KRW : won południowokoreański - 0.002663
    # CNY : yuan renminbi (Chiny) - 0.5047
    # XDR : SDR (MFW) - 4.9948


class Rate(BaseModel):
    currency: str
    code: str
    mid: float


class ExchangeRatesTable(BaseModel):
    table: str
    data: datetime
    number: str
    rates: List[Rate]


# deserializacja za pomocą pydantic
currency_rates = []

for rate in rates:
    # print(rate)
    currency = rate.find("Currency").text
    code = rate.find("Code").text
    mid = rate.find("Mid").text
    print(f"{code} : {currency} - {mid}")

    currency_rates.append(Rate(currency=currency, code=code, mid=float(mid)))

date = datetime.strptime(date, "%Y-%m-%d")

exchange_rate_table = ExchangeRatesTable(
    table=table_name,
    data=date,
    number=no,
    rates=currency_rates
)

print(exchange_rate_table)
# table='A' data='2025-06-27' number='123/A/NBP/2025'
# rates=[Rate(currency='bat (Tajlandia)', code='THB', mid=0.1109),
# table='A' data=datetime.datetime(2025, 6, 27, 0, 0) number='123/A/NBP/2025'

rates_pydantic = exchange_rate_table.rates
for rate in rates_pydantic:
    print(rate)
# currency='SDR (MFW)' code='XDR' mid=4.9948
# currency='dolar amerykański' code='USD' mid=3.6177
