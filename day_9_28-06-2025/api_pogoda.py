import requests
from datetime import datetime

API_KEY = ""

url = f"https://api.openweathermap.org/data/2.5/weather?q=Warszawa&appid={API_KEY}&&lang=pl&format=jsonl&units=metric"

page = requests.get(url)
print(page)  # <Response [200]>
print(page.text)

data = page.json()
# print(data)
print("Miasto:", data['name'])  # Miasto: Warszawa
print("Pogoda:", data['weather'][0]['description'])  # Pogoda: zachmurzenie umiarkowane
print("Aktualna temperatura:", data['main']['temp'])  # Aktualna temperatura: 19.02
print("Temperatura minimalna:", data['main']['temp_min'])  # Temperatura minimalna: 17.88
print("Temperatura maksymalna:", data['main']['temp_max'])  # Temperatura maksymalna: 19.97

# sunrise, sunset
print(50 * "-")
sunrise = data['sys']['sunrise']
print("Wschód słonca (timestamp):",
      sunrise)  # print("Wschód słonca (timestamp):", sunrise)  # Wschód słonca: 1751077023
# timestamp - liczba sekund od epoki Unixa - 1 stycznia 1970 r
dt_object_sunrise = datetime.fromtimestamp(sunrise)
print("Wschód słońca:", dt_object_sunrise)  # Wschód słońca: 2025-06-28 04:17:03

print(50 * "_")
sunset = data['sys']['sunset']
dt_object_sunset = datetime.fromtimestamp(sunset)
print("Zachód słońca (ts):", sunset)
print("Zachód słońca:", dt_object_sunset)
# __________________________________________________
# Zachód słońca (ts): 1751137269
# Zachód słońca: 2025-06-28 21:01:09
