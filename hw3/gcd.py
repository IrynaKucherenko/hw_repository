"""
    Алгоритм Евклида. НОД - наибольший общий делитель

    1. Большее число делим на меньшее.
    2. Если делится без остатка, то меньшее число и есть НОД (следует выйти из цикла)
    3. Если есть остаток, то большее число заменяем на остаток от деления.
    4. Переходим к 1 пункту.

    * разработайте алгоритм, который работает для положительных чисел
"""

a = int(input("1 "))
b = int(input("2 "))

while a != 0 and b != 0:

    if a > b:
        a = a % b
    else:
        b = b % a
    print(a + b)
