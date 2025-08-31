# xlsxWriter - do tworzenia plików excel
# pip install xlsxwriter

import xlsxwriter
import datetime as dt

# tworzymy plik
# book = xlsxwriter.Workbook("xlsxwriter.xlsx")
# book = xlsxwriter.Workbook("xlsxwriter2.xlsx")
book = xlsxwriter.Workbook("xlsxwriter3.xlsx")

# tworzymy arkusz
sheet = book.add_worksheet("Arkusz1")

sheet.write("A1", 'Witaj1')
sheet.write("A2", "Witaj 2")

# formatowanie/kolory
formatting = book.add_format(
    {"font_color": "#FF0000",
     "bg_color": "#FFFF00",
     "bold": True,
     "align": "center",
     "border": 1,
     "border_color": "#FF0000"}
)
sheet.write("A3", "Witaj 3", formatting)

# formatowanie daty
date_format = book.add_format({"num_format": "yyyy/mm/dd"})
sheet.write("A4", dt.date(2016, 10, 13), date_format)

# fromatowanie wartości numerycznych
number_format = book.add_format({"num_format": "0.00"})
sheet.write("A4", 3.3333333, number_format)

book.close()
