# pip install torch transformers accelerate sentencepiece
import ssl

import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
# huggingface-cli login
# pip install accelerate
ssl._create_default_https_context = ssl._create_unverified_context

# ⚡️ Ustawienia modelu
model_name = "google/gemma-2b-it"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name, device_map="auto")

# funkcja do czatu
def chat_with_model(prompt, max_length=150):
    inputs = tokenizer.encode(prompt, return_tensors="pt").to(device)
    outputs = model.generate(inputs, max_length=max_length, do_sample=True)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response

# 🧠 Wczytaj model i tokenizer
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model_name = "google/gemma-2b-it"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained("google/gemma-2b-it").to(device)
model.eval()

print("🤖 Gemma-2b - Mini czat lokalny (wielojęzyczny). Wpisz 'exit' aby zakończyć.")
while True:
    prompt = input("\n👤 Ty: ")
    if prompt.lower() == "exit":
        break
    print("Myślę")
    response = chat_with_model(prompt)
    print(f"🤖 Gemma: {response}")