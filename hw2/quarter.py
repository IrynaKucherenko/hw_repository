"""
    Программа принимает на ввод координаты точки - x и y.
    Выводит, в какой четверти системы координат лежит точка.

                ^ y
                |
            II  |    I
                |
        --------=-------->
                |         x
            III |    IV
                |
"""

try:
    x = float(input("x= "))
    y = float(input("y= "))
    if x > 0 and y > 0:
        print("quarter 1")
    elif x < 0 and y > 0:
        print("quarter 2")
    elif x < 0 and y < 0:
        print("quarter 3")
    elif x > 0 and 0 > y:
        print("quarter4")
    elif x == 0 and y == 0:
        print("the origin")
    elif x == 0:
        print("point on the y-axis")
    elif y == 0:
        print("point on the x-axis")
except ValueError:
    print("enter only numbers!")
