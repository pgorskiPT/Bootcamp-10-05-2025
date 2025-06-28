import requests

url = "http://numbersapi.com/random/year?json"
response = requests.get(url)
data = response.json()

# print(data)
# {'text': "942 is the year that Kaminarimon, the eight-pillared gate to Japan's Kinryuzan Sensouji
# Temple, is erected.", 'number': 942, 'found': True, 'type': 'year'}

print("\nQuestion:")
print(data['text'].replace(str(data['number']), "___"))

user_answer = input("\nWhat year did this happen? ")

if user_answer == str(data['number']):
    print("Correct! You got it right!")
else:
    print(f"That's incorrect. The correct year was {data['number']}")