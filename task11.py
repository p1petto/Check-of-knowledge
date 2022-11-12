import time
from memory_profiler import profile

@profile
def first(l):
    a = l.copy()
    return a.pop()

@profile
def second(l):
    return l[len(l) - 1]

@profile
def third(l):
    return l[-1]

l = [x for x in range(1000)]

time_start = time.time()
print("Через pop()", first(l))
time_elapsed = (time.time() - time_start)
print("Время на выполнение", time_elapsed)

time_start = time.time()
print("Через len()", second(l))
time_elapsed = (time.time() - time_start)
print("Время на выполнение", time_elapsed)

time_start = time.time()
print("Через [-1]", third(l))
time_elapsed = (time.time() - time_start)
print("Время на выполнение", time_elapsed)
