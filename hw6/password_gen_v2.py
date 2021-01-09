"""
    Обновите генератор паролей из hw5/password_gen.py таким образом,
    чтобы генерировались только уникальные пароли.

    Для этого можно записывать пароли в файл, а при генерации нового
    сравнивать его с содержимым файла.
"""

import string
import random

hw = open("files/password_gen.txt", "w+")


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
        pas = pas_light()
        print(pas)
        hw.seek(0)
        password = hw.read()
        if pas == password:
            return pas_light()
        else:
            hw.write(pas)
            hw.close()

    elif a == "2":
        pas = pas_medium()
        print(pas)
        hw.seek(0)
        password = hw.read()
        if pas == password:
            return pas_medium()
        else:
            hw.write(pas)
            hw.close()

    elif a == "3":
        pas = pas_hard()
        print(pas)
        hw.seek(0)
        password = hw.read()
        if pas == password:
            return pas_hard()
        else:
            hw.write(pas)
            hw.close()

    elif a == "4":
        pas = pas_complex()
        print(pas)
        hw.seek(0)
        password = hw.read()
        if pas == password:
            return pas_complex()
        else:
            hw.write(pas)
            hw.close()

    elif a == "5":
        return None
    else:
        return main()


def pas_light():
    pas = string.ascii_lowercase
    size = 8
    pas = ("".join(random.choice(pas) for x in range(size)))
    return pas


def pas_medium():
    pas = string.ascii_letters + string.digits
    size = 8
    pas = ("".join(random.choice(pas) for x in range(size)))
    return pas


def pas_hard():
    pas = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
    size = random.randint(8, 12)
    pas = ("".join(random.choice(pas) for x in range(size)))
    return pas


def pas_complex():
    size = int(input("pass length: "))
    if size < 8:
        print("easy")
        ask = input("another length ? y/n: ")
        if ask == "y":
            return pas_complex()
    s = input("Enter symbols:")
    s = s.replace(" ", "")
    pas = ("".join(random.choice(s) for x in range(size)))
    return pas


main()

