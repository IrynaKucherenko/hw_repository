import random
import string

# 1. Создайте переменную x, которая равняется 2 в степени 3
x = 2 ** 3

# 2. Прибавьте к x 3
x += 3

# 3. Сгенерируйте список num_list длиной x, из случайных чисел в диапазоне от 1 до x

list = string.digits
num_list = ["".join(random.choice(list) for x in range(x))]
print(num_list)

# 4. Выведите на экран числа из списка num_list в обратном порядке
#    (от последнего до первого элемента) через пробел

my_list = []
for i in num_list:
    for c in i:
        my_list.append(c)
revers_list = my_list[::-1]
my_string = " ".join(revers_list)
print(my_string)

# 5. Вставьте в средину списка число 11.

my_list.insert(len(my_list) // 2, 11)
print(my_list)

# 6. Запишите в файл list_info.txt строчки
#    - количество элементом списка
#    - количество уникальных элементов списка
#    - самое маленькое число списка
#    - сумму чисел списка кратных 3

list_unique = []
num = []
counter = 0
count_unique = 0
amount = 0
for i in my_list:
    counter += 1

for i in my_list:
    if i not in list_unique:
        list_unique.append(i)

for i in list_unique:
    count_unique += 1

for i in my_list:
    s = int(i)
    if i not in num:
        num.append(s)
min_num = min(num)

for i in num:
    if i % 3 == 0:
        amount += i

print(f"количество элементом списка: {counter}"
      f"\nколичество уникальных элементов списка: {count_unique}"
      f"\nсамое маленькое число списка: {min_num}"
      f"\nсумму чисел списка кратных 3: {amount}\n"
      )
dd = (f"{counter}\n{count_unique}\n{min_num}\n{amount}\n")
with open("list_info.txt", "w+") as f:
    f.write(dd)

# 7. Создайте список countries_info из 3 словарей c ключами
#    'country', 'population', 'cities' и заполните их любыми значениями
#    ('country' - строка, 'population' - число, 'cities' - список строк)

countries_info = []
dict_1 = {"Ukraine": "Kiev", "population": 41902416, "cities": ["Kharkiv", "Odesa", "Dnipro"]}
dict_2 = {"France": "Paris", "population": 65495423, "cities": ["Marseille", "Lyon", "Toulouse"]}
dict_3 = {"Austria": "Vienna", "population": 8902600, "cities": ["Graz", "Linz", "Salzburg"]}

countries_info.append(dict_1)
countries_info.append(dict_2)
countries_info.append(dict_3)

print(countries_info)

# 8. Отсортируйте в каждом словаре cities по длине строк в порядке убывания
for dict_ in countries_info:
    for key, value in dict_.items():
        cities = (dict_.get("cities"))
        for i in cities:
            print(sorted(cities, key=len, reverse=False))

# 9. Отсортируйте список словарей countries_info
#    по ключу 'population' в порядке возрастания

print(sorted(countries_info, key=lambda data: data["population"]))

# 10. Напишите функцию create_country_info, которая принимает 3 параметра
#     country, population и cities
#     и возвращает словарь типа
#     {'country': , 'population': 123, 'cities': ['New York', 'Los Angeles', 'Portland']}

country = 'USA'
population = 123
cities = ['New York', 'Los Angeles', 'Portland']


def create_country_info(country, population, cities):
    country_info = dict(zip(["country", "population", "cities"], [country, population, cities]))
    return country_info


print(create_country_info(country, population, cities))


# 11. Создайте словарь с помощью функции create_country_info
#     и вставьте его в начало списка countries_info

def create_country_info(country, population, cities):
    countries_info = []
    a = dict(zip(["country", "population", "cities"], [country, population, cities]))
    countries_info.append(a)
    return countries_info


print(create_country_info(country, population, cities))
