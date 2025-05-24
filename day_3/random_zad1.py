import random

# random - działania na liczbach pseudolosowych

# """Return random integer in range [a, b], including both end points."""
print(random.randint(1, 100))  # int od 1 do 100
# z prawej zbiór otwarty
print(random.randrange(1, 100))  # int od 1 do 99
print(random.randrange(6))  # od 0 do 5
print(random.random())  # 0.8378956828319916 float od 0 do 0.9999999
print(random.random() * 7)  # float od 0 do 6.999999 4.571956324439835

