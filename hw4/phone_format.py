"""
    Написать программу, которая принимает номер телефона в любом формате:
    +38 (050) 12-34-567 или 099 123 -45 67 или 80501234567 или 888 050 123 4567
    а выводит в формате: 380501234567.

    Если цифр в номере недостаточно, чтобы описать номер в нужном формате -
        попросить пользователя повторить ввод.
"""

while True:

    input_number = (input('Enter phone number: '))

    number = ("".join(s for s in input_number if s.isdigit()))
    right_number = ("38" + number[-10:])

    if len(right_number) == 12:
        print(right_number)
        break
    else:
        print("Please, try again")





