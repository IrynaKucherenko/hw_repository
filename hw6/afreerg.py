import re

phone_book = open("files/phone_book.txt", "r+")

string = phone_book.read()

print(string)

new_string = re.sub('[^a-zA-Z0-9 \n\.]', '', string)
print(new_string)
s = [new_string]
print(s)

l = new_string.replace(" ", "")
print(l)

ll = l.split('/')
print(l)



