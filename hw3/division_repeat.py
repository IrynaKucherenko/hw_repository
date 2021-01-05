"""
    Программа принимает на ввод 5-ти значное число.
    Заменяет каждую вторую цифру на 0 и выводит результат.

    [in] 12345
    [out] 10305

    * Если введено не 5-ти значное число
        либо не число обработать и вывести соответствующее сообщение.
"""

try:
    a = int(input("number: "))

    if (a < 10000) or (a > 99999):
        print("Range error! Enter five-digit number")
        exit()
    var_b = a // 1000
    var_c = a // 10
    var_d = var_c // 10
    three = var_d % 10
    var_i = var_c * 10
    five = a - var_i
    one = var_b // 10
    two = var_b % 10
    four = var_c % 10
    print(one, 0, three, 0, five)
except ValueError:
    print("It's not numbers!")

