import json
import random
import string


users = {}
try:
    with open("test.json", "r") as f:
        data = f.read()
        users = json.loads(data)
except:
    print(" data available")


def save_update():
    try:
        with open("test.json", "w") as f:
            f.write(json.dumps(users, indent=4))
        print("Data successfully updated")
    except Exception:
        print("Can't save data")


def main():
    print("=================")
    print("REGISTRATION FORM")
    a = input(
        "Main menu:\n"
        "1. Register a new user\n"
        "2. View users list\n"
        "3. exit\n"
        "Enter: "
    )

    if a == "1":
        return get_register()
    elif a == "2":
        return get_review()
    elif a == "3":
        print("Have a nice day:) Bye!")
        print("======================")
    else:
        return main()


def get_register():
    number = get_phone_number()
    email = get_mail()
    password = get_pas()
    if users.get(number) is None:
        users[number] = {f"email": email, "password": password}
    hidden_pas = len(password) * "*"
    print("===========================================")
    print(f"Congratulations on successful registration! \
        \nYour phone number: {number} \nYour email: {email} \nYour password: {hidden_pas}")
    print("===========================================")

    with open("test.json", "w") as f:
        f.write(json.dumps(users, indent=4))
    return main()


def get_phone_number():
    num = input("Phone number:")
    a = ("".join(s for s in num if s.isdigit()))
    number = ("+38" + a[-10:])
    if len(number) != 13:
        print("Invalid format. Try again")
        return get_phone_number()
    return number


def get_mail():
    email = input("e-mail:")
    if len(email) >= 6 and email[0] != "@"\
            and email[-1] != "@"\
            and email.count("@") == 1\
            and email.count(".") != [-1]\
            and email.count(".") == 1:
        return email
    else:
        print("Invalid format. Try again")
        return get_mail()


def get_pas():
    password = input(
        "The password must contain upper, lower case letters, digit!\nPass: ")
    if len(password) < 8:
        print("password must be more than 8 characters. Try again")
        return get_pas()
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
        answer = input("confirm password:")
        if answer == password:
            return password
        else:
            print("passwords are different! Try again")
            return get_pas()
    else:
        print("Invalid format. Try again")
        return get_pas()


def new_pas(number):
    pas = string.ascii_letters + string.digits
    size = 8
    new_password = ("".join(random.choice(pas) for x in range(size)))
    users[number]["password"] = new_password
    save_update()
    print("new password:", new_password)
    print("=======================")
    return main()


def dell_user(number):
    d = "Are you sure you want to delete " + number + " y/n:"
    choice = input(d)
    if choice == "y":
        del users[number]
        save_update()
        print("User ", number, " deleted")
        print("=============================")
        return main()
    print("Deletion is canceled")
    print("====================")
    return main()


def get_review():
    c = 0
    for i in users:
        if i in users:
            c += 1
    print("registered users:", c)
    if c == 0:
        return main()
    ask = input("show all users? y/n: ")
    ulist = []
    if ask != "n":
        c = 0
        for number in users.keys():
            c += 1
            print(c, number)
            ulist.append(number)
        user_review(ulist)
    else:
        return main()


def user_review(ulist):
    a = input("press '0' for main menu or select sequence number of user: ")
    if a == "0":
        return main()

    try:
        index = int(a)
        index = index - 1
        number = ulist[index]
    except Exception:
        print("can't find user for -", a)
        return user_review(ulist)
    print(" ", "\n", number, "is selected")
    print(users[number], "\n")
    get_choice(number)


def get_choice(number):
    x = input("1. reset the password?\n2. delete the user?\n3. return to the main menu\n4. exit\nenter: ")
    if x == "1":
        return new_pas(number)
    elif x == "2":
        return dell_user(number)
    elif x == "3":
        return main()
    else:
        print("please, make your choice")
        return get_choice(number)


if __name__ == "__main__":
    main()

