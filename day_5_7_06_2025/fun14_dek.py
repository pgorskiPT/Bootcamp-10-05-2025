import operator
import time
from functools import partial

import numpy as np


# pip install numpy
def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Czas wykonania funkcji {func.__name__}: {execution_time}")
        return result

    return wrapper


@measure_time
def my_wait():
    time.sleep(2)


@measure_time
def my_for_sum():
    suma = 0
    for i in range(15_000_000):
        suma += i
    print("Sum is:", suma)


@measure_time
def my_sum_without_for():
    total = sum(range(15_000_000))
    print("Sum is:", total)


@measure_time
def my_sum_np():
    total = np.sum(np.arange(15_000_000), dtype=np.int64)
    print('Sum is:', total)


lista = list(range(1_000_000))


@measure_time
def my_for_mul():
    l = []
    for i in lista:
        l.append(i * 2)


@measure_time
def my_for_with_map_mul():
    l_map = []
    l_map = list(map(lambda x: x * 2, lista))


@measure_time
def my_for_list_coprehensions():
    l = [i * 2 for i in lista]


@measure_time
def my_for_with_map_operator():
    l_map = list(map(partial(operator.mul, 2), lista))


my_wait()  # Czas wykonania funkcji my_wait: 2.005078077316284
my_for_sum()  # Czas wykonania funkcji my_for_sum: 0.41095519065856934
my_sum_without_for()  # Czas wykonania funkcji my_sum_without_for: 0.15706205368041992
my_sum_np()  # Czas wykonania funkcji my_sum_np: 0.025210142135620117
print("------")
my_for_mul()  # Czas wykonania funkcji my_for_mul: 0.03571605682373047
my_for_with_map_mul()  # Czas wykonania funkcji my_for_with_map_mul: 0.04247403144836426
my_for_list_coprehensions()  # Czas wykonania funkcji my_for_list_coprehensions: 0.021322965621948242
my_for_with_map_operator()  # 0.030473947525024414
