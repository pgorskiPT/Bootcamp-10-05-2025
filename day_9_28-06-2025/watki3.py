import os
from concurrent.futures import ProcessPoolExecutor


def worker(i):
    print(f"Proces: {i} w PID {os.getpid()}")


print(__name__)  # __mp_main__

# with ProcessPoolExecutor(max_workers=5) as executor:
#     for i in range(20):
#         executor.submit(worker, i)
# #  This probably means that you are not using fork to start your
#         child processes and you have forgotten to use the proper idiom
#         in the main module:
#
#             if __name__ == '__main__':
#                 freeze_support()
#                 ...

# przy ProcessPoolExecutor musimy uzywac __main__
if __name__ == '__main__':
    with ProcessPoolExecutor(max_workers=5) as executor:
        for i in range(20):
            executor.submit(worker, i)
