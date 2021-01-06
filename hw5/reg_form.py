"""
    Необходимо реализовать форму регистрации пользователей.
    Поля формы: номер телефона, email, пароль и подтверждение пароля.

    !!! Для решения необходимо использовать функции и рекурсию, а не циклы. !!!

    пункты с ** - дополнительно, но не обязательно (не влияет на оценку)

    1. Пользователь вводит номер телефона.
        Программа проверяет валидность телефона:
        - приводит номер к формату 380501234567
        - если номер не получается привести к нужному формату
            то запрашивает ввод номера еще раз
            и так до тех пор, пока не будет введен валидный номер

    2. Пользователь вводит email.
        Программа проверяет валидность email:
        - должен иметь длину 6 символов и больше
            (функция len())
        - содержать один символ '@'
            (строчный метод count())
        - ** содержать логин и полный домен (логин@полный.домен)
        Пользователь может вводить email до тех пор, пока он не будет валидным.

    3. Пользователь ввод пароль.
        Программа проверяет надежность пароля:
        - минимум 8 символов
            (функция len())
        - пароль не должен содержать пробельные символы
            (строчный метод isspace())
        - наличие минимум 1 буквы в верхнем регистре, 1 в нижнем и 1 цифры
            (строчные методы isupper(), islower(), isdigit())
        - ** наличие минимум 1 спец символа

    4. После успешного ввода пароля пользователь вводит подтверждение пароля.
        Если подтверждение пароля не сходится с введенным паролем,
        то возвращаемся к пункту 3.

    Программа выводит сообщение:

    Поздравляем с успешной регистрацией!
    Ваш номер телефона: +380501234567
    Ваш email: example@mail.com
    Ваш пароль: **********

"""


def main():
    number = phone_number()
    email = mail()
    hidden_pas = pas()
    print(f"Congratulations on successful registration! \
    \nYour phone number: {number} \nYour email: {email} \nYour password: {hidden_pas}")


def phone_number():
    number = input("Phone number:")
    a = ("".join(s for s in number if s.isdigit()))
    r_number = ("+38" + a[-10:])
    number = r_number

    if len(r_number) != 13:
        return phone_number()
    return number


def mail():
    email = input("e-mail:")
    if len(email) >= 6 and email[0] != "@" and email.count("@") == 1:
        return email
    return mail()


def pas():
    password = input("pass_: ")

    if len(password) < 8:
        print("less then 8 sings")
    counter_u = 0
    counter_l = 0
    counter_d = 0
    counter_s = 0

    for chair in password:
        if chair.isupper() is True:
            counter_u += 1
        elif chair.islower() is True:
            counter_l += 1
        elif chair.isdigit() is True:
            counter_d += 1
        elif chair.isspace() is True:
            counter_s += 1
    if counter_u != 0 and counter_l != 0 and counter_d != 0 and counter_s == 0:
        answer = str(input("confirm password:"))
        if answer == password:
            hidden_pas = len(password) * "*"
            return hidden_pas
        else:
            return pas()

    else:
        return pas()


main()



