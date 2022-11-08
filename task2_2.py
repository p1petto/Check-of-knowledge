def check_num(n):
    b = True
    try:
        a = float(n)
    except:
        b = False
    return b

def main():
    sum = 0
    counter = int(input(("Сколько чисел вы хотите ввести?")))

    while (counter > 0):
        n = input("Введите число")
        if check_num(n):
            counter -= 1
            sum += float(n)

    print(sum)


main()
