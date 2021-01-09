"""
    1.
    Создать файл file_practice.txt
    Записать в него строку 'Starting practice with files'
    Файл должен заканчиваться пустой строкой
"""

"""
    2.
    Прочесть первые 5 символов файла и вывести содержимое в верхнем регистре
    Затем прочесть весь файл от начала до конца, вывести содержимое на экран
"""

hw = open("files/file_practice.txt", "w")
print("Starting practice with files", file=hw, end="")
hw = open("files/file_practice.txt")
hw.tell()
print(hw.read(5).upper())
hw.seek(0)
print(hw.read())
hw.close()


"""
    3.
    Прочесть файл files/text.txt
    В тексте заменить все буквы 'i' на 'e', если 'i' большее кол-во,
    иначе - заменить все буквы 'e' на 'i'
    Полученный текст дописать в файл file_practice.txt
"""

with open("files/file_practice.txt", "a+") as hw:
    hw.read()
    hw.seek(0)
    string = hw.read()

    counter_i = 0
    counter_e = 0

    for i in string:
        if i == "i":
            counter_i += 1
        elif i == "e":
            counter_e += 1

    if counter_i > counter_e:
        hw.write(" " + string.replace("i", "e"))
    else:
        string_e = string.replace("e", "i")
        hw.write(" " + string.replace("e", "i"))


"""
    4.
    Если в файле file_practice.txt четное количество элементов
    - файл должен заканчиваться строкой 'the end', иначе - строкой 'bye'
    Прочесть весь файл и вывести содержимое
"""


with open("files/file_practice.txt", "r+") as hw:
    str = hw.read()
    if len(str) % 2 == 0:
        hw.write("\nthe end")
    else:
        hw.write("\nbye")

    hw.seek(0)
    print(hw.read())
    hw.tell()

"""
    5.*
    В средину файла file_practice.txt вставить строку '*some inserted text*'
"""

with open("files/file_practice.txt", "r+") as hw:
    add = hw.read()
    idx = add.find("\n")
    hw.write("\n" + add[:idx] + "\n*some inserted text*" + add[idx:])




