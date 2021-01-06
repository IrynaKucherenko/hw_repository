"""
    Генератор паролей.
    Пользователь выбирает 1 из 3 вариантов:
    1. Сгенерировать простой пароль(только буквы в нижнем регистре, 8 символов)
    2. Сгенерировать средний пароль (любые буквы и цифры, 8 символов)
    3. Сгенерировать сложный пароль (минимум 1 большая буква, 1 маленькая, 1 цифра и 1 спец-символ, длина от 8 до 16 символов)
        (для 3 пункта можно генерировать пароли до тех пор, пока не выполнится условие)

    Для решения использовать:
    - константы строк из модуля string (ascii_letters, digits и т.д.)
    - функцию choice из модуля random (для выборки случайного элемента из последовательности)
    - функцию randint из модуля random (для генерации случайной длины сложного пароля от 8 до 16 символов)


    Дополнительно:
    1. Позволить пользователю выбирать длину пароля, но предупреждать, что
        пароль ненадежный, если длина меньше 8 символов
    2. Добавить еще вариант генерации пароля - 4. Пользовательский пароль:
        - пользователь вводил пул символов, из которых будет генерироваться пароль
        - вводит длину желаемого пароля
        - программа генерирует пароль из нужной длины из введенных символов
        - * игнорируются пробелы

"""

import string
import random


def main():
    a = input(
        "1. Сгенерировать простой пароль\n"
        "2. Сгенерировать средний пароль\n"
        "3. Сгенерировать сложный пароль\n"
        "4. Пользовательский пароль\n"
        "5. Выход\n"
        "Enter: "
    )

    if a == "1":
        print(easy())
    elif a == "2":
        print(mid())
    elif a == "3":
        print(diff())
    elif a == "4":
        print(choice_all())
    elif a == "5":
        return None


def easy():
    pas = string.ascii_lowercase
    size = 8
    return "".join(random.choice(pas) for x in range(size))


def mid():
    pas = string.ascii_letters + string.digits
    size = 8
    return "".join(random.choice(pas) for x in range(size))


def diff():
    pas = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
    size = random.randint(8, 12)
    return "".join(random.choice(pas) for x in range(size))


def choice_all():
    size = int(input("pass length: "))
    if size < 8:
        print("easy")
        ask = input("another length ? y/n: ")
        if ask == "y":
            return choice_all()
    s = input("Enter symbols:")
    s = s.replace(" ", "")
    return "".join(random.choice(s) for x in range(size))


main()
