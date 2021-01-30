"""
    Для того, чтобы больше попрактиковаться с классами
    воспользуйтесь задачником http://www.itmathrepetitor.ru/zadachi-na-klassy/

    Реализуйте класс Alphabet.

    Алфавит имеет такие атрибуты:
    - language (язык)
    - letters (список букв алфавита)

    Объект алфавита может (методы):
    - вывести все буквы алфавита
    - посчитать количество букв алфавита
    - определять, относится ли буква к этому алфавиту
"""

import string


class Alphabet:
    def __init__(self, language, letters):
        self.language = language
        self.letters = letters

    def get_language(self):
        if self.language == "Eng":
            a = ord("a")
            self.letters = string.ascii_lowercase
            return self.letters, len(self.letters)
        elif self.language == "Greek":
            α = ord("α")
            self.letters = ''.join([chr(i) for i in range(α, α + 25)])
            return self.letters, len(self.letters)
        elif self.language == "Rus":
            а = ord("а")
            self.letters = ''.join(
                [chr(i) for i in range(а, а + 6)] + [chr(а + 33)] + [chr(i) for i in range(а + 6, а + 32)])
            return self.letters, len(self.letters)

    def test_letters(self):
        a = input("alpha: ")
        if a in self.letters:
            print(self.language)
        else:
            print("letter from another alphabet")


l1 = Alphabet("Eng", "а")
print(l1.get_language())
l1.test_letters()
l2 = Alphabet("Greek", "a")
print(l2.get_language())
l2.test_letters()
l3 = Alphabet("Rus", "α")
print(l3.get_language())
l3.test_letters()

