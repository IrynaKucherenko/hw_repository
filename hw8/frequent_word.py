"""
    Напишите функцию, которая принимает текст и
    возвращает слово, которое в этом тексте встречается чаще всего.

    Напишите несколько тестов для функции.

    * Если таких слов несколько - приоритет у первого,
        если расположить список в алфавитном порядке.
"""

#from collections import Counter


def most_common(text):
    return sorted(((x, text.count(x)) for x in set(text.split())), key=lambda x: (-x[1], x[0]))[0][0]

t_1 = "fff gg hh hh AA AA bbb bbb bbb x hh jjjjjjjj fff hh"
assert most_common(t_1) == "hh"

t_2 = "ww gg hh hh ww bbb AA hh jjjjjjjj fff ww."
assert most_common(t_2) == "hh"

t_3 = "ww ww tt tt jj jj QQ QQ "
assert most_common(t_3) == "QQ"

print("===ok===")


#def frequent_word(text):
#    a = sorted(text.split())
#    c = Counter(a)
#    n = c.most_common(1)
#    return(n)

