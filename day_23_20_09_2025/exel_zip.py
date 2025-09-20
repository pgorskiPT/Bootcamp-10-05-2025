from zipfile import ZipFile
import xml.etree.ElementTree as ET

# otwieramy plik Excel jako zip
with ZipFile("tabela_przestawna21.xlsx", "r") as archive:
    print(archive)
    # with archive.open("xl/worksheets/sheet1.xml") as f:
    with archive.open("xl/sharedStrings.xml") as f:
        xml_content = f.read()

print(xml_content)

root = ET.fromstring(xml_content)

shared_strings = [elem.text for elem in root.findall(".//{http://schemas.openxmlformats.org/spreadsheetml/2006/main}t")]
print("Odczytane wartości tekstowe:", shared_strings)


def convert_index_to_text(index):
    if index.isdigit():
        idx = int(index)
        if idx < len(shared_strings):
            return shared_strings[idx]
        else:
            return idx
