"""
    Написать функцию, которая будет проверять счастливый билетик или нет.

    Билет счастливый, если сумма одной половины цифр равняется сумме второй.
"""


def is_lucky(ticket_num):
    ticket_num = str(ticket_num)
    lst = list(ticket_num)
    dig = [int(i) for i in lst]
    len_l = len(dig) // 2
    return sum(dig[:len_l]) == sum(dig[-len_l:])


assert is_lucky(1230) is True
assert is_lucky(239017) is False
assert is_lucky(134008) is True
assert is_lucky(15) is False
assert is_lucky(2020) is True
assert is_lucky(199999) is False
assert is_lucky(77) is True
assert is_lucky(479974) is True

print('All tests passed successfully!')
