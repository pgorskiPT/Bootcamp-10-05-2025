import time

import whisper
# pip install torch torchvision torchaudio
import ssl
import urllib.request
import torch
# device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")

start = time.perf_counter()

print(torch.backends.mps.is_available())  # Powinno zwrócić True


time_prefix = False
ssl._create_default_https_context = ssl._create_unverified_context

# device = "mps" if torch.backends.mps.is_available() else "cpu"
device = "cpu" if torch.backends.mps.is_available() else "cpu"
print(f"Używam: {device}")
print("Start...")
# model = whisper.load_model('medium')
model = whisper.load_model('small', device=device)
# model = whisper.load_model('tiny')
# result = model.transcribe("audio_file.wav", word_timestamps=True)
result = model.transcribe("audio_file1.wav", word_timestamps=True)

# print(result["segments"])
end = time.perf_counter()
elapsed = end - start
output_filename = 'transkrypcja_medium.txt'

with open(output_filename, "w") as file:
    for segment in result['segments']:
        start_time = segment['start']
        end_time = segment['end']

        formatted_start = f"{int(start_time // 3600):02}:{int((start_time % 3600) // 60):02}:{int(start_time % 60):02}"
        formatted_end = f"{int(end_time // 3600):02}:{int((end_time % 3600) // 60):02}:{int(end_time % 60):02}"
        if not time_prefix:
            formatted_end = ""
            formatted_start = ""
        for sentence in result['text'].split("."):
            if sentence.strip():
                file.write(f"[{formatted_start} - {formatted_end}] {sentence.strip()}.\n")

print("Transkrypcja zostałą zakończona")
print(f"✅ Transkrypcja została zakończona")
print(f"📄 Zapisano do pliku: {output_filename}")
print(f"⏱ Czas działania: {elapsed:.2f} sekund")