"""
    Определить, существует ли треугольник.

    Программа принимает на ввод 3 стороны треугольника.
    Выводит стороны и текст, существует треугольник или нет.

    * у треугольника каждая сторона меньше суммы двух других сторон
"""

try:
    a = int(input("a= "))
    b = int(input("b= "))
    c = int(input("c= "))

    if (a < (c + b)) and (b < (a + c)) and (c < (a + b)):
        print(" triangle")
    else:
        print("not triangle")
except ValueError:
    print("enter only numbers!")
