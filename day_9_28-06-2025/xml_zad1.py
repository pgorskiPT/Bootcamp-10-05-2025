# dane w tagach, pliki xml
#  1 <rozklad>
#  2   <miejscowosc>Poznań</miejscowosc>
#  3   <linia>
#  4       <numer>5</numer>
#  5       <poczatek>Górczyn</poczatek>
#  6       <koniec>Miłostowo</koniec>
#  7   </linia>
#  8   <linia>
#  9       <numer>105</numer>
# 10       <poczatek>Rondo Rataje</poczatek>
# 11       <koniec>Piątkowo</koniec>
# 12   </linia>
# 13 </rozklad>
from xml.dom import minidom

root = minidom.Document()  # <?xml version="1.0" ?>

xml = root.createElement('root')
root.appendChild(xml)  # <root> </root>

productChild = root.createElement('product')
productChild.setAttribute('name', "Python-to-Python")
xml.appendChild(productChild)  # <product name="Python-to-Python"/>

print(root)  # <xml.dom.minidom.Document object at 0x104445550>

xmlStr = root.toprettyxml()
print(type(xmlStr))  # <class 'str'>
print(xmlStr)
# <?xml version="1.0" ?>
# <root>
# 	<product name="Python-to-Python"/>
# </root>

savePath = "ptp.xml"
with open(savePath, "w") as f:
    f.write(xmlStr)
