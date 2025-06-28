import requests

client_id = ""
token_url = "https://dribbble.com/oauth/token"
client_secret = ""
auth_code = input("Wklej kod autoryzacyjny:")

response = requests.post(
    token_url,
    headers={"Accept": "application/json"},
    data={
        "client_id": client_id,
        "client_secret": client_secret,
        "code": auth_code,
        "grant_type": "authorization_code"
    }
)

if response.status_code == 200:
    print(response.json())
    access_token = response.json()["access_token"]
    print(f"Token dostepu: {access_token}")
else:
    print("Bład w uzyskaniu tokenu:", response.json())
