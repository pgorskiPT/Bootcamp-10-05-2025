from numpy import random

x = random.randint(100, size=5)
print(x)  # [ 4 71 16 46 12]

x = random.randint(100, size=(3, 5))
print(x)
# [[33 34 73 75 43]
#  [17 58 36 85 61]
#  [45 71 33 90 87]]

x = random.rand(5)
print(x)  # [0.34273804 0.96834891 0.65215289 0.52568585 0.81017015]
print(x.dtype)  # float64

x = random.rand(3, 4)
print(x)
# [[0.0127836  0.3262671  0.15431102 0.6256785 ]
#  [0.64529925 0.69210495 0.7151219  0.53031409]
#  [0.39575333 0.08520256 0.57090952 0.0352661 ]]

x = random.choice([3, 5, 7, 9])
print(x)  # 7

x = random.choice([3, 5, 7, 9], size=(3, 5))
print(x)
# [[7 3 5 5 3]
#  [7 7 7 5 9]
#  [9 5 5 3 3]]

# bez powtórzeń - False
x = random.choice([3, 5, 7, 9], 2, replace=False)
print(x)  # [3 7]

gen = random.default_rng()
x = gen.choice([3, 5, 7, 9], 2, replace=False)
print(x)  # [9 3]

x = random.random_sample((5,))
print(x)
# [0.00289719 0.35712541 0.66625193 0.25652681 0.15303865] z zakresu 0.0 1.0