"""
    1. Если в строке больше символов в нижнем регистре - вывести все в нижнем,
        если больше в верхнем - вывести все в верхнем,
        если поровну - вывести в противоположных регистрах.

    2. Если в строке каждое слово начинается с заглавной буквы, тогда
        добавить в начало строки 'done. '.
        Иначе заменить первые 5 элементов строки на 'draft: '.
    (можно использовать метод replace и/или конкатенацию строк + срезы)

    3. Если длина строки больше 20, то обрезать лишние символы до 20.
        Иначе дополнить строку символами '@' до длины 20.
    (можно использовать метод ljust либо конкатенацию и дублирование (+ и *))

    После выполнения кажого пункта выводить результат типа:
        1. Исходная строка: "some string".
        Результат: "some edited string".
    (Использовать форматирование строк f либо метод format)
"""

# можно заменить данную строку на input()
# string = 'Lorem, Ipsum, is, sImPlY, duMMy, TEXT, of, The, printing, INDUSTRY.'


string = input()

some_word = "edited"
count_l = 0
count_u = 0

for char in string:
    if char.islower() is True:
        count_l += 1
    elif char.isupper() is True:
        count_u += 1

if count_u > count_l:
    print(string.upper())
elif count_l > count_u:
    print(string.lower())
else:
    print(string.swapcase())
print(f"some {some_word} string")


if string.istitle():
    print("done. " + string)
else:
    print(string.replace(string[:6], "draft: "))
print(f"some {some_word} string")


if len(string) > 20:
    print(string[:20])
else:
    print(string.ljust(20, "@"))
print(f"some {some_word} string")