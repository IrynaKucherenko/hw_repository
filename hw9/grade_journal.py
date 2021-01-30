"""
    Пользователь вводит количество студентов n.
    После чего вводит n строк, в которых записана фамилия и балл через пробел.

    Программа выводит список фамилий, отсортированный по их баллам по убыванию.

    Пример:

    [out] Введите количество студентов:
    [in]  3

    [out] Введите фамилию и балл:
    [in]  Иванов 87

    [out] Введите фамилию и балл:
    [in]  Смирнов 90

    [out] Введите фамилию и балл:
    [in]  Фролов 89

    [out]
        1. Смирнов
        2. Фролов
        3. Иванов
"""


def main():
    try:
        list_grade_students = []
        number = int(input("Введите количество студентов: "))
        for i in range(number):
            i = str(input("Введите фамилию и балл: ")).split()
            name_gr = list(i)
            name = (name_gr[0]).title()
            grade = int(name_gr[1])
            name_grate = {"фамилия": name, "балл": grade}
            list_grade_students.append(name_grate)
            my_list = (sorted(list_grade_students, key=lambda data: data["балл"], reverse=True))
        c = 0
        for i in my_list:
            c += 1
            print(f"{c}.", i.get("фамилия"))
    except ValueError:
        print("Invalid format. Enter the number")
        return main()




if __name__ == '__main__':
    main()
