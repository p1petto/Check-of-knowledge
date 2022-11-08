import math

def pythagorean_triples(n, m):
    l = []
    if n < m:
        for i in range(n, m):
            for j in range (i + 1, m + 1):
                c = i ** 2 + j ** 2
                if math.sqrt(c) == round(math.sqrt(c)):
                    c = math.sqrt(c);
                    l.append([i, j, int(c)])
    return l

def test_task():
    assert pythagorean_triples(1, 10) == [[3, 4, 5], [6, 8, 10]]