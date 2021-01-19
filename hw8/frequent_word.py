"""
    Напишите функцию, которая принимает текст и
    возвращает слово, которое в этом тексте встречается чаще всего.

    Напишите несколько тестов для функции.

    * Если таких слов несколько - приоритет у первого,
        если расположить список в алфавитном порядке.
"""


def frequent_word(text):
    return sorted(((x, text.count(x)) for x in set(text.split())), key=lambda x: (-x[1], x[0]))[0][0]


t_1 = "uuuuu, gg, hh, uuuuu"
assert frequent_word(t_1) == "uuuuu"

t_1 = "uuuuu, gg, hh, uuuuu, gg, gg "
assert frequent_word(t_1) == "gg"

t_1 = "a, bb, bb, ccc, ccc, ccc"
assert frequent_word(t_1) == "ccc"

print("===ok===")