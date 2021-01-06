"""
    Необходимо написать простой калькулятор,
    который оперирует с двумя числами и оператором.

    В зависимости от введенного оператора,
    между числами проводится определенная операция.

    Результат выводится на экран.

    * обработать все возможные ошибки программы с помощью try-except
"""

try:
    a = float(input("num1: "))
    s = input("sign: ")
    b = float(input("num2: "))

    if s == "+":
        print(a + b)
    elif s == "-":
        print(a - b)
    elif s == "*":
        print(a * b)
    elif s == "/":
        print(a / b)
    else:
        print("Error! Need to enter sign: +, -, *, / ")
except ValueError:
    print("enter only numbers!")
except ZeroDivisionError:
    print("division by zero!")






