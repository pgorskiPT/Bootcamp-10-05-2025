import random
import time
import threading
import multiprocessing
from concurrent.futures import ThreadPoolExecutor

import numpy as np

total_points_inside_circle = 0


def monte_carlo_pi(n):
    points_inside_circle = 0

    for _ in range(n):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        if x ** 2 + y ** 2 <= 1:
            points_inside_circle += 1

    return 4 * (points_inside_circle / n)


def no_threads(iterations):
    start = time.time()
    pi = monte_carlo_pi(iterations)
    end = time.time()
    print(f"Bez wątków: {pi}, czas: {end - start}")


def with_threads(iterations):
    num_thread = 8
    iterations_per_thread = iterations // num_thread
    threads = []

    def thread_monte_carlo_pi():
        global total_points_inside_circle
        points_inside_circle_th = monte_carlo_pi(iterations_per_thread)
        with lock:
            total_points_inside_circle += points_inside_circle_th

    lock = threading.Lock()
    start = time.time()
    for _ in range(num_thread):
        thread = threading.Thread(target=thread_monte_carlo_pi)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    pi = (total_points_inside_circle / num_thread)
    end = time.time()
    print(f"Z wątkami: {pi}, czas {end - start}")


# iterations = 10_000_000
iterations = 50_000_000
if __name__ == '__main__':
    no_threads(iterations)
    with_threads(iterations)

# Bez wątków: 3.14202, czas: 2.81632399559021
# Bez wątków: 3.1417344, czas: 13.558860063552856 przy 50_000_000
