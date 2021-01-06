"""
    Вводится число от 1 до 999
    (если введено не число либо число вне диапазона - вывести сообщение)

    1. Найти сумму цифр числа.
    2. Вывести на экран, порядок, в котором расположены цифры числа
        (возростание/убывание/в разброс(равны))
"""

try:
    a = int(input("number: "))
    b = a // 10
    c = b // 10
    d = a % 10
    e = b % 10
    print(c + d + e)
    if a > 999:
        print("error! number>999")
    elif b == 0:
        print(" single digit")
    elif (c < e < d) and (e < d):
        print("order magnitude")
    elif (c > e > d) or (b == e):
        print("descending order")
    elif (c > e < d) or (c < e > d):
        print("randomly")
    else:
        print("similar")
except ValueError:
    print("enter only numbers!")
