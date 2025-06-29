import os
import time
from concurrent.futures import ProcessPoolExecutor


def worker(n):
    print(f"Proces: {n} w PID {os.getpid()}")
    time.sleep(1)


def main():
    with ProcessPoolExecutor(max_workers=5) as executor:
        for i in range(20):
            executor.submit(worker, i)


if __name__ == '__main__':
    main()

# Proces: 15 w PID 5982
# Proces: 16 w PID 5986
# Proces: 17 w PID 5983
# Proces: 18 w PID 5985
# Proces: 19 w PID 5984
