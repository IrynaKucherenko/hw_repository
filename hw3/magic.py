"""
    Магическое число.
    При запуске программы генерируется число, которое нужно угадать.
    Подсказки: больше или меньше.
    Программа в бесконечном цикле.
    После отгадывания появляется результат: само число, количество попыток,
        а так же вопрос: "Continue? (y/n)"

    * Для генерации случайного числа можно воспользоваться
        функцией random.randint(-inf, +inf),
        где -inf - +inf - диапазон возможных чисел
"""

import random

random_number = random.randint(1, 100)  # случайное число от 1 до 100

counter = 0

while True:
    a = int(input("enter number 1-100: "))
    counter += 1

    if a > random_number:
        print("more then magic")
    elif a < random_number:
        print("less than magic ")
    else:
        print("BINGO!")
        print("Try: ", counter)
        answer = str(input("Continue? (y/n)"))
        if answer != "y":
            print("Game over")
            break

        random_number = random.randint(1, 10)
        counter = 0
