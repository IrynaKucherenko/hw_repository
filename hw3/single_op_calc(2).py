"""
    Программа считает сумму/разницу/произведение/частное n чисел.
    Алгоритм:
    1. Пользователь вводит число n.
    2. Затем выбирает операцию (+, -, *, /).
    3. После этого вводит n чисел.
    4. Программа выводит результат и сообщение "Continue? (y/n)".
    5. Если пользователь вводит y, то программа выполняется сначала.
        Иначе - выводит сообщение 'Bye!' и прекращает свою работу.
"""

try:
 while True:

    a = int(input("number: "))
    s = input("sign: ")
    result = None

    for a in range(1, a + 1):
        b = int(input("num: "))
        if result is None:
            result = b
        elif s == "+":
            result += b
        elif s == "-":
            result -= b
        elif s == "*":
            result *= b
        elif s == "/":
            result /= b
        print("result: ", result)
    else:
        answer = str(input("Continue? (y/n)"))
        if answer != "y":
            print('Bye!')
            break
except ZeroDivisionError:
    print("division by zero!")





