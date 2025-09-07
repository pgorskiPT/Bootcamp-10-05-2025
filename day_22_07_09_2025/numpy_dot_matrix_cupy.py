# pip install cupy-cuda12x

from typing import Tuple
import time
import random
import cupy as cp  # Używamy CuPy zamiast NumPy

def generate_random_array2D(shape: Tuple[int, int]) -> cp.ndarray:
    # Tworzymy tablicę na CPU, potem przenosimy ją na GPU
    cpu_array = [
        [random.random() for _ in range(shape[1])]
        for _ in range(shape[0])
    ]
    return cp.array(cpu_array)  # konwersja do tablicy GPU

# Tworzenie macierzy na GPU
GPU_ARRAY_A = generate_random_array2D(shape=(500, 500))
GPU_ARRAY_B = generate_random_array2D(shape=(500, 500))

# Mnożenie na GPU
print("=" * 20)
start_time = time.time()
gpu_operation_result = GPU_ARRAY_A @ GPU_ARRAY_B  # lub cp.dot(...)
gpu_exec_time = time.time() - start_time
print(f"Time CuPy (GPU): {gpu_exec_time:.6f} s")

# Dla porównania: NumPy na CPU
import numpy as np

CPU_ARRAY_A = cp.asnumpy(GPU_ARRAY_A)
CPU_ARRAY_B = cp.asnumpy(GPU_ARRAY_B)

start_time = time.time()
numpy_result = np.dot(CPU_ARRAY_A, CPU_ARRAY_B)
cpu_exec_time = time.time() - start_time
print(f"Time NumPy (CPU): {cpu_exec_time:.6f} s")

# Porównanie wyników
diff = cp.sum(cp.abs(gpu_operation_result - cp.array(numpy_result)))
print(f"Różnica między GPU a CPU: {diff}")
print(f"Zgodność: {diff < 1e-5}")


# ====================
# Time CuPy (GPU): 0.242361 s
# Time NumPy (CPU): 0.003560 s
# Różnica między GPU a CPU: 1.4431748240895104e-08
# Zgodność: True