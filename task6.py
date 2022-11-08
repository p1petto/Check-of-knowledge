def get_info_even_odd(n):
    sum_even = 0
    sum_odd = 0
    num_even = n / 2
    num_odd = n / 2 + n % 2

    for i in range(1, n):
        if i % 2 == 0:
            sum_even += i
        else:
            sum_odd += i

    return sum_even, sum_odd, num_even, num_odd

def main():
    n = int(input("Введите число"))
    print ("кол-во четных:", get_info_even_odd(n)[2])
    print ("кол-во нечетных:", get_info_even_odd(n)[3])
    print ("сумма четных:", get_info_even_odd(n)[0])
    print ("сумма нечетных:", get_info_even_odd(n)[1])

main()