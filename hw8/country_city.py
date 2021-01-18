"""
    1. Реализовать функцию get_country(city), которая принимает название города
    и возвращает страну, которой он принадлежит.

    Покрыть функцию тестами.


    2. Релизовать функцию groupping_data(data), которая принимает словарь data
    и возвращает отформатированные данные в виде списка словарей с ключами
    'country', 'capital' и 'cities'.
"""

data = {
    'Ukraine': ['Kiev', 'Kharkiv', 'Odesa', 'Dnipro'],
    'France': ['Paris', 'Marseille', 'Lyon', 'Toulouse'],
    'Austria': ['Vienna', 'Graz', 'Linz', 'Salzburg'],
    'Germany': ['Berlin', 'Hamburg', 'Munich', 'Frankfurt']
}


def get_country(city):
    for key, value in data.items():
        if city in value:
            return key


t_1 = "Kiev"
assert get_country(t_1) == "Ukraine"

t_2 = "Marseille"
assert get_country(t_2) == "France"

t_3 = "Linz"
assert get_country(t_3) == "Austria"

t_4 = "Frankfurt"
assert get_country(t_4) == "Germany"

print("====ok====")


a = {
    'Ukraine': ['Kiev', 'Kharkiv', 'Odesa', 'Dnipro'],
    'France': ['Paris', 'Marseille', 'Lyon', 'Toulouse'],
    'Austria': ['Vienna', 'Graz', 'Linz', 'Salzburg'],
    'Germany': ['Berlin', 'Hamburg', 'Munich', 'Frankfurt']
}


def groupping_data(a: dict):
    my_list = []
    for key, value in a.items():
        x = (key, value[0], value[1:])
        country = (x[0])
        capital = (x[1])
        cities = (x[2])
        b = dict(zip(["country", "capital", "cities"], [country, capital, cities]))
        my_list.append(b)
    return my_list


print(groupping_data(a))
