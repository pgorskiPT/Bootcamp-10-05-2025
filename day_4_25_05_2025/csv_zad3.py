import pandas

# pip install pandas

data = pandas.read_csv('dane/records_discount.csv', delimiter=";")

print(data)
#    sku    exp_date   price
# 0    1  2025-05-25  100.00
# 1    2  2025-05-25  200.00
# 2    3  2025-05-26  499.99
# 3    4  2025-05-25   50.00
# 4    5  2025-05-26   80.00

print(data.columns) # Index(['sku', 'exp_date', 'price'], dtype='object')
print(data.values)
#  Index(['sku', 'exp_date', 'price'], dtype='object')
# [[1 '2025-05-25' 100.0]
#  [2 '2025-05-25' 200.0]
#  [3 '2025-05-26' 499.99]
#  [4 '2025-05-25' 50.0]
#  [5 '2025-05-26' 80.0]]

print(data.items)
# <bound method DataFrame.items of    sku    exp_date   price
# 0    1  2025-05-25  100.00
# 1    2  2025-05-25  200.00
# 2    3  2025-05-26  499.99
# 3    4  2025-05-25   50.00
# 4    5  2025-05-26   80.00>