import math
def all_dividers(n):
    l = []
    for i in range(1, n):
        if n % i == 0:
            l.append(i)
    return l

def sum_of_dividers(n):
    l = all_dividers(n)
    return sum(l)

def perfect_values(n):
    l = []
    if n < 5:
        i = 2
        while (True):
            if (sum_of_dividers(i) == i):
                l.append(i)
                n -= 1
            if (n < 1):
                return l
            i += 1

print(perfect_values(4))