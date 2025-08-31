import xlwt
import xlrd  # z python 3.12
from xlutils.copy import copy
#  pip uninstall xlwt
# pip install "xlrd==1.2.0" "xlwt==1.3.0" "xlutils==2.0.0"
import sys

print(sys.version)  # pełny string, np. '3.13.2 (main, Aug  5 2025, ...)'
print(sys.version_info)
import sys

print(sys.executable)

book = xlrd.open_workbook("xlwt.xls", formatting_info=True)
book = copy(book)
book.get_sheet(0).write(0, 0, "zmienione")

book.save("edited.xls")
