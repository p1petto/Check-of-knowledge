import time
from memory_profiler import profile

@profile
def task3_1(x):
    time_start = time.time()
    time_elapsed = (time.time() - time_start)
    print("Время на выполнение", time_elapsed)
    return x**5

@profile
def task3_2(x):
    time_start = time.time()
    time_elapsed = (time.time() - time_start)
    print("Время на выполнение", time_elapsed)
    res = 1
    for i in range(5):
        res *= x
    return res

def test_task_1():
    assert task3_1(50) == (312500000)

def test_task_2():
    assert task3_2(50) == (312500000)