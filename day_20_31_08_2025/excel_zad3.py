# pip install xlrd
import xlrd
import sys
print(sys.version)      # pełny string, np. '3.13.2 (main, Aug  5 2025, ...)'
print(sys.version_info)
import sys
print(sys.executable)
from xlwt.Utils import cell_to_rowcol2 # problem pythona 3.13

person = xlrd.open_workbook('dane_person.xls')

print(person)  # <xlrd.book.Book object at 0x10765da90>
print(person.sheet_names())  # ['Arkusz1']

sheet = person.sheet_by_index(0)
print(sheet.name)  # Arkusz1

sheet = person.sheet_by_name("Arkusz1")
print(sheet.name)  # Arkusz1

print(sheet.nrows)  # 2 wiersze
print(sheet.ncols)  # 3 koluny

print(sheet.cell(1, 0).value)  # Radek
print(sheet.cell(*cell_to_rowcol2("B1")).value)
