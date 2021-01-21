"""
    Реализовать декораторы:
    1. @time_decorator - считает и выводит время работы функции,
        если функция выполняется дольше 5 секунд, тогда дополнительно
        выводить сообщение print(f'{func.__name__} - very slow function')

    * в func.__name__ лежит название функции

    2. @slow_decorator - замедляет выполнение функции на 5 секунд

"""

import time


def time_decorator(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        number = func(*args, **kwargs)
        end = time.time() - start
        print("Время выполнения функции: %f" % end)
        if end > 5:
            print(f'{phone_number} - very slow function')
        return number

    return wrapper


@time_decorator
def phone_number():
    number = input("Phone number:")
    a = ("".join(s for s in number if s.isdigit()))
    number = ("+38" + a[-10:])
    if len(number) != 13:
        print("Wrong format. Try again.")
        return phone_number()
    return number


print(phone_number())

#######################################################
def slow_decorator(func):
    def wrapper(*args, **kwargs):
        number = func(*args, **kwargs)
        time.sleep(5)
        return number

    return wrapper


@slow_decorator
def phone_number():
    number = input("Phone number:")
    a = ("".join(s for s in number if s.isdigit()))
    number = ("+38" + a[-10:])
    if len(number) != 13:
        print("Wrong format. Try again.")
        return phone_number()
    return number


print(phone_number())

