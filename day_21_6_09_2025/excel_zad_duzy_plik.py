import openpyxl

import lxml  # przyspiesza proces zapisu

book = openpyxl.Workbook(write_only=True)
# write_only=True - optymalizuje zużycie pamieci
# przy tej fladze nie dziła book.active
sheet = book.create_sheet()

# 1000 x 200 komórek
for row in range(1000):
    sheet.append(list(range(200)))

book.save("openpyxl_optimized.xlsx")