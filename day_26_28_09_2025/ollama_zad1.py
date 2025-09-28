import requests

# # ollama pull llama3.2
# ollama pull SpeakLeash/bielik-11b-v2.3-instruct:Q4_K_M
# ollama run SpeakLeash/bielik-11b-v2.3-instruct:Q4_K_M

url = "http://localhost:11434/api/generate"
headers = {"Content-Type": "application/json"}
data = {
    "model": "SpeakLeash/bielik-11b-v2.3-instruct:Q4_K_M",
    "prompt": "Wymień trzy największe miasta w Polsce.",
    "stream": False
}

response = requests.post(url, json=data, headers=headers)
print(response.json()["response"])