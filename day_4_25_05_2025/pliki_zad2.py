import chardet

# pip install chardet
# !pip install chardet - w notebook jupyter
# pip - menadżer pakietów python
with open("test.log", "r") as file:
    lines = file.read()
print(lines)
# Radek
# Kolejna
# Jescze jedna
# Dodane
# Dodane
# Dodane
# Dodane
# Dśodane

file_path = "test.log"
with open(file_path, 'rb') as file:  # rb - odczyt bajtowe
    raw_data = file.read()

print(raw_data)
# b'Radek\nKolejna\nJescze jedna\nDodane\nDodane\nDodane\nDodane\nD\xc5\x9bodane\n'
# \xc5\x9b - zapis szesnastkowy dla znaaku Ś w Unicode

result = chardet.detect(raw_data)
print(result)
# {'encoding': 'Windows-1252', 'confidence': 0.73, 'language': ''}
# po zwiększeniu próbki (dodanie więcej polskich znaków w pliku) wynik poprawny
# {'encoding': 'utf-8', 'confidence': 0.938125, 'language': ''}
encoding = result["encoding"]
confidence = result["confidence"]
print("Kodowanie znaków:", encoding)
print(f"Trafność: {confidence * 100} %")
# Kodowanie znaków: utf-8
# Trafność: 93.8125 %

print(raw_data.decode(encoding=encoding))
# Radek
# Kolejna
# Jescze jedna
# Dodane
# Dodane
# Dodane
# Dodane
# Dśćąźodane
