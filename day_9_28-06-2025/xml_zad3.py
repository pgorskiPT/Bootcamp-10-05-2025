from xml.dom import minidom

DOMTree = minidom.parse("dane.xml")
# DOMTree = minidom.parse("../dane.xml") katalog wyżej
print(DOMTree.toxml())
# <?xml version="1.0" ?>
# <znajomi>
#     <osoba>
#         <imie foo="zzz">Zygmunt</imie>
#         <email>1@1.pl</email>
#     </osoba>
#     <osoba>
#         <imie foo="aaaa">Janina</imie>
#         <email>2@2.pl</email>
#     </osoba>
# </znajomi>

cNodes = DOMTree.childNodes
print(cNodes)  # [<DOM Element: znajomi at 0x1032cc8c0>]

znajomi = cNodes[0]
print("Znajomi:", znajomi)
# Znajomi: <DOM Element: znajomi at 0x1050908c0>

print(znajomi.getElementsByTagName("osoba"))
# [<DOM Element: osoba at 0x104d089e0>, <DOM Element: osoba at 0x104d08b90>]

persons = znajomi.getElementsByTagName("osoba")
print(persons[0].toxml())
# <osoba>
#         <imie foo="zzz">Zygmunt</imie>
#         <email>1@1.pl</email>
#     </osoba>

print(persons[1].toxml())
# <osoba>
#         <imie foo="aaaa">Janina</imie>
#         <email>2@2.pl</email>
#     </osoba>

osoba = persons[0]
imie = osoba.getElementsByTagName("imie")[0]  # bo dostajemy listę [<DOM Element: imie at 0x102a2ca70>]
print(imie)
imie1 = imie.firstChild.data
print(imie1)  # Zygmunt
atrybut = imie.getAttribute("foo")
print(atrybut)  # zzz, wartość dla atrybutu "foo"
# PRzerwa 11:30
