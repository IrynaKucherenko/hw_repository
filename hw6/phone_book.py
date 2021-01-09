"""
    Текстовый файл (phone_book.txt) содержит список из имен и номеров телефона.
    Переписать в файл (edited_phone_book.txt) данные владельцев,
    чьи имена начинаются на букву "m" либо заканчиваются на "а"
    (регистр не имеет значения).

    В файл записывать данные в таком формате:
    1. +380501234561 - Имя
    2. +380501234562 - Имя
    3. +380501234563 - Имя
    4. +380501234564 - Имя
"""


class PhoneBookRecord:
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def __str__(self):
        return "{0} {1}".format(self.number, self.name)


a = open("files/edited_phone_book.txt", "r+")


def phone_number(src):
    number = "".join(src)
    number = "".join(i for i in number if i.isalnum())
    prefix = 13 - len(number)
    if prefix > 0 and prefix < 5:
        number = "+380"[0:prefix] + number
    return number


with open("files/phone_book.txt") as f:
    lines = f.readlines()
    num = 0
    for line in lines:
        items = line.split()
        name = items[0]
        number = phone_number(items[1:])
        r = PhoneBookRecord(name, number)
        if r.name.endswith(("A", "a")) or r.name.startswith(("m", "M")):
            s = str(r)
            test_s = s.replace(" ", " - ").replace("+", "\n+")
            for i in test_s:
                if i == "+":
                    num += 1
                    string = test_s.replace("\n", "")
                    correct_string = (f"{num}, {string}\n")
                    a.write(correct_string)










