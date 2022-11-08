import math

def is_fibonacci(n):
    """Натуральное число n является числом Фибоначчи тогда
    и только тогда, когда 5n^2 + 4 или 5n^2 - 4 является квадратом"""
    if (math.sqrt(5 * n ** 2 + 4) == round(math.sqrt(5 * n ** 2 + 4))
            or math.sqrt(5 * n ** 2 - 4) == round(math.sqrt(5 * n ** 2 - 4))):
        return True
    return False

def test_fib1():
    assert is_fibonacci(50) == (False)

def test_fib2():
    assert is_fibonacci(610) == (True)

def test_fib2():
    assert is_fibonacci(1) == (True)

def test_fib2():
    assert is_fibonacci(3) == (True)