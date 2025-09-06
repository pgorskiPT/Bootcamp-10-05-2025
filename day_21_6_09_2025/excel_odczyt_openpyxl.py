import openpyxl

book = openpyxl.load_workbook("openpyxl_optimized.xlsx",
                              data_only=True,
                              read_only=True,
                              keep_links=False)
#   read_only=True, powoduje, że plik jest ładowany w sposób sekwencyjny
# przydatne przy dużych plikach
print(book)

for b in book:
    print(b)
    for i in b:
        print(i)
book.close()  # konieczne przy read_only=True
