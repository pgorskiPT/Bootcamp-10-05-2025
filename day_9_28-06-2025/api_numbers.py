import requests

url = "http://numbersapi.com/random/year?json"

response = requests.get(url)
print(response)  # <Response [200]>
data = response.json()
print(type(data))  # <Response [200]>

print(data)
# {'text': '166 is the year that Dacia is invaded by barbarians.',
# 'number': 166,
# 'found': True,
# 'type': 'year'}

print("Podaj odpowiedź n apytanie:\n", data['text'].replace(str(data['number']), ""))
odp = input("\nPodaj odpowiedź: ")

if odp == str(data['number']):
    print("Prawidłowa odpowiedź")
else:
    print("Błędna odpowiedź")

insects = 10000000000000000000
print(f"{insects:,}")  # 10,000,000,000,000,000,000
