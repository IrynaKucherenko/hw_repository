"""
    Вводится строка.

    1. Вывести количество слов в введенной строке.
    2. Вывести самое длинное слово и его длину.
"""

string = input('Enter a string: ')

new_string = string.split()
l = len(new_string)
max_length = 0
max_word = ""

for word in new_string:
    if len(word) > max_length:
        max_length = len(word)
        max_word = word

print("words:", l, "\nmax_word:", max_word, "\nlen(max_word):", len(max_word))

