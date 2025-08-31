# pip install xlrd
import xlrd

# from xlwt.Utils import cell_to_rowcol2 # problem pythona 3.13

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
