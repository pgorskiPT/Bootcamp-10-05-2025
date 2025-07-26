import random
import time
import threading
import multiprocessing
from concurrent.futures import ThreadPoolExecutor

import numpy as np

total_points_inside_circle = 0


# def monte_carlo_pi(n):
#     points_inside_circle = 0
#
#     for _ in range(n):
#         x = random.uniform(-1, 1)
#         y = random.uniform(-1, 1)
#
#         if x ** 2 + y ** 2 <= 1:
#             points_inside_circle += 1
#
#     return 4 * (points_inside_circle / n)

# z wykorzystaniem numpy
def monte_carlo_pi(num_sample):
    x = np.random.uniform(-1, 1, num_sample).astype(np.float32)
    y = np.random.uniform(-1, 1, num_sample).astype(np.float32)

    inside_circle = x ** 2 + y ** 2 <= 1
    num_inside_circle = np.sum(inside_circle)
    pi_estimate = 4 * num_inside_circle / num_sample

    return pi_estimate


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


def with_processes(iterations):
    num_processes = 8
    iterations_per_process = iterations // num_processes

    start = time.time()
    with multiprocessing.Pool(num_processes) as pool:
        result = pool.map(monte_carlo_pi, [iterations_per_process] * num_processes)

        pi = sum(result) / num_processes
        end = time.time()
        print(f"Z procesami: {pi}, czas {end - start}")


def with_thread_pool_executor(iterations):
    num_threads = 8
    iterations_per_thread = iterations // num_threads

    start = time.time()
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        result = list(executor.map(monte_carlo_pi, [iterations_per_thread] * num_threads))
        pi = sum(result) / num_threads

    end = time.time()
    print(f"Z ThreadPoolExecutor: {pi}, czas: {end - start}")


# iterations = 10_000_000
# iterations = 50_000_000
iterations = 500_000_000
if __name__ == '__main__':
    no_threads(iterations)
    with_threads(iterations)
    with_processes(iterations)
    with_thread_pool_executor(iterations)
# Bez wątków: 3.14202, czas: 2.81632399559021
# Bez wątków: 3.1417344, czas: 13.558860063552856 przy 50_000_000
# Bez wątków: 3.14113496, czas: 13.856833696365356
# Z wątkami: 3.1415748000000003, czas 13.144520044326782
# Z procesami: 3.14130368, czas 3.0923409461975098
# Z ThreadPoolExecutor: 3.14145656, czas: 13.134495973587036
# z numpy
# Bez wątków: 3.14128992, czas: 0.7234160900115967
# Z wątkami: 3.14194648, czas 0.4711921215057373
# Z procesami: 3.1415516799999996, czas 0.5735378265380859
# Z ThreadPoolExecutor: 3.1415332000000005, czas: 0.4754297733306885