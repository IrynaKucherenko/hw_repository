"""
    Напишите функцию, которая принимает список чисел
    и возвращает отсортированный список,
    при условии, что все числа -1 остаются на своих местах.

    [in]   [6, 3, -1, 4, 2, -1, 1]
    [out]  [1, 2, -1, 3, 4, -1, 6]
"""


def sort_ascending(x):
    temp_list = []
    for i in range(len(x)):
        if x[i] > 0:
            temp_list.append(x[i])
            x[i] = " "

    temp_list.sort(reverse=True)

    for i in range(len(x)):
        if x[i] == " ":
            x[i] = temp_list.pop()
    return x


test_1 = [-1, 150, 190, 170, -1, -1, 160, 180]
assert sort_ascending(test_1) == [-1, 150, 160, 170, -1, -1, 180, 190]

test_2 = [-1, -1, -1, -1, -1]
assert sort_ascending(test_2) == [-1, -1, -1, -1, -1]

test_3 = [4, 2, 9, 11, 2, 16]
assert sort_ascending(test_3) == [2, 2, 4, 9, 11, 16]

test_4 = [23, 54, -1, 43, 1, -1, -1, 77, -1, -1, -1, 3]
assert sort_ascending(test_4) == [1, 3, -1, 23, 43, -1, -1, 54, -1, -1, -1, 77]

test_5 = [-1]
assert sort_ascending(test_5) == [-1]

print('All tests passed successfully!')
