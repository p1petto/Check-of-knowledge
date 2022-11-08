import math
from memory_profiler import profile
import time

def number_of_dividers(n):
    """Для оптимизации считаем только до корня
    само число тоже является делителем"""
    count_d = 0
    for i in range(1, math.trunc(math.sqrt(n))):
        if n % i == 0:
            count_d += 2
        if math.sqrt(n) == math.trunc(math.sqrt(n)):
            count_d += 1
    return count_d

@profile
def main():
    time_start = time.time()
    n = int(input("Введите число"))
    print(number_of_dividers(n))
    time_elapsed = (time.time() - time_start)
    print("Время на выполнение", time_elapsed)
main()
