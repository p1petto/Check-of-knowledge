import time
from memory_profiler import profile

@profile
def func(a, b, c):
    time_start = time.time()
    temp = b
    b = c
    c = a
    a = temp
    time_elapsed = (time.time() - time_start)
    print("Время на выполнение", time_elapsed)

    return a, b, c

def test_task():
    assert func(1, 2, 3) == (2, 3, 1)