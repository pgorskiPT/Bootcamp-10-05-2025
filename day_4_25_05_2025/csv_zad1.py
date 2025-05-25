# pliki csv - dane oddzielone znakiem podziału, pliki tekstowe
# ,;tab
# imię,opis,ocena
# Andrzej Nowak,fajny,4
# "Jan Wiśniewski","fajny","2"
# Kowalski,"wiecznie pyta ""która godzina"", ale może być",5
import csv  # biblioteka do działan z plikami csv

row = ["Radek", 'Coe', "3", 0]
fields = ['name', 'branch', 'year', 'cgpa']

# połaczenie kolekcji i rzutowanie na słownik
zipped_dict = dict(zip(fields, row))
print(zipped_dict)  # {'name': 'Radek', 'branch': 'Coe', 'year': '3', 'cgpa': 0}
print(type(zipped_dict))  # <class 'dict'>

with open("dane/records.csv", "w", newline="") as csv_f:
    csvwriter = csv.writer(csv_f)  # narzędzie do zapisu plików csv
    csvwriter.writerow(row)

with open("dane/records_2.csv", "w", newline="") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(fields)
    csvwriter.writerow(row)

with open("dane/records_3.csv", "w", newline="") as csv_f:
    csv_dict_writer = csv.DictWriter(csv_f, fieldnames=fields)
    csv_dict_writer.writeheader()  # zapisz nazwy kolumn
    csv_dict_writer.writerow(zipped_dict) # zapis dannych z jedego słownika
