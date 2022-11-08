def is_right(n):
    arr_of_digit = [int(i) for i in str(n)]
    for i in range(len(arr_of_digit)):
        if arr_of_digit[i] == 0 or n % arr_of_digit[i] != 0:
            return False
    return True
def func(n, m):
    l = []
    for i in range(n, m+1):
        if (is_right(i)):
            l.append(i)

    return l

def test_task():
    assert func(10, 50) == [11, 12, 15, 22, 24, 33, 36, 44, 48]